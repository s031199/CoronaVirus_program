from Statistikalangas.Checker import *

informacija = []


def update_status():
    informacija.append({
        'Data': data,
        'Patvirtinti': patvirtinti_covid,
        'Sergantis': sergantis_covid,
        'Patvirtinti nauji': patvirtinti_nauji_covid,
        'Mire': mirusiu_covid,
        'Uzsikrete': uzsikretusiu_covid,
        'Pasveike': pasveikusiu_covid,
        'Izoliuoti': izoliuoti_covid,
        'Data iveztiniai': data_iveztiniai_covid,
        'Iveztiniai': iveztiniai_covid,
    })
    return informacija


# [('rugpjūčio17d.9val.', '2436', '637', '20', '81', '13', '1705', '3173', '154')]
for data, patvirtinti_covid, sergantis_covid, patvirtinti_nauji_covid, mirusiu_covid, uzsikretusiu_covid, pasveikusiu_covid, izoliuoti_covid, data_iveztiniai_covid, iveztiniai_covid in to_results_link(rg_link):
    update_status()
