import os
import requests
import re
import sys

def pripravi_imenik(ime_datoteke):
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
    try:
        print(f'Shranjujem {url} ...', end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('Že shranjeno!')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('Shranjeno!')

def vsebina_datoteke(ime_datoteke):
    with open(ime_datoteke, encoding='utf-8') as datoteka:
        return datoteka.read()

for n in range(1, 31):
    link = f"https://www.nepremicnine.net/oglasi-prodaja/ljubljana-mesto/stanovanje/{n}/"
    datoteka = f"podatki\stanovanja-mesto\{n}.html"
    shrani_spletno_stran(link, datoteka)

for n in range(1, 11):
    link = f"https://www.nepremicnine.net/oglasi-prodaja/ljubljana-mesto/hisa/{n}/"
    datoteka = f"podatki\hise-mesto\{n}.html"
    shrani_spletno_stran(link, datoteka)

for n in range(1, 7):
    link = f"https://www.nepremicnine.net/oglasi-prodaja/ljubljana-okolica/stanovanje/{n}/"
    datoteka = f"podatki\stanovanja-okolica\{n}.html"
    shrani_spletno_stran(link, datoteka)

for n in range(1, 16):
    link = f"https://www.nepremicnine.net/oglasi-prodaja/ljubljana-okolica/hise/{n}/"
    datoteka = f"podatki\hise-okolica\{n}.html"
    shrani_spletno_stran(link, datoteka)

povezave = []
vzorec = r'<!--<meta itemprop="url" content="(?P<povezava>.*?)" />-->'
for filename in os.listdir("podatki\stanovanja-mesto"):
    if filename.endswith(".html"): 
        with open("podatki/stanovanja-mesto/" + filename, encoding='utf-8') as datoteka:
            stran = datoteka.read()
            pojavitve = re.findall(vzorec, stran)
            povezave.extend(pojavitve)
            
for povezava in povezave:
    n = povezave.index(povezava)
    ime_datoteke = f"podatki\stanovanja-mesto\posamezne\{n}.html"
    shrani_spletno_stran(povezava, ime_datoteke)

povezave = []
for filename in os.listdir("podatki\hise-mesto"):
    if filename.endswith(".html"): 
        with open("podatki/hise-mesto/" + filename, encoding='utf-8') as datoteka:
            stran = datoteka.read()
            pojavitve = re.findall(vzorec, stran)
            povezave.extend(pojavitve)
            
for povezava in povezave:
    n = povezave.index(povezava)
    ime_datoteke = f"podatki\hise-mesto\posamezne\{n}.html"
    shrani_spletno_stran(povezava, ime_datoteke)

povezave = []
for filename in os.listdir("podatki\stanovanja-okolica"):
    if filename.endswith(".html"): 
        with open("podatki/stanovanja-okolica/" + filename, encoding='utf-8') as datoteka:
            stran = datoteka.read()
            pojavitve = re.findall(vzorec, stran)
            povezave.extend(pojavitve)
            
for povezava in povezave:
    n = povezave.index(povezava)
    ime_datoteke = f"podatki\stanovanja-okolica\posamezne\{n}.html"
    shrani_spletno_stran(povezava, ime_datoteke)

povezave = []
for filename in os.listdir("podatki\hise-okolica"):
    if filename.endswith(".html"): 
        with open("podatki/hise-okolica/" + filename, encoding='utf-8') as datoteka:
            stran = datoteka.read()
            pojavitve = re.findall(vzorec, stran)
            povezave.extend(pojavitve)
            
for povezava in povezave:
    n = povezave.index(povezava)
    ime_datoteke = f"podatki\hise-okolica\posamezne\{n}.html"
    shrani_spletno_stran(povezava, ime_datoteke)
