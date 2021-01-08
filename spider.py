import requests
import csv
import json

headers = {
    'Cookie': '_T_WM=53629218447; XSRF-TOKEN=db4d17; WEIBOCN_FROM=1110006030; MLOGIN=0; M_WEIBOCN_PARAMS=fid%3D100103type%253D1%2526q%253D%2525E4%2525B8%252581%2525E7%25259C%25259F%26uicode%3D10000011',
    'Referer': 'https://m.weibo.cn/detail/4312409864846621',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    'X-Requested-With': 'XMLHttpRequest'
}
urls =[]
def getHostUrls():
    # #丁真#
    urls.append("https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E4%B8%81%E7%9C%9F%23&page_type=searchall")
    # #丁真的世界#
    urls.append("https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E4%B8%81%E7%9C%9F%E7%9A%84%E4%B8%96%E7%95%8C%23&page_type=searchall")
    # "#丁真说不要再p了#
    urls.append("https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E4%B8%81%E7%9C%9F%23&page_type=searchall")
    # #四川为了丁真有多努力#
    urls.append("https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E5%9B%9B%E5%B7%9D%E4%B8%BA%E4%BA%86%E4%B8%81%E7%9C%9F%E6%9C%89%E5%A4%9A%E5%8A%AA%E5%8A%9B%23&page_type=searchall")
    # "#丁真所在国企负责人回应拒绝选秀#"
    urls.append("https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E4%B8%81%E7%9C%9F%23&page_type=searchall")

def spider(page_num,hostUrl):
    # main_url为要爬取的主页地址
    if page_num:
        main_url = hostUrl + '&page=' + str(page_num)
    # 微博的分页机制是每页10条微博
    try:
        r = requests.get(url=main_url, headers=headers)
        r.raise_for_status()
    except Exception as e:
        print("爬取失败", e)
        return 0
    result_json = json.loads(r.content.decode('utf-8'))
    info_list = []
    for card in result_json['data']['cards']:
        info_list_sub = []
        if card.get("mblog"):
            info_list_sub.append(card['mblog']['attitudes_count'])  # 获赞数

            info_list_sub.append(card['mblog']['comments_count'])  # 评论数

            info_list_sub.append(card['mblog']['reposts_count'])    # 转发数


            if page_num == 1:
                info_list_sub.append(card['mblog']['created_at'])  # 发博时间
            elif '2018' not in card['mblog']['created_at']:
                info_list_sub.append(card['mblog']['created_at'])
            else:
                print("2019年微博爬取完毕")
                break

            info_list_sub.append(card['mblog']['weibo_position'])    # 是否原创

            if card['mblog'].get('raw_text'):
                info_list_sub.append(card['mblog']['raw_text'])   # 微博内容
            else:
                info_list_sub.append(card['mblog']['text'])

            # if card['mblog']['source'] == '':
            #     info_list_sub.append(None)
            # else:
            #     info_list_sub.append(card['mblog']['source'])

            # time.sleep(random.randint(4, 6))  # 每爬取一条微博暂停4到6秒，防反爬

            info_list.append(info_list_sub)
        else:
            continue
    return info_list


def save_csv(infolist):
    with open('weibo.csv', 'a+', encoding='utf_8_sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(infolist)


def main(num):
    for hostUrl in urls:
        for i in range(1, num+1):
            information = spider(i,hostUrl)
            save_csv(information)
            print("第%s页爬取完毕" % i)

print("### 开始爬取微博 ")
# 1、封装地址到urls中
getHostUrls()
# 2、遍历封装好的urls，循环查询接口，获取评论数
if __name__ == '__main__':
    main(10)