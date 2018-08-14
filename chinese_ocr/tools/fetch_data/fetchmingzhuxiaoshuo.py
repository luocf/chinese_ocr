#!/usr/bin/python
# -*- coding: UTF-8 -*-

# coding: utf-8
import time
import urllib.request,sys,re

home_page_url = "http://www.mingzhuxiaoshuo.com/";
fetched_data_path = "../GenTextImageBlocks/myData/train_txt/"
def main():

    page_html = httpRequest(home_page_url);
    try:
        lines_re= re.compile(r'(?isu)<a class=awhite12 href="(.*?)" target="_self">(.*?)</a>')
        href_lines = re.findall(lines_re, page_html.decode('gb18030'))
        cf = open(fetched_data_path+"mingzhuxiaoshuo.txt", 'w')
        for line in href_lines:
            target_url = line[0]
            if "  ┊  " in target_url:
                continue
                #target_url = target_url.split("  ┊  ")[1].strip()
            title = str(line[1])
            cf.write(title+"\n")
            fetchTypeData(title, target_url)
    except Exception as e:
        print("解析错误 target_url：" + home_page_url, e)
    finally:
        cf.close()
def fetchTypeData(title, page_url):
    cf = open(fetched_data_path + title+".txt", 'w')
    try:
        page_html = httpRequest(page_url);
        lines_re = re.compile(r'(?isu)<td align=center><a class=atuhuang12 href="(.*?)" target=_blank title=(.*?)><font color="#006699">.*?</font></a></td>')
        page_html = page_html.decode('gb18030').lower()
        href_lines = re.findall(lines_re, page_html)
        for line in href_lines:
            target_url = home_page_url+line[0]
            title = str(line[1])
            cf.write(title + "\n")
            fetchSubPageData(title, target_url)
    except Exception as e:
        print("解析错误 target_url：" + page_html, e)
    finally:
        cf.close()


def fetchSubPageData(title, page_url):
    cf = open(fetched_data_path + title + ".txt", 'w')
    try:
        page_html = httpRequest(page_url);
        lines_re = re.compile(r'(?isu)<a class=white12.*?href="(.*?)"><font color="#ffffff">在线阅读</font></a>')
        page_html = page_html.decode('gb18030').lower()
        href_lines = re.findall(lines_re, page_html)
        for line in href_lines:
            target_url = home_page_url + line
            fetchPageData(cf, target_url)
    except Exception as e:
        print("解析错误 target_url：" + page_html, e)
    finally:
        cf.close()
def fetchPageData(cf, page_url):
    try:
        page_html = httpRequest(page_url);
        lines_re = re.compile(r'(?isu)<li><a href="(.*?)" target="_blank" title="(.*?)">(.*?)</a></li> ')
        page_html = page_html.decode('gb18030').lower()
        href_lines = re.findall(lines_re, page_html)
        for line in href_lines:
            target_url = home_page_url + line[0]
            title = str(line[1])
            cf.write(title + "\n")
            fetchData(cf, target_url)
    except Exception as e:
        print("解析错误 target_url：" + page_html, e)

def fetchData(cf, target_url):
    try:
        sub_page_html = httpRequest(target_url);
        sub_page_content = sub_page_html.decode('gb18030').lower()
        content_lines_re = re.compile(r'(?isu)<br />(.*?)<br />')
        contents_lines = re.findall(content_lines_re, sub_page_content)
        if len(contents_lines) == 0:
            content_lines_re = re.compile(r'(?isu)<span style="font-family:宋体;font-size:16px;background-color:#f5f8f8;">(.*?)</span>')
            contents_lines = re.findall(content_lines_re, sub_page_content)
        if len(contents_lines) == 0:
            content_lines_re = re.compile(r'(?isu)<div class="spctrl"></div>>(.*?)</<div class="spctrl"></div>')
            contents_lines = re.findall(content_lines_re, sub_page_content)
        if len(contents_lines) == 0:
            content_lines_re = re.compile(r'(?isu)<p>(.*?)</p>')
            contents_lines = re.findall(content_lines_re, sub_page_content)
        #contents_lines = sub_page_content.split('\n')
        for line in contents_lines:
            print(line);
            line = line.replace('&nbsp;', "").strip()
            if (len(line) < 2):
                continue
            semicolon_lines = line.split(";")
            for  semicolon_line in semicolon_lines:
                if (len( semicolon_line) < 2):
                    continue
                full_point_lines = semicolon_line.split("。")
                for full_point_line in full_point_lines:
                    comma_lines = full_point_line.split("，")
                    for comma_line in comma_lines:
                        if (len(comma_line) < 2):
                            continue
                        cf.writelines(comma_line+"\n");
            #sub_line_num = int(len(line) / 256)
            #for i in range(sub_line_num):
            #    contents = line[i*256:i*256+256]

    except Exception as e:
        print(e)
def httpRequest(target_url):
    content = urllib.request.urlopen(target_url, None,10).read()
    print(target_url)
    return content
main()

