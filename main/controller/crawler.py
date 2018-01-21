from main.downloader import downloader
from main.parser import html_parser, json_parser


# 爬取一页信息
def craw_one_page(func):
    def in_craw_one_page(new_url, baseline=10):    # 默认baseline=10
        print('begin to main..')

        content = downloader.download_json(new_url)  # 根据URL获取网页
        datas = func(content, baseline)     # 一次解析所得的结果

        print('main end..')
        return datas
    return in_craw_one_page


def parse_from_json(content, baseline):
    json_collection = json_parser.json_to_object(content)
    results = json_parser.build_bean_from_json(json_collection, baseline)
    return results


def parse_from_html(content, baseline):
    html_parser.build_soup(content)  # 使用BeautifulSoup将html网页构建成soup树
    results = html_parser.build_bean_from_html(baseline)
    return results



