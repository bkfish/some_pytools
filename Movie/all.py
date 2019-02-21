import requests
import re
from bs4 import BeautifulSoup
import os
import urllib
base_url='{{要爬的网页的base}}'
start_str = '目标链接的开头'
end_str = '.mp4' #目标链接的结尾
#32168-32857 构造要爬的url
for num in range(32857,32168,-1):
    URL=base_url+str(num)+".html"
    print("Now dowing:"+URL)
    r=requests.get(URL)
    string=r.text
    url_list = []
    record_position = 0
    while record_position < len(string):
        # 遍历整个字符串 #截取完一次之后让下个字符串出现
        start_index = string.find(start_str, record_position)
        # print('--------------', start_index)
        #调用字符串的find方法的时候，若出现错误，则返回的值为-1.
        if start_index == -1:
            # 没有匹配结果
            break
        #end_str是要截取的字符串，start_index是开始截取的位置，返回的是字符串的位置的索引。
        #从href="这个字符串得起始索引位置往后查找.com
        end_index = string.find(end_str, start_index)
        # print('********', end_index)
        # 开始截取
        url = string[start_index+len(start_str):end_index+len(end_str)]
        # 修改record_position得值，用于下一次循环。
        #实质是让每次截取的都不在
        #是第一个字符串，如果不通过这种方式，则会导致下次截取的还是第一个字符串。
        record_position = end_index
        #把截取的字符串追加到列表中。
        url_list.append(url)
    if len(url_list)==0:
        print("don's find"+str(num))
        continue
    mp4_url=start_str+url_list[0]
    file = str(num)+".mp4"
    print("downloading with " + file)
    LocalPath = os.path.join('/Movies',file)  #设置下载目录
    urllib.request.urlretrieve(mp4_url,LocalPath)
    print("success download :" + file)

