import requests
import json
from steam_api_key import my_key
import os
from config.settings import BASE_DIR
import pickle


def steam_app_data():
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + my_key

    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        print("steam app data connect")

        json_data = json.loads(req.text)

        app_data = json_data['applist']['apps']

        app_num = len(app_data)
        print(app_num)

        app_id_list = []
        app_name_list = []

        for idx in range(0, app_num-1):
            app_id_list.append(app_data[idx]['appid'])
            app_name_list.append(app_data[idx]['name'])

        print(app_id_list)
        print(app_name_list)

        app_id_text_file = open(os.path.join(BASE_DIR, 'static/crawling_data/steam_app_id_data.txt'), 'wb')
        app_name_text_file = open(os.path.join(BASE_DIR, 'static/crawling_data/steam_app_name_data.txt'), 'wb')

        pickle.dump(app_id_list, app_id_text_file)
        pickle.dump(app_name_list, app_name_text_file)
        app_id_text_file.close()
        app_name_text_file.close()

    else:
        print("steam app data disconnect")

if __name__ == "__main__":
    steam_app_data()

    # f = open(os.path.join(BASE_DIR, 'static/crawling_data/steam_app_id_data.txt'), 'rb')
    # d = pickle.load(f)
    # print(type(d))
    # print(d)
    #
    # g = open(os.path.join(BASE_DIR, 'static/crawling_data/steam_app_name_data.txt'), 'rb')
    # e = pickle.load(g)
    # print(type(e))
    # print(e)