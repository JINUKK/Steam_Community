import requests
import json
from steam_api_key import my_key


def steam_app_data(app):
    detail_url = "https://store.steampowered.com/api/appdetails?appids=" + app
    custom_headers = {
        'Cookie': 'Steam_Language=koreana',
    }
    detail_req = requests.get(detail_url, headers=custom_headers)

    if detail_req.status_code == requests.codes.ok:
        app_id = app
        app_name = detail_req.json()[app]['data']['name']

        app_image = detail_req.json()[app]['data']['header_image']

        price_overview = detail_req.json()[app]['data'].get('price_overview', None)

        if price_overview is not None:
            app_dc_per = detail_req.json()[app]['data']['price_overview']['discount_percent']
            app_init_price = detail_req.json()[app]['data']['price_overview']['initial_formatted']
            app_final_price = detail_req.json()[app]['data']['price_overview']['final_formatted']

        else:
            app_dc_per = 0
            app_init_price = ""
            app_final_price = ""

        app_developers = detail_req.json()[app]['data']['developers']

        app_release_date = detail_req.json()[app]['data']['release_date']

        app_supported_languages = detail_req.json()[app]['data']['supported_languages']

        ad = ''
        for i in app_developers:
            ad += i + ','

        app_dev = ad.rstrip(",")

        app_publishers = detail_req.json()[app]['data']['publishers']

        ap = ''
        for i in app_publishers:
            ap += i + ','

        app_pub = ap.rstrip(",")

        app_genres = detail_req.json()[app]['data']['genres']

        ag = ''
        for i in app_genres:
            ag += i['description'] + ','

        app_gen = ag.rstrip(",")

        if app_release_date['coming_soon']:
            app_re_date = app_release_date['date'] + "(출시예정)"

        else:
            app_re_date = app_release_date['date']

        try:
            sl_list = app_supported_languages.replace("<strong>", "").replace("</strong>", "").split("<br>")
            app_sl = sl_list[0] + "(" + sl_list[1] + ")"
        except:
            app_sl = app_supported_languages.replace("<strong>", "").replace("</strong>", "")

        print(app_name)
        print(app_image)
        print(app_dc_per)
        print(app_init_price)
        print(app_final_price)
        print(app_dev)
        print(app_pub)
        print(app_gen)
        print(app_re_date)
        print(app_sl)

    else:
        print("steam app data disconnect")

if __name__ == "__main__":
    steam_app_data('905340')