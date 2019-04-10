"""

	Team Members:
		Conner Joseph Brewster (UIN: 925004339)
		Duy Le (UIN: 125009667)
		Adam Morvant (UIN: 924004752)
	Date: Thursday, April 25th, 2019 at 12:00:00 PM Central Standard Time (Daylight Savings Time)
	Course: CSCE-470-500 - Information Storage and Retrieval
	Professor: Ruihong Huang
	
	QuickDex - Class Project
	Information retrieval program for Pokémon species data.
	
	Main.java - primary Java file.

"""
import requests, six
import lxml.html as lh
from itertools import cycle, islice
from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt

url = 'http://pokemondb.net/pokedex/all'

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

def form_dictionary(tr_elements, col):
	for j in range(1, len(tr_elements)):
		T = tr_elements[j]
		if len(T) != 10:
			break
		i = 0

		for t in T.iterchildren():
			data = t.text_content()
			if i > 0:
				try:
					data = int(data)
				except:
					pass
			col[i][1].append(data)
			i +=1

	poke_dict = {title:column for (title,column) in col}
	df = pd.DataFrame(poke_dict)
	df.head()
	print_full(df)

def print_col_names(tr_elements):
	col = []
	i = 0
	for t in tr_elements[0]:
		i += 1
		name = t.text_content()
		print('%d:"%s"'%(i,name))
		col.append((name,[]))

	form_dictionary(tr_elements, col)

# test function, mostly useless
def print_tr_length(tr_elements):

	[print(len(T)) for T in tr_elements[:12]]

# Main function.
def main():
	page = requests.get(url)
	doc = lh.fromstring(page.content)
	tr_elements = doc.xpath('//tr')

	#print_tr_length(tr_elements)
	print_col_names(tr_elements)

# Run program.
if __name__ == "__main__":
	main()
