from __future__ import print_function
import colorsys
import binascii
import struct, shutil
from PIL import Image
import numpy as np
import scipy, os
import scipy.misc
import scipy.cluster


NUM_CLUSTERS =10
input_base_path = '/Users/chethankarur/Pictures/chethankarur.com/img/nature/'
output_base_path = '/Users/chethankarur/Documents/StockTest/'

def get_color_code(image_path):
	im = Image.open(image_path)
	im = im.resize((150, 150))      # optional, to reduce time
	ar = np.asarray(im)
	shape = ar.shape
	ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

	codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

	vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
	counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

	index_max = scipy.argmax(counts)                    # find most frequent
	peak = codes[index_max]
	colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
	return(colour)

def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

def final_des(dict_codes_final):
	num_name = 1
	for i in dict_codes_final.keys():
		curr_filename = dict_codes_final[i]
		ip_filepath = input_base_path+curr_filename
		target_file_path = output_base_path+str(num_name)+'.webp'
		shutil.copy(ip_filepath, target_file_path)
		num_name+=1

#main
folders_list = os.listdir(input_base_path)
dict_codes = {}

for i in folders_list:
	try:
		ccode = get_color_code(input_base_path+i)
		if(ccode not in dict_codes.keys()):
			dict_codes[ccode]= i
		else:
			continue
	except:
		leave=1

color_list = list(dict_codes.keys())
color_list.sort(key=get_hsv)
color_list.reverse()

dict_codes_final = {}
for i in color_list:
	dict_codes_final[i]=dict_codes[i]

final_des(dict_codes_final)