import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

def store_secondlevel(db):

    file1 = open("secondlevel.json", "w")
    file1.write(json.dumps(db))
    file1.close()


def get_page(link):

    r = requests.get(link)

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

        return [
            description,
            external_link
        ]
    else:
        return ["", ""]

def get_all_pages():

    f = open('./firstlevel.json')
    data = json.load(f)
    f.close()


    complete = []
    for row in tqdm(data):
        page_details = get_page(row[1])
        complete.append([*row, *page_details])

    store_secondlevel(complete)


get_all_pages()
