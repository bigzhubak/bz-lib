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


def getScriptHash(script):
    src = script.get('src')
    script_file = re.sub('\?v=.*', '', src)
    f = open('../' + script_file, 'r')
    script_content = f.read()
    hash = hashlib.sha224(script_content).hexdigest()
    f.close()
    print 'new hash=%s' % hash
    return hash

if __name__ == '__main__':
    # if len(sys.argv) == 2:
    #    file = int(sys.argv[1])
    #    soup = bs4.BeautifulSoup(self.request.text)
    # else:
    #    print 'run as:'
    #    print 'python update_js_version.py index.html'

    f = open('../index.html', 'rw')
    html = f.read()
    f.close()
    scripts = getScripts(html)
    f = open('../index.html', 'w')
    for script in scripts:
        hash = getScriptHash(script)
        html = re.sub('\?v=.*"', '?v=%s"'%hash, html)
        f.write(html)
    f.close()
