import requests

class AppInfo:
    def __init__(self, id=None, name=None, image=None, price=None):
        self.id = id
        self.name = name
        self.image = image
        self.price = price
        self.link = "https://store.steampowered.com/app/" + id

def search_steamapps(app):
    req = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v1')

    if req.status_code == requests.codes.ok:
        print("connect")

        json_data = req.json()['applist']['apps']['app']

        # print(json_data)

        li = []

        num = len(json_data)

        for idx in range(0, num-1):
            # print(json_data[idx]['appid'])
            li.append(json_data[idx]['appid'])

        # test = 457841

        # if str(test) == app:
        #     print("yes!!")
        #
        # else:
        #     print("달라요")
        # print(li)
        # print("app="+ app)

        if int(app) in li:
            url = "https://store.steampowered.com/api/appdetails?appids=" + app
            detail_req = requests.get(url)

            # print(detail_req.json())
            # print(detail_req.json()[str(app)]['data']['name'])
            # print(detail_req.json()[str(app)]['data']['header_image'])
            app_id = app
            app_name = detail_req.json()[app]['data']['name']
            app_image = detail_req.json()[app]['data']['header_image']
            try:
                # print(detail_req.json()[str(app)]['data']['price_overview']['final_formatted'])
                app_price = detail_req.json()[app]['data']['price_overview']['final_formatted']
            except:
                # print(detail_req.json()[app]['data']['is_free'])
                if detail_req.json()[app]['data']['is_free'] == True:
                    app_price = "무료"
                else:
                    app_price = ""

            app_info = AppInfo(app_id, app_name, app_image, app_price)
        else:
            app_info = AppInfo()

        return app_info

    else:
        print("disconnect")
# data = req.text
# data.count('appid')
# json_data = req.json()['applist']['apps']
#
# print(req.text.count('appid'))
# f = open('/home/jinwook/steamapps/steamapps.txt', 'w')
#
# a = req.text.count('appid')
# sa_list = []
# for i in range(0, 50):
#     sa_list.append(json_data[i])
# print(len(sa_list))
# f.write(str(sa_list))
# f.close()

# name_data = json_data['appid'].name
# print(data)
# print(json_data)
# print(data.count('appid'))