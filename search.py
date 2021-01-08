import requests
import re
import time
def get_one_page(url):#请求函数：获取某一网页上的所有内容
    headers = {
        'User-agent' : 'your User-agent',
        'Host' : 'weibo.cn',
        'Accept' : 'application/json, text/plain, */*',
        'Accept-Language' : 'zh-CN,zh;q=0.9',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Cookie' : 'your Cookie!!!!',
        'DNT' : '1',
        'Connection' : 'keep-alive'
    }#请求头的书写，包括User-agent,Cookie等
    response = requests.get(url,headers = headers,verify=False)#利用requests.get命令获取网页html
    if response.status_code == 200:#状态为200即为爬取成功
        return response.text#返回值为html文档，传入到解析函数当中
    return None
def parse_one_page(html):#解析html并存入到文档result.txt中
    pattern = re.compile('<span class="ctt">.*?</span>', re.S)
    items = re.findall(pattern,html)
    result = str(items)
    with open('test.txt','a',encoding='utf-8') as fp:
        fp.write(result)

for i in range(28412):
    url = "https://weibo.cn/comment/HgCfidCUs?uid=1343887012&rl=0&oid=4345701393410667&page="+str(i)
    html = get_one_page(url)
    print(html)
    print('正在爬取第 %d 页评论' % (i+1))
    parse_one_page(html)
    time.sleep(3)