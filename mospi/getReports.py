# https://www.mospi.gov.in/download-reports

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

def store_firstlevel(db):

    file1 = open("./firstlevel.json", "w")
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

        r = requests.post('https://www.mospi.gov.in/views/ajax', headers=headers, data=f"view_name=statistical_publications&view_display_id=page_1&view_args=&view_path=download-reports&view_base_path=download-reports&view_dom_id=458022aa6cf9e73b8cc6754b9d05b956&pager_element=0&main_cat=All&publication_report_cat=All&sub_category=All&page={page_number}&ajax_html_ids%5B%5D=base_url&ajax_html_ids%5B%5D=wrapper&ajax_html_ids%5B%5D=header&ajax_html_ids%5B%5D=block-lang-dropdown-language&ajax_html_ids%5B%5D=lang_dropdown_form_language&ajax_html_ids%5B%5D=lang-dropdown-select-language&ajax_html_ids%5B%5D=block-block-23&ajax_html_ids%5B%5D=accessControl&ajax_html_ids%5B%5D=large&ajax_html_ids%5B%5D=larger&ajax_html_ids%5B%5D=normal&ajax_html_ids%5B%5D=wob&ajax_html_ids%5B%5D=mainNav&ajax_html_ids%5B%5D=block-nice-menus-1&ajax_html_ids%5B%5D=nice-menu-1&ajax_html_ids%5B%5D=block-search-form&ajax_html_ids%5B%5D=search-block-form&ajax_html_ids%5B%5D=edit-search-block-form--2&ajax_html_ids%5B%5D=edit-actions&ajax_html_ids%5B%5D=edit-submit--2&ajax_html_ids%5B%5D=block-block-11&ajax_html_ids%5B%5D=inner_con&ajax_html_ids%5B%5D=block-system-main&ajax_html_ids%5B%5D=views-exposed-form-statistical-publications-page-1&ajax_html_ids%5B%5D=edit-combine-wrapper&ajax_html_ids%5B%5D=edit-combine&ajax_html_ids%5B%5D=edit-main-cat&ajax_html_ids%5B%5D=sub_cat_show_hide&ajax_html_ids%5B%5D=edit-publication-report-cat&ajax_html_ids%5B%5D=sub_sub_cat_show_hide&ajax_html_ids%5B%5D=edit-sub-category&ajax_html_ids%5B%5D=edit-submit-statistical-publications&ajax_html_ids%5B%5D=edit-reset&ajax_html_ids%5B%5D=printData&ajax_html_ids%5B%5D=block-views-download-report-menus-block&ajax_html_ids%5B%5D=block-views-bottom-slider-block&ajax_html_ids%5B%5D=footer&ajax_html_ids%5B%5D=block-block-1&ajax_html_ids%5B%5D=block-visitors-count-site-visitor-count&ajax_html_ids%5B%5D=block-block-2&ajax_html_ids%5B%5D=backtotop&ajax_html_ids%5B%5D=ui-dialog-title-event-popup-container&ajax_html_ids%5B%5D=event-popup-container&ajax_html_ids%5B%5D=cboxOverlay&ajax_html_ids%5B%5D=colorbox&ajax_html_ids%5B%5D=cboxWrapper&ajax_html_ids%5B%5D=cboxTopLeft&ajax_html_ids%5B%5D=cboxTopCenter&ajax_html_ids%5B%5D=cboxTopRight&ajax_html_ids%5B%5D=cboxMiddleLeft&ajax_html_ids%5B%5D=cboxContent&ajax_html_ids%5B%5D=cboxTitle&ajax_html_ids%5B%5D=cboxCurrent&ajax_html_ids%5B%5D=cboxPrevious&ajax_html_ids%5B%5D=cboxNext&ajax_html_ids%5B%5D=cboxSlideshow&ajax_html_ids%5B%5D=cboxLoadingOverlay&ajax_html_ids%5B%5D=cboxLoadingGraphic&ajax_html_ids%5B%5D=cboxMiddleRight&ajax_html_ids%5B%5D=cboxBottomLeft&ajax_html_ids%5B%5D=cboxBottomCenter&ajax_html_ids%5B%5D=cboxBottomRight&ajax_page_state%5Btheme%5D=mospi&ajax_page_state%5Btheme_token%5D=LSbLY4eF0Ewio55JIppg8pYgfaQ4aQYA3VaczCrGess&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.core.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.button.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.resizable.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.dialog.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fviews_slideshow.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcalendar%2Fcss%2Fcalendar_multiday.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fcomment%2Fcomment.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_api%2Fdate.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_popup%2Fthemes%2Fdatepicker.1.7.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_repeat_field%2Fdate_repeat_field.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Ffield%2Ftheme%2Ffield.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fnode%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsearch%2Fsearch.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fuser%2Fuser.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fyoutube%2Fcss%2Fyoutube.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fforum%2Fforum.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fcss%2Fviews.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fckeditor%2Fcss%2Fckeditor.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcolorbox%2Fstyles%2Fdefault%2Fcolorbox_style.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fcss%2Fctools.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fevent_calendar%2Fevent_popup%2Fcss%2Fevent_popup.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Ftaxonomy_access%2Ftaxonomy_access.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fcss%2Fnice_menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fcss%2Fnice_menus_default.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fcontrib%2Fviews_slideshow_cycle%2Fviews_slideshow_cycle.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Flang_dropdown%2Flang_dropdown.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fcss%2Fstyle.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fcss%2Fie.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fcss%2Fie6.css%5D=1&ajax_page_state%5Bjs%5D%5B0%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Fpublication_view%2Fpublication_ajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Ftelephone_module%2Ftelephone_dir_ajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fjs%2Fgo_offline.js%5D=1&ajax_page_state%5Bjs%5D%5Bmy-new-jquery%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.once.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fdrupal.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.core.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.widget.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.button.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.mouse.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.draggable.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.position.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.resizable.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fui%2Fjquery.ui.dialog.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fjquery.ui.dialog.patch.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.cookie.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.form.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fjquery.bgiframe.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fjquery.hoverIntent.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fsuperfish.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fnice_menus.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fjs%2Fviews_slideshow.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fadmin_menu%2Fadmin_devel%2Fadmin_devel.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Flibraries%2Fcolorbox%2Fjquery.colorbox-min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcolorbox%2Fjs%2Fcolorbox.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcolorbox%2Fstyles%2Fdefault%2Fcolorbox_style.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcolorbox%2Fjs%2Fcolorbox_load.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcolorbox%2Fjs%2Fcolorbox_inline.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fevent_calendar%2Fevent_popup%2Fjs%2Fevent_popup.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fevent_calendar%2Fevent_popup%2Fjs%2Fevent_popup_validate.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fbase.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fprogress.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Flibraries%2Fjquery.cycle%2Fjquery.cycle.all.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fcontrib%2Fviews_slideshow_cycle%2Fjs%2Fviews_slideshow_cycle.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fajax_view.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Flang_dropdown%2Flang_dropdown.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fjs%2Fjquery.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fjs%2Fjquery-migrate-1.2.1.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fjs%2Fmodernizr-custom-33193.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fjs%2Ffunctions.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fjs%2Fgeneral.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fmospi%2Fjs%2Fbruteforce.js%5D=1")
        html = r.json()[2]['data']
        soup = BeautifulSoup(html, 'html.parser')

        db = []

        for link in soup.find_all('a')[:5]:
            clean_link = link.get('href')
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
    for i in tqdm(range(0, 153)):
        page_links = get_page(i)
        complete = [*complete, *page_links]

    store_firstlevel(complete)

    print('len', len(complete))

get_all_pages()