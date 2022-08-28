import orodja
import re

indeksi_po_letih = [57, 5, 8, 8, 8, 9, 11, 12, 11, 13, 11, 12, 12, 13, 15, 14, 22,
18, 21, 28, 31, 36, 36, 34, 40, 36, 36, 36, 32, 31, 41, 53, 62, 57, 67, 62, 82, 
102, 113, 106, 109, 99, 105, 131, 140, 140, 165, 173, 172, 189, 188, 184, 197, 118]

for i in range(len(indeksi_po_letih)):
    leto = 1969 + i
    for j in range(indeksi_po_letih[i]):
        indeks = 30 * j
        link = f"http://www.go4go.net/go/games/bydate/{leto}/{indeks}"
        datoteka = f"podatki\{leto}\{j}.html"
        orodja.shrani_spletno_stran(link, datoteka)

orodja.shrani_spletno_stran("https://www.go4go.net/go/games/byplayer", "podatki\igralci_po_narodnosti.html")

vzorec_bloka_igre = re.compile(
    r'<td colspan="6"><img src="/images/whiteball.gif">.*?<img src="/images/printer.gif"></a></td>',
    flags = re.DOTALL)

vzorec_igre = re.compile(
    r'&nbsp;&nbsp;\[(?P<leto>.*?)\-(?P<mesec>.*?)\-(?P<dan>.*?)\]&nbsp;'
    r'&nbsp;(?P<turnir>.*?)\n.*?</td>.*?'
    r'<td style="text-align:center;"><?b?>?(?P<igralec_crni>[\-a-zA-Z\s]*)(?P<igralec_crni_rang>[1-9]?).*?</td>.*?'
    r'<td style="text-align:center;"><?b?>?(?P<igralec_beli>[\-a-zA-Z\s]*)(?P<igralec_beli_rang>[1-9]?).*?</td>.*?'
    r'<td style="text-align:center;">(?P<zmagovalec>\w*)\+?(?P<tip_zmage>.*?)</td>',
    flags = re.DOTALL)

vzorec_bloka_narodnosti = re.compile(
    r'<select name="p" size="6" style="width:200px; font-size:87.5%; font-family:serif; margin:10px;">.*?<input type="submit" value="Search">',
    flags = re.DOTALL)
    
vzorec_igralca = re.compile(
    r'<option value=".*?">(?P<igralec>.*?)\s\(.*?\)')

igre = []
for i in range(len(indeksi_po_letih)):
    leto = str(1969 + i)
    for j in range(indeksi_po_letih[i]):
        stran = orodja.vsebina_datoteke("podatki/" + leto + "/" + str(j) + ".html")
        for blok in vzorec_bloka_igre.finditer(stran):
            igre.append(vzorec_igre.search(blok.group(0)).groupdict())

igralci_po_narodnosti = []
stran = orodja.vsebina_datoteke("podatki/igralci_po_narodnosti.html")
for blok in vzorec_bloka_narodnosti.findall(stran):
    igralci_po_narodnosti.append(vzorec_igralca.findall(blok))

dict_igralci_po_narodnosti = []
drzave = ["Kitajska", "Koreja", "Japonska", "Tajvan", "Ostali", "AI"]
for i in range(len(igralci_po_narodnosti)):
    for igralec in igralci_po_narodnosti[i]:
        dict_igralci_po_narodnosti.append({"Drzava" : drzave[i], "Igralec" : igralec})

orodja.zapisi_csv(igre, 
["leto", "mesec", "dan", "turnir",
"igralec_crni", "igralec_crni_rang", "igralec_beli",
"igralec_beli_rang", "zmagovalec", "tip_zmage"], 
"podatki_iz_turnirjev.csv")

orodja.zapisi_csv(dict_igralci_po_narodnosti, 
["Drzava", "Igralec"], 
"podatki_o_narodnosti.csv")