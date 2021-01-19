from Statistikalangas.Website import *


def to_r_without_s(htmlcode):
    r_without_s = re.sub(r"\s+", "", htmlcode.text)
    return r_without_s


def to_results_link(rg_link):
    results_link = rg_link.findall(to_r_without_s(htmlcode))
    return results_link
