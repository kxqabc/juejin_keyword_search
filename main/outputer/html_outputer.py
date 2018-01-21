class HtmlOutputer(object):

    def __init__(self):
        self.datas = []     # 輸入結果列表

    # 構建輸入數據(結果列表)
    def build_data(self, datas):
        if datas is None:
            print('Invalid data for output!')
            return None
        # 判断是应该追加还是覆盖
        if self.datas is None or len(self.datas)==0:
            self.datas = datas
        else:
            self.datas.extend(datas)

    # 输出html文件
    def output(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\">")
        fout.write("<link rel=\"stylesheet\" href=\"http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css\"> ")
        fout.write("<script src=\"http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js\"></script>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table class=\"table table-striped\" width=\"200\">")

        fout.write("<thead><tr><td><strong>文章</strong></td><td><strong>星数</strong></td></tr></thead>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td width=\"100\"><a href=\"%s\" target=\"_blank\">%s</a></td>" % (data.link, data.title))
            fout.write("<td width=\"100\">    %s</td>" % data.starCount)
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()