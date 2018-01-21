# 根据输入的base_url(基础地址)和params(参数字典)来构造一个新的url
# eg:https://search-merger-ms.juejin.im/v1/search?query=python&page=1&raw_result=false&src=web
# 参数中的start_page是访问的起始页数字，gap是访问的页数间隔
def build_ajax_url(base_url, params):
    if base_url is None:
        print('Invalid param base_url!')
        return None
    if params is None or len(params) == 0:
        print('Invalid param request_params!')
        return None
    equal_sign = '='    # 键值对内部连接符
    and_sign = '&'  # 键值对之间连接符
    # 将base_url和参数拼接成url放入集合中
    param_list = []
    for item in params.items():
        param_list.append(equal_sign.join(item))    # 字典中每个键值对中间用'='连接
    param_str = and_sign.join(param_list)       # 不同键值对之间用'&'连接
    new_url = base_url + '?' + param_str
    print('生产出新url：', new_url)
    return new_url


