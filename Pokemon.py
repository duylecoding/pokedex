import requests
import lxml.html as lh
import Helper
import pandas as pd
import numpy as np
import os

#1:"Lv."
#2:"Move"
#3:"Type"
#4:"Cat."
#5:"Power"
#6:"Acc."

directory = 'data'

def print_col_names(tr_elements, pokemon):
    col = []
    i = 0
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        #print('%d:"%s"' % (i, name))
        col.append((name, []))
    form_dictionary(tr_elements, col, pokemon)

def form_dictionary(tr_elements, col, pokemon):
    for j in range(1, len(tr_elements)):
        T = tr_elements[j]
        if len(T) != 6:
            break
        i = 0
        for t in T.iterchildren():
            data = t.text_content()
            if i > 0:
                try:
                    data = int(data)
                except Exception as e:
                    pass
            col[i][1].append(data)
            i += 1

    poke_dict = {title: column for (title, column) in col}
    df = pd.DataFrame(poke_dict)

    #Helper.print_full(df)
    df.head()
    path = directory + '/' + pokemon + '_moveset.csv'
    df.to_csv(path)
    
def main(pokemon):
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = 'https://pokemondb.net/pokedex/' + pokemon + '/moves/7'
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    print_col_names(tr_elements, pokemon)

if __name__ == '__main__':
    main('bulbasaur')