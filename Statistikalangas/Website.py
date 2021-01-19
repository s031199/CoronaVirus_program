import re
from requests_html import HTMLSession

session = HTMLSession()
htmlcode = session.get('https://nvsc.lrv.lt/lt/visuomenei/nacionalinio-visuomenes-sveikatos-centro-duomenys')
rg_link = re.compile('<p><strong>Nacionaliniovisuomenėssveikatoscentro......(.*?)duomenimis:</strong></p><ul><li>Patvirtintųligosatvejųskaičiuskonkretiemsžmonėms:<strong>(.*?)</strong></li><li>Sergančiųžmoniųskaičius:<strong>(.*?)</strong></li><li>PervakardienąpatvirtintųnaujųCOVID-19susirgusiųžmoniųskaičius:<strong>(.*?)</strong></li><li>Mirusiųnuokoronavirusožmoniųskaičius:<strong>(.*?)</strong></li><li>Užsikrėtusiejikoronavirusu,mirędėlkitųpriežasčių:<strong>(.*?)</strong></li><li>Pasveikusiųžmoniųskaičius:<strong>(.*?)</strong></li><li>Izoliacijojeesančiųasmenųskaičius.sergančių,sąlytįturėjusių,išpaveiktųteritorijųatvykusių,kuriemsišduotisprendimaiaktualiu14dienųlaikotarpiu.:<strong>(.*?)</strong></li></ul><p>Nuo(.*?)įvežtiniųatvejų:<strong>(.*?)</strong></p>')







