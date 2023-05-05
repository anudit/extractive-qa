import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from pprint import pprint

def store_secondlevel(db):

    file1 = open("./secondlevel.json", "w")
    file1.write(json.dumps(db))
    file1.close()

def get_page_summary(url):

    try:    
        r = requests.get(url, timeout=20)

        if (r.status_code == 200):
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all('a');
            pdf_links = []
            for link in links:
                l =link.get('href').lower()
                if '.pdf' in l or '.csv' in l:
                    if 'http' in l:
                        pdf_links.append(l)
                    else:
                        pdf_links.append(url + l)
            return {
                "links": pdf_links
            }
        else:
            return False
    except:
        return False


def get_page(link):

    try:
        r = requests.get(link, timeout=20)

        if (r.status_code == 200):
            soup = BeautifulSoup(r.text, 'html.parser')

            top_panel = soup.find(
                class_="views-row views-row-1 views-row-odd views-row-first views-row-last"
            )

            description = top_panel.find_all(
                class_="field-content"
            )[1].get_text()
            external_link = top_panel.find_all(
                class_="field-content"
            )[0].find('a').get('href')

            summ_ext = get_page_summary(external_link)

            related_links = []
            panels = soup.find_all(
                'ol'
            )
            if(len(panels)>1):
                bottom_panel_links = panels[1].find_all(class_="views-row")
                for li in bottom_panel_links:
                    ele = li.find('h3').find('a')
                    desc = li.find(class_='field-content').get_text()
                    deets = {
                        "name": ele.get_text(),
                        "link": ele.get('href'),
                        "description": desc
                    }

                    summ = get_page_summary(ele.get('href'))
                    deets['summary']=summ

                    related_links.append(deets)



            parsed = {
                "description": description,
                "external_link": external_link,
                "external_summary": summ_ext,
                "related_links": related_links
            }
            
            return parsed
        else:
            return False
    
    except:
         return False

def get_all_pages():

    f = open('./firstlevel-1.json')
    data = json.load(f)
    f.close()

    complete = []
    for row in tqdm(data):
        gov_parsed = get_page(row[1])
        complete.append({
            "name": row[0],
            "gov_link": row[1],
            "gov_parsed": gov_parsed,
        })

        store_secondlevel(complete)


get_all_pages()
