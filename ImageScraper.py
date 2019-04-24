import cv2
import numpy as np
import urllib.request
import time


def download_pokemon_images(pokemonid):
    try:
        #for i in range(1, 810):
        url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'+'{:03d}'.format(pokemonid)+'.png'
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        bin_str = response.read()
        byte_arr = bytearray(bin_str)
        np_arr = np.array(byte_arr, dtype='uint8')
        image = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("data/"+'{:04d}'.format(pokemonid)+'.png', image)
        print("Saved: ", url)
    except Exception as e:
        print(str(e))