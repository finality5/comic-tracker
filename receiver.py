import requests
import time

f = open("subscribe.txt")
comic_list = f.read().split('\n')[:-1]
f.close()
for url in comic_list:
    try:
        time.sleep(1)
        res = requests.get(url).text
        raw_res = res.split('<a class="lst"')
        raw_last_chap = raw_res[1].split('\n')[0].split('"')
        print(raw_last_chap[3])
        print(raw_last_chap[1])
        print(raw_res[1].split('\n')[3].split('"')[3])
        print()
    except:
        print("Error . . Invalid link? No internet connection?")

    