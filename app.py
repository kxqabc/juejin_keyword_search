import os
from flask import Flask, jsonify, redirect, url_for, render_template, request
from main.controller import crawler
from main.exception.parameter_error import InvalidParameter
from urllib.parse import quote
from main.url import url_manager

app = Flask(__name__)

# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)

# 带爬取的url地址，不包含请求参数
ajax_base_url = 'https://search-merger-ms.juejin.im/v1/search'


# 根目录，返回输入截面
@app.route('/')
def index():
    return render_template('input.html')


# 搜索功能视图函数
@app.route('/search')
def search():
    try:
        baseline = int(request.args.get('baseline'))    # 从请求参数中获取文章赞同数的下限值
    except ValueError:
        raise InvalidParameter('输入框不能为空或者请不要在输入框第二栏中输入非数字字符!')
    keyword = quote(request.args.get('keyword'))  # 获取搜索的关键字, urllib.parse.quote() 复杂处理url中的中文
    if keyword is None or len(keyword) == 0:
        raise InvalidParameter('输入框不能为空!')

    params = {}  # 对应的请求参数
    params['query'] = keyword
    params['page'] = '0'
    params['raw_result'] = 'false'
    params['src'] = 'web'

    new_url = url_manager.build_ajax_url(ajax_base_url, params)     # 构建请求地址
    craw_json = crawler.craw_one_page(crawler.parse_from_json)      # 选择json解析器
    datas = craw_json(new_url, baseline)        # 进行下载、解析，获得结果
    if datas is None or len(datas) == 0:
        return

    return render_template('output.html', datas=datas, keyword=request.args.get('keyword'), baseline=baseline)  # keyword传原始值，否则next_page中再进行quote则会出错


# 请求获得更多数据
@app.route('/nextPage')
def next_page():
    keyword = quote(request.args.get('keyword'))  # 获取搜索的关键字, urllib.parse.quote() 复杂处理url中的中文
    try:
        baseline = int(request.args.get('baseline'))
        req_page = int(request.args.get('req_page'))
    except ValueError:
        return redirect(url_for('index'))
    if keyword is None or len(keyword) == 0:
        return redirect(url_for('index'))

    params = {}  # 对应的请求参数
    params['query'] = keyword
    params['page'] = str(req_page)
    params['raw_result'] = 'false'
    params['src'] = 'web'

    new_url = url_manager.build_ajax_url(ajax_base_url, params)     # 构建请求地址
    craw_json = crawler.craw_one_page(crawler.parse_from_json)      # 选择json解析器
    datas = craw_json(new_url, baseline)        # 进行下载、解析，获得结果
    # 将结果对象构成的列表转完成json数组
    json_array = []
    for data in datas:
        json_array.append(data.__dict__)

    return jsonify(json_array)


# 参数错误界面
@app.errorhandler(InvalidParameter)
def invalid_param(error):
    return render_template('param-error.html', error_message=error.message), error.status_code


if __name__ == '__main__':
    app.debug = True
    app.run()
