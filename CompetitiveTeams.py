import requests
import lxml.html as lh
import Helper
import pandas as pd
import numpy as np
import os
    
def main(pokemon):
    competitive_formats = ['ubers', 'dou', 'ou', 'uu', 'ru', 'nu']
    for i in range(len(competitive_formats)):
        url = 'https://www.pikalytics.com/pokedex/' + competitive_formats[i] + '/' + pokemon
        f = open('data/' + pokemon + '_' + competitive_formats[i] + '_teammates.txt', 'w', encoding='utf-8')
        page = requests.get(url)
        doc = lh.fromstring(page.content)
        tr_elements = doc.xpath('//div//a')
        for t in tr_elements:
            f.write(t.text_content())
        f.close()


if __name__ == '__main__':
    main('bulbasaur')