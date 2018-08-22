#!/usr/bin/python2.7 
#-*- encoding: utf-8 -*- 
"""
# 作者: vincent
# 时间: 2017-7-11
# 文件: transword.py

"""
import os
import sys
import urllib2
import urllib
import json
import argparse
import datetime
import platform
from argparse import RawTextHelpFormatter

reload(sys)
sys.setdefaultencoding('utf-8')


# 查询函数
def queryTranslate(queryStr):
    youdao_url_json ="http://fanyi.youdao.com/openapi.do?keyfrom=" \
            +"mlovez-dev&key=1341364669&type=data&doctype=json&version=1.1&"

    resultJson ="" 
    try:
        response =urllib2.urlopen(youdao_url_json \
                +urllib.urlencode({'q':queryStr}))
        resultJson =response.read()

    except Exception, e:
        print "--> Exception catched :"
        print e

    return resultJson
    

# 主函数
def main(words) :
    KEY_ERRORCODE ='errorCode'
    KEY_BASIC ='basic'
    KEY_PHONETIC ='phonetic'
    KEY_EXPLAINS ='explains'
    KEY_TRANSLATION ='translation' 
    wordsxml =''
    wordsphonetic =''
    wordexplaining =''
    path =os.path.expandvars('$HOME')
    filename ='mywords'
#    print "查询：\n    " +words
    jsonObj =json.loads(queryTranslate(words))
    wordsxml =words
    if jsonObj !=None and jsonObj.has_key(KEY_ERRORCODE) \
            and jsonObj[KEY_ERRORCODE] ==0 :
        if jsonObj.has_key(KEY_BASIC) :
            if jsonObj[KEY_BASIC].has_key(KEY_PHONETIC) :
                wordsphonetic =jsonObj[KEY_BASIC][KEY_PHONETIC]
            if jsonObj[KEY_BASIC].has_key(KEY_EXPLAINS) :
                for v in jsonObj[KEY_BASIC][KEY_EXPLAINS] :
                    wordexplaining =wordexplaining+v
     
        #单词写入本地文件
        choices ="y"
        if choices in ['y','Y']:
          filepath = r'%s/ydword/%s.xml' %(path,filename)
          if (platform.system()).lower() == 'windows':
            filepath = r'E:\pyword\%s.xml' %filename
          fp = open(filepath,'a+')
          file = fp.readlines()
          fp.write(u"""  <item>\n  <word>%s</word>\n  <trans><![CDATA[%s]]></trans>\n  <phonetic><![CDATA[[%s]]]></phonetic>\n  <tags>%s</tags>\n  <progress>1</progress>\n  </item>\n\n""" %(wordsxml,wordexplaining,wordsphonetic,filename))
          fp.close()
    else :
        print words
        print u"没有相应的翻译 ..."


if __name__ == "__main__" :
    # 命令行参数解释器
    helpStr =u"要翻译的英文或中文，如果有空格或标点请加引号\n" \
            +u"（因为Bash对于末尾感叹号处理缺陷原因，当末尾\n" \
            +u"有感叹号时最好用单引号）"
    descStr =u"一个简单的命令行翻译程序"
    parser =argparse.ArgumentParser(description=descStr, \
                formatter_class=RawTextHelpFormatter)
    parser.add_argument("words", action="store", help=helpStr)
    args =parser.parse_args()
    # main() 函数
    main(args.words)
    exit(0)


