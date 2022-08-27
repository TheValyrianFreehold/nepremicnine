import os
import requests
import sys
import csv

indeksi_po_letih = [57, 5, 8, 8, 8, 9, 11, 12, 11, 13, 11, 12, 12, 13, 15, 14, 22,
18, 21, 28, 31, 36, 36, 34, 40, 36, 36, 36, 32, 31, 41, 53, 62, 57, 67, 62, 82, 
102, 113, 106, 109, 99, 105, 131, 140, 140, 165, 173, 172, 189, 188, 184, 197, 118]

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

def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        writer.writerows(slovarji)

for i in range(len(indeksi_po_letih)):
    leto = 1969 + i
    for j in range(indeksi_po_letih[i]):
        indeks = 30 * j
        link = f"http://www.go4go.net/go/games/bydate/{leto}/{indeks}"
        datoteka = f"podatki\{leto}\{j}.html"
        shrani_spletno_stran(link, datoteka)