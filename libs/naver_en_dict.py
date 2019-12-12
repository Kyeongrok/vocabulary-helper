import requests
from bs4 import BeautifulSoup

map = {
    "cultivating":"",
    "gentelness":"",
    "outrage":"",
    "inflame":"",

}

def getMean(word):
    url = "https://endic.naver.com/search.nhn?sLn=en&query={}&searchOption=all&isOnlyViewEE=Y".format(word)
    pageString = requests.get(url).content

    bsobj = BeautifulSoup(pageString, "html.parser")
    aaa = bsobj.find("div", {"class":"word_num"})
    fnt_k05 = aaa.find("span", {"class":"fnt_k05"})
    return fnt_k05.text

