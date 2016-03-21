#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bs4
import re
import hashlib
import sys


def getScripts(html):
    soup = bs4.BeautifulSoup(html)
    reg = re.compile("\?vbz=", re.I)
    scripts = soup.find_all('script', {'src': reg})
    return scripts


def getScriptHash(script):
    src = script.get('src')
    script_file = re.sub('\?vbz=.*', '', src)
    f = open(script_file, 'r')
    script_content = f.read()
    hash = hashlib.sha224(script_content).hexdigest()
    f.close()
    print 'new hash=%s' % hash
    return hash


def main(file_path):
    f = open(file_path, 'rw')
    html = f.read()
    f.close()
    scripts = getScripts(html)
    f = open(file_path, 'w')
    for script in scripts:
        hash = getScriptHash(script)
        html = re.sub('\?vbz=.*"', '?vbz=%s"' % hash, html)
        f.write(html)
    f.close()
if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        main(file_path)
    else:
        print 'run as:'
        print 'python update_js_version.py index.html'
