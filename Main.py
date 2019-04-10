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

# Main function.
def main():
	page = requests.get(url)
	doc = lh.fromstring(page.content)
	tr_elements = doc.xpath('//tr')
	[print(len(T)) for T in tr_elements[:12]]

# Run program.
if __name__ == "__main__":
	main()
