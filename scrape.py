import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

def store_firstlevel(db):

    file1 = open("firstlevel.json", "w")
    file1.write(json.dumps(db))
    file1.close()


def get_page(page_number):

    try:
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-GB,en;q=0.5",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Brave\";v=\"110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "x-requested-with": "XMLHttpRequest"
        }

        r = requests.post('https://www.india.gov.in/views/ajax', headers=headers, data=f"page={page_number}&view_name=metadata_for_schemes&view_display_id=block&view_args=166854&view_path=taxonomy%2Fterm%2F166854&view_base_path=my-government%2Fschemes&view_dom_id=27282a66431e23e069aaed6849130249&pager_element=0&ajax_html_ids%5B%5D=header&ajax_html_ids%5B%5D=block-block-4&ajax_html_ids%5B%5D=text_resize_decrease&ajax_html_ids%5B%5D=text_resize_reset&ajax_html_ids%5B%5D=text_resize_increase&ajax_html_ids%5B%5D=switch-lang&ajax_html_ids%5B%5D=logo&ajax_html_ids%5B%5D=menu-bar&ajax_html_ids%5B%5D=block-panels-mini-main-menu&ajax_html_ids%5B%5D=mini-panel-main_menu&ajax_html_ids%5B%5D=nav&ajax_html_ids%5B%5D=block-block-16&ajax_html_ids%5B%5D=searchForm&ajax_html_ids%5B%5D=search_key&ajax_html_ids%5B%5D=edit-submit1&ajax_html_ids%5B%5D=auto_suggesion&ajax_html_ids%5B%5D=advsearchbtn&ajax_html_ids%5B%5D=light&ajax_html_ids%5B%5D=views-exposed-form-advance-metadata-search-page-1&ajax_html_ids%5B%5D=edit-title-wrapper&ajax_html_ids%5B%5D=edit-title&ajax_html_ids%5B%5D=edit-term-node-tid-depth-wrapper&ajax_html_ids%5B%5D=edit-term-node-tid-depth&ajax_html_ids%5B%5D=edit-sort-by&ajax_html_ids%5B%5D=edit-sort-order&ajax_html_ids%5B%5D=edit-submit-advance-metadata-search&ajax_html_ids%5B%5D=block-views-most-search-block&ajax_html_ids%5B%5D=main&ajax_html_ids%5B%5D=content-column&ajax_html_ids%5B%5D=main-content&ajax_html_ids%5B%5D=content&ajax_html_ids%5B%5D=block-system-main&ajax_html_ids%5B%5D=leftside-bar&ajax_html_ids%5B%5D=views-exposed-form-metadata-for-schemes-block&ajax_html_ids%5B%5D=edit-title-wrapper&ajax_html_ids%5B%5D=edit-title&ajax_html_ids%5B%5D=edit-submit-metadata-for-schemes&ajax_html_ids%5B%5D=block-suggest-metadata-suggest-metadata&ajax_html_ids%5B%5D=info-suggestion-wrapper&ajax_html_ids%5B%5D=information-suggestion-wrapper&ajax_html_ids%5B%5D=suggest_us&ajax_html_ids%5B%5D=metadata-suggestion-form-ajax&ajax_html_ids%5B%5D=edit-metadata-suggestion&ajax_html_ids%5B%5D=metadata_suggestion_form&ajax_html_ids%5B%5D=footer&ajax_html_ids%5B%5D=footertop&ajax_html_ids%5B%5D=menutext&ajax_html_ids%5B%5D=block-block-6&ajax_html_ids%5B%5D=fotter-bottom&ajax_html_ids%5B%5D=block-block-7&ajax_html_ids%5B%5D=block-block-9&ajax_page_state%5Btheme%5D=npi_adaptive&ajax_page_state%5Btheme_token%5D=BYb-NXoZhzqkX0FERCmMpVPo157_o2yRoKjcDcawYX8&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fcalendar%2Fcss%2Fcalendar_multiday.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fdate%2Fdate_api%2Fdate.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fdate%2Fdate_popup%2Fthemes%2Fdatepicker.1.7.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fdate%2Fdate_repeat_field%2Fdate_repeat_field.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Ffield%2Ftheme%2Ffield.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Flogintoboggan%2Flogintoboggan.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fnode%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsearch%2Fsearch.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fuser%2Fuser.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fviews%2Fcss%2Fviews.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fctools%2Fcss%2Fctools.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fpanels%2Fcss%2Fpanels.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fat_core%2Fcss%2Fat.layout.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fnpi_adaptive%2Fcss%2Ffont-awesome.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fnpi_adaptive%2Fcss%2Fglobal.custom.responsive.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fnpi_adaptive%2Fcss%2Fglobal.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fnpi_adaptive%2Fcss%2Fglobal.styles.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fnpi_adaptive%2Fcss%2Fprint.css%5D=1&ajax_page_state%5Bcss%5D%5Bpublic%3A%2F%2Fadaptivetheme%2Fnpi_adaptive_files%2Fnpi_adaptive.default.layout.css%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fjquery_update%2Freplace%2Fjquery%2F3.1%2Fjquery.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery-extend-3.4.0.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery-html-prefilter-3.5.0-backport.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.once.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fdrupal.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fjquery_update%2Freplace%2Fui%2Fexternal%2Fjquery.cookie.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fjquery_update%2Freplace%2Fjquery.form%2F4%2Fjquery.form.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fjquery_update%2Fjs%2Fjquery_update.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fadmin_menu%2Fadmin_devel%2Fadmin_devel.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustoms%2Fhb_documents%2Fhb_documents.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustoms%2Fhb_schemes%2Fhb_schemes.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustoms%2Fwebform_email_reply%2Fscript.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fviews%2Fjs%2Fbase.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fprogress.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontributed%2Fviews%2Fjs%2Fajax_view.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fnpi_adaptive%2Fscripts%2Fjquery.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fadaptivetheme%2Fnpi_adaptive%2Fscripts%2Fcustom.js%5D=1&ajax_page_state%5Bjquery_version%5D=3.1")
        html = r.json()[2]['data']
        soup = BeautifulSoup(html, 'html.parser')

        db = []

        for link in soup.find_all('a')[:5]:
            clean_link = f"https://www.india.gov.in{link.get('href')}";
            db.append([
                link.get_text(),
                clean_link
            ])

        return db
    
    except:
        print('error on page', page_number)
        return []


def get_all_pages():
    complete = []
    for i in tqdm(range(0, 185)):
        page_links = get_page(i)
        complete = [*complete, *page_links]

    store_firstlevel(complete)

    print('len', len(complete))

get_all_pages()