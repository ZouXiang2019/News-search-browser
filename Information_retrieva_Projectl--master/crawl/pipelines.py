# -*- coding: gbk -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import os


class netease_spiderPipeline(object):
    def __init__(self):
        self.current_dir = os.getcwd()
    #
    # web_id = 1
    # def process_item(self, item, spider):
    #     dir_path = os.path.join(self.current_dir, 'news', item['source'], item['date'].replace('/', '-'))
    #     if not os.path.exists(dir_path):
    #         os.makedirs(dir_path)
    #     news_file_path = os.path.join(dir_path, item['newsId'] + '.txt')
    #     # news_file_path1 = os.path.join(dir_path, item['newsId'] + '.txt')
    #     if os.path.exists(news_file_path) and os.path.isfile(news_file_path):
    #         print('---------------------------------------')
    #         print(item['newsId'] + '.json exists, not overriden')
    #         print('---------------------------------------')
    #         return item
    #
    #     news_file = open(news_file_path, 'w')
    #     # news_file_path1 = codecs.open(news_file_path1, 'w', 'gbk')
    #     # line = json.dumps(dict(item), ensure_ascii=False)
    #     # line2 = json.dumps(dict(item['title']), ensure_ascii=False)
    #
    #     for i in range(len('title')):
    #         news_file.write(str(self.web_id) + '#####' + item['title'][i] + '#####' + item['contents'] + '#####' + '#####' + item['url'] + '#####')
    #
    #     # news_file.write(item['time']+ '/' + item['date'])
    #     news_file.close()
        # news_file.write(line2)
        # news_file.close()
        # link_url = item['url']
        # file_name = 'netease_data.txt'
        #
        # fp = open(item['path'] + '/' + file_name, 'w')
        # fp.write(item['content'])
        # fp.close()
        # return item
