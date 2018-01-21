# 将每条文章保存为一个bean，其中包含：题目、链接、获得的赞数 属性
class ResultBean(object):
    def __init__(self, title, link, star_count=10):
        self.title = title
        self.link = link
        self.star_count = star_count
