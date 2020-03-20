import requests
import json
from termcolor import colored
import sys

#ufile = open(sys.argv[1], 'rb')
siteoption = True
while siteoption:
    try:
        cfg = json.loads(open("config.json", "r").read())
        opts = []
        counter = 1
        for i in cfg['sites']:
            if 'name' and 'url' in i:
                print(f"{colored(counter, 'green')}. {i['name']}")
                opts.append(i)
                counter += 1
            else:
                pass
        soption = int(input(f"Select which one to upload to ({colored(f'1-{counter - 1}', color='green')}) "))
        soption = opts[soption - 1]
        opts.clear()
        siteoption = False
        ctype = True
    except ValueError:
        print(colored(f"Make sure you put in a number which is between {colored(f'1-{counter}', color='green')}", "red"))
        continue
    except IndexError:
        print(colored(f"Please select a number between {colored(f'1-{counter}', color='green')}", "red"))
        continue

while ctype:
    try:
        print(f"{colored(1, 'green')}. Text\n{colored(2, 'green')}. Image\n{colored(3, 'green')}. Video\n{colored(4, 'green')}. Audio\n{colored(5, 'green')}. Application\n{colored(6, 'green')}. Multipart\n{colored(7, 'green')}. vnd")
        ctypes = int(input(f"Select content type ({colored('1-7', 'green')}) "))
        if ctypes == 1:
            json.loads(open('config.json', 'r').read())['content-types']['text']
        elif ctypes == 2:
            json.loads(open('config.json', 'r').read())['content-types']['image']
        elif ctypes == 3:
            json.loads(open('config.json', 'r').read())['content-types']['video']
        elif ctypes == 4:
            json.loads(open('config.json', 'r').read())['content-types']['audio']
        elif ctypes == 5:
            json.loads(open('config.json', 'r').read())['content-types']['application']
        elif ctypes == 6:
            json.loads(open('config.json', 'r').read())['content-types']['multipart']
        elif ctypes == 7:
            json.loads(open('config.json', 'r').read())['content-types']['vnd']
        else:
            raise IndexError("out of range")
    except IndexError:
        print(colored(f"Please select a number between {colored(f'1-7', color='green')}", "red"))
        continue


url = "https://support.cloudflare.com/api/v2/uploads.json?filename=xd"
headers = {"Content-Type": "image/png"}


req = requests.post(url, headers=headers, data=ufile)

res = json.loads(req.content)
print(colored('-----------------', 'green'))
print(f'Expires at {res["upload"]["expires_at"]}\nURL: {res["upload"]["attachments"][0]["mapped_content_url"]}')
