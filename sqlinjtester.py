#! /usr/bin/env pyhton

import sys
import urllib
import urllib.request


hedef_url=input("Lütfen hedef url'yi giriniz: ")
istek=urllib.request.urlopen(hedef_url + "'1=1")
body=istek.read()
fbody=body.decode('utf-8')
if "You have an error in your SQL syntax" in fbody:
    print("Hedef sitede  SQL injection zaafiyeti var")
else:
    print("Hedef sitede zaafiyet bulunamadı")
