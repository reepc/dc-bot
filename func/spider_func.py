import requests as req
import random as ran
import json
from requests import HTTPError

with open("./json/setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


def catch_pic(keyword=None, random=False, id=None) -> str:
    session = req.session()

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "refer": "https://www.pixiv.com/",
        "PHPSESSID": jdata["PHPSESSID"],
    }

    global false, null, true
    false = "False"
    null = "None"
    true = "True"

    def rn():
        return ran.randint(1000000, 200000000)

    try:
        final = rn() if random else keyword
        if not random:
            if id is not None:
                pic_url = f"https://www.pixiv.net/artworks/{id}"
                embed_url = f"https://www.pixiv.cat/{id}.jpg"
            else:
                print(keyword)
                url = f"https://www.pixiv.net/ajax/search/artworks/{keyword}"
                print(url)
                response = session.get(url, headers=headers)
                content = eval(response.content)["body"]["illustManga"]["data"]
                print(content)
                datas = content
                pic_id = []

                for data in datas:
                    if "id" in data:
                        pic_id.append(data["id"])

                final = ran.choice(pic_id)
                pic_id.clear()
                pic_url = f"https://www.pixiv.net/artworks/{final}"
                response = req.get(pic_url)
                while response.status_code != 200:
                    final = rn()
                    pic_url = f"https://www.pixiv.net/artworks/{final}"
                    response = req.get(pic_url)

                embed_url = f"https://pixiv.cat/{final}.jpg"

        return pic_url, embed_url
    except HTTPError as error:
        raise error


if __name__ == "__main__":

    def random_test():
        print(catch_pic(random=True))

    def keyword_test():
        print(catch_pic(keyword=str(input("enter your keyword:"))))

    choose = int(input("0 or 1:"))
    if choose:
        keyword_test()
    else:
        random_test(random=True)
