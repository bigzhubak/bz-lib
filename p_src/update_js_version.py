#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bs4
import re
import hashlib


def getScripts(html):
    soup = bs4.BeautifulSoup(html)
    reg = re.compile("\?v=", re.I)
    scripts = soup.find_all('script', {'src': reg})
    return scripts


def getScripthash(script):
    src = script.get('src')
    script_file = re.sub('\?v=.*', '', src)
    f = open('../' + script_file, 'r')
    script_content = f.read()
    hash = hashlib.sha224(script_content).hexdigest()
    f.close()
    return hash

if __name__ == '__main__':
    # if len(sys.argv) == 2:
    #    file = int(sys.argv[1])
    #    soup = bs4.BeautifulSoup(self.request.text)
    # else:
    #    print 'run as:'
    #    print 'python update_js_version.py index.html'

    f = open('../index.html', 'r')
    html = f.read()
    f.close()
    scripts = getScripts(html)
    for script in scripts:
        hash = getScripthash(script)
        print hash
