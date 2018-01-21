from bs4 import BeautifulSoup
from main.beans import result_bean


class HtmlParser(object):

    # 创建BeautifulSoup对象，将html结构化
    def build_soup(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        return self.soup

    # 根据获得的赞数过滤得到符合条件的tag
    def get_dom_by_star(self, baseline):
        doms = self.soup.find_all('span', class_='count')
        # 根据最少赞数过滤结果，只保留不小于baseline的节点
        for dom in doms:
            if int(dom.get_text()) < baseline:
                doms.remove(dom)
        return doms

    # 根据节点构建结果对象并添加到列表中
    def build_bean_from_html(self, baseline):
        doms = self.get_dom_by_star(baseline)
        if doms is None or len(doms)==0:
            print('doms is empty!')
            return None
        results = []
        for dom in doms:
            starCount = dom.get_text()      # 获得的赞数
            root = dom.find_parent('div', class_='info-box')    #这篇文章的节点
            a = root.find('a', class_='title', target='_blank') #包含了文章题目和链接的tag
            link = 'https://juejin.im' + a['href'] + '/detail'  #构造link
            title = a.get_text()
            results.append(result_bean.ResultBean(title, link, starCount))
            print(link, title, starCount)
        return results
