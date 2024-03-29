#! /usr/bin/python
# -*- coding: utf-8 -*-	

import re

# Regularis kifejezesek

print re.findall("a.", "almafa") #iterálható strukturát hoz létre, amire lehet csinálni for-t, for nem az elmeken megy végig
# ['al', 'af']

it = re.finditer("a.", "almafa") #visszaadja az illeszkedő objektumokat is
for m in it:
    print m.span()
# (0, 2)
# (3, 5)

print re.split("a.","almafaalatt")
# ['', 'm', '', 'l', 't']

print re.split("(a.)","almafaalatt")
# ['', 'al', 'm', 'af', '', 'aa', 'l', 'at', 't']

print re.split("(a.)","almafaalatt",2)
# ['', 'al', 'm', 'af', 'aalatt']

print re.split("(a.)","kortefa")
# ['kortefa']

print re.sub(".at.", "@", "xy_at_elte.hu, wz<at>elte.hu")
# xy@elte.hu, wz@elte.hu

print re.sub(".at.", "@", "xy_at_elte.hu, wz<at>elte.hu", 1)
# xy@elte.hu, wz<at>elte.hu

print re.subn(".at.", "@", "xy_at_elte.hu, wz<at>elte.hu") #ha tudni akarom hány csere volt
# ('xy@elte.hu, wz@elte.hu', 2)