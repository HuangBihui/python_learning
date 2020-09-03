#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests
import os
import sys
import unicodedata
from bs4 import BeautifulSoup
import lxml

'''
DOWNLOAD_DIR = os.path.join(os.getcwd(), "songs_dir")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
}
'''

def validate_file_name(filename):
    # trans chinese punctuation to english
    filename = unicodedata.normalize('NFKC', filename)
    filename = filename.replace('/', "%2F").replace('\"', "%22")
    rstr = r"[\/\\\:\*\?\"\<\>\|\+\-:;',=.?@]"
    # Replace the reserved characters in the file name to '-'
    rstr = r"[\/\\\:\*\?\"\<\>\|\+\-:;=?@]"  # '/ \ : * ? " < > |'
    return re.sub(rstr, "_", filename)


def main():
    download_dir = os.path.join(os.getcwd(), "download_dir")
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

        
    url = "http://pages.cs.wisc.edu/~remzi/OSTEP/"
    response = requests.get(url)
    html = BeautifulSoup(response.text,features="lxml")
    book_list=html.findAll('table')
    book = book_list[4]

    for tr in book.findAll('tr'):
        for td in tr.findAll('td'):
            a = td.find('a')
            if a:
                durl=url+a.get('href')
                filename = "{0}".format(validate_file_name(td.getText()+a.get('href')))
                filepath=os.path.join(download_dir, filename)
                r = requests.get(durl)
                with open(filepath, "wb") as f:
                    f.write(r.content)


if __name__ == "__main__":
    main()

    

