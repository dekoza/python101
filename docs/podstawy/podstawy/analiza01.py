#! /usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul32 import czytaj, zapisz
import time

# ustawienia
ileliczb = 5
maksliczba = 20
ilerazy = 20
nazwapliku = "automat.json"

losowania = czytaj(nazwapliku)
    
iletrafien = 0
for i, slownik in enumerate(losowania):
    print i,"->",slownik
    ileliczb = len(slownik['wylosowane'])
    for k, w in slownik.iteritems():
        print k,"->",w
    iletrafien = iletrafien + slownik['ile']

srednio = float(iletrafien)/float(len(losowania))
procent = srednio/float(ileliczb)*100
print "{0:2.2f} -> {1:3.2f}%".format(srednio, procent)
