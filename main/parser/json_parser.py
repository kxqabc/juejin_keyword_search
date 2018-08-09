#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from main.beans.result_bean import ResultBean
from main.exception.parse_error import ParseError


# 将json字符创解析为一个对象
def json_to_object(json_content):
    if json_content is None:
        print('parse error!json is None!')
        return None
    return json.loads(str(json_content))


# 从JSON构成的对象中提取出文章的title、link、collectionCount等数据，并将其封装成一个Bean对象，最后将这些对象添加到结果列表中
def build_bean_from_json(json_collection, baseline):
    if json_collection is None:
        raise ParseError('build bean from json error! json_collection is None!')
    list = json_collection['d'] # 文章的列表
    result_list = []    # 结果的列表
    if list is None or len(list) == 0:
        return []
    for element in list:
        starCount = element['collectionCount']  # 获得的收藏数，即获得的赞数
        if int(starCount) >= baseline:   # 如果收藏数不小于baseline，则构建结果对象并添加到结果列表中
            title = element['title']
            link = element['originalUrl']
            result = ResultBean(title, link, starCount)
            result_list.append(result)      # 添加到结果列表中
            print(title, link, starCount)
    return result_list
