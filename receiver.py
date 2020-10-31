import requests
import time
import datetime

f = open("subscribe.txt")
comic_list = f.read().split('\n')[:-1]
f.close()
ans = []
for url in comic_list:
    try:
        tmp = {}
        time.sleep(1)
        res = requests.get(url).text
        raw_res = res.split('<a class="lst"')
        raw_last_chap = raw_res[1].split('\n')[0].split('"')
        date_string = raw_res[1].split('\n')[3].split('"')[3]
        date_string = date_string.split(' ')
        date_string = datetime.datetime.strptime(" ".join(date_string[-3:]), "%b %d, %Y")
        tmp['name'] = raw_last_chap[3]
        tmp['link'] = raw_last_chap[1]
        tmp['published'] = date_string
        print('.')
        ans.append(tmp)
    except KeyboardInterrupt:
        print("Exit by user")
        break
    except:
        print("Error . . Invalid link? No internet connection?")
print()
ans = sorted(ans, key = lambda i: i['published'])
for r in ans:
    print(r['name'])
    print(r['link'])
    print(r['published'].strftime("%d/%m/%Y"))
    print()
