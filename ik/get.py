from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import os
from selenium import webdriver
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from enum import Enum
import re


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    driver.implicitly_wait(2)
    return driver

def store_firstlevel(db, extra_fn = "", dir="./saves"):

    file1 = open(f"{dir}/caseheads-{extra_fn}.json", "w")
    file1.write(json.dumps(db))
    file1.close()

def parse_plist(plist):
    final_string = ''
    citations = []
    for p in plist:
        final_string += p.get_text()
        cits = p.find_all('a')
        if cits:
            for cit in cits:
                href = cit.get('href')
                if (href.startswith('/doc/')):
                    citations.append(int(href.replace('/doc', '').replace('/','')))  

    return final_string, citations       

def get_from_sel(url, wait_for="results_content"):

    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, wait_for)))
        src = driver.page_source
        return src
    except:
        return False
    
def get_from_sel2(url, driver):

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "searchbox_top")))
        src = driver.page_source
        return src
    except:
        return False

return_error_state = Enum('ReturnErrorState', ['HTML_FETCH_FAILED', 'NO_RESULTS'])


def get_full_document_details(doc_id, driver):
    url = f"https://indiankanoon.org/doc/{doc_id}"
    html = get_from_sel2(url, driver)

    if (html != False):

        soup = BeautifulSoup(html, 'html.parser')

        title_check = soup.find("div", class_="doc_title")

        if (title_check):

            deets = {
                't': soup.find("div", class_="doc_title").get_text().replace('\n', ''),
                's': soup.find("div", class_="docsource_main").get_text().replace('\n', ''),
                'id': doc_id,
                'd': '',
                'c': [],
                'cl': 0,
                'b': ''
            }
            prelist = soup.find_all("pre", id=re.compile('pre_'))
            if (prelist):
                final_string, citations = parse_plist(prelist)
                deets['d'] += final_string
                deets['c'] += citations
                deets['cl'] += len(citations)
            
            plist = soup.find_all("p", id=re.compile('p_'))
            if (plist):
                final_string, citations = parse_plist(plist)
                deets['d'] += final_string
                deets['c'] += citations
                deets['cl'] += len(citations)


            author = soup.find("div", class_="doc_author")
            if author:
                deets['a'] = author.get_text().replace('\n', '')

            bench = soup.find("div", class_="doc_bench")
            if bench:
                bench['a'] = bench.get_text().replace('\n', '')
                
            return deets

        else:
            return return_error_state.NO_RESULTS;
    else:
        return return_error_state.HTML_FETCH_FAILED



def parse_page(start_time, end_time, page = 1):
    url = f"https://indiankanoon.org/search/?formInput=fromdate%3A+{start_time}+todate%3A+{end_time}&pagenum={page}"
    # print('opening', url)
    html = get_from_sel(url)
    if (html!= False):
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.find_all("div", class_="result")

        if results:

            data = []
            for result in results:
                deets = {
                    't': result.find("div", class_="result_title").get_text().replace('\n', ''),
                    's': result.find("div", class_="docsource").get_text().replace('\n', '')
                }
                cites = result.find_all("a", class_="cite_tag")
                if (cites and len(cites) == 3):
                    deets['id']= int(result.find_all("a", class_="cite_tag")[2].get('href').replace('/doc', '').replace('/',''))
                    deets['ci']= int(result.find_all("a", class_="cite_tag")[0].get_text().replace('\n', '')[len('Cites '):])
                    deets['cb']= int(result.find_all("a", class_="cite_tag")[1].get_text().replace('\n', '')[len('Cited by '):])
                
                data.append(deets)

            return data

        else:
            # print('false', url)
            return return_error_state.NO_RESULTS
    else:
        # print('false', url)
        return return_error_state.HTML_FETCH_FAILED

def run():

    for year in range(1900, 1947):
        complete_data = [] 
        for date in (pbar := tqdm(pd.date_range(start=f"01-01-{year}",end=f"12-31-{year}"))):
            date_string = f"{date.day}-{date.month}-{date.year}"
            for i in range(0, 40):
                pbar.set_description(f"{date_string}/{i} | {len(complete_data)}")
                page_data =  parse_page(
                    date_string,
                    date_string,
                    i
                )
                if page_data == return_error_state.NO_RESULTS:
                    break
                if page_data == return_error_state.HTML_FETCH_FAILED:
                    continue
                else:
                    complete_data += page_data

        store_firstlevel(complete_data, str(year))

def run_full_year():

    for year in (pbar := tqdm(range(1901, 1947))):
        complete_data = [] 
        date_start = f"1-1-{year}"
        date_end = f"31-12-{year}"

        for i in range(0, 40):
            pbar.set_description(f"{year}/{i} | {len(complete_data)}")
            page_data =  parse_page(
                date_start,
                date_end,
                i
            )
            if page_data == return_error_state.NO_RESULTS:
                break
            elif page_data == return_error_state.HTML_FETCH_FAILED:
                continue
            else:
                complete_data += page_data

        store_firstlevel(complete_data, str(year))

def run_docid_wise(list_of_ids, driver, name):

    complete_data = []
    no_res = 0
    failed = 0

    for ind, doc_id in (pbar := tqdm(enumerate(list_of_ids))):
        pbar.set_description(f"{doc_id}|f:{len(complete_data)}|e:{no_res}|f:{failed}")
        page_data =  get_full_document_details(doc_id, driver)
        if page_data == return_error_state.NO_RESULTS:
            no_res+=1
            continue
        elif page_data == return_error_state.HTML_FETCH_FAILED:
            failed+=1
            continue
        else:
            complete_data.append(page_data)

        if ind%1000 == 0: #snapshot the progress every 1000 ids.
            store_firstlevel(complete_data, name, './docs')


    store_firstlevel(complete_data, name, './docs')

    return True

def chunks(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def main():
    cpu_count = os.cpu_count()
    ids = [x for x in range(0, 100_000)]
    with ThreadPoolExecutor(max_workers=cpu_count) as executor:
        executor.map(
            run_docid_wise, 
            chunks(ids, int(len(ids)/cpu_count)), 
            [create_driver() for _ in range(0, cpu_count)],
            [f"core_{x}" for x in range(0, cpu_count)]
        )


if __name__ == '__main__':
    main()


# run()
# print(getDoc(199498621)['c'])

# print(get_from_sel('https://indiankanoon.org/doc/117/'))

# {
#     t: title
#     s: source
#     ci: cites
#     cb: citedby
# }

# 107382 across 113 years -  before fix
# 124788 across 113 years -  full year