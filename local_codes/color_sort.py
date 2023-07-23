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
output_base_path = input_base_path

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

def increase_hex_color(hex_code):
    # Remove the '#' symbol if present
    hex_code = hex_code.lstrip('#')
    print('CP1')
    
    # Convert the hex code to RGB values
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    print('CP2')

    # Increase each RGB component by one
    r = min(255, r + 1)
    g = min(255, g + 1)
    b = min(255, b + 1)
    print('CP3')
    
    # Convert the updated RGB values to hex format
    updated_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    print('updated the hex')
    
    return updated_hex


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

def force_add_photo(dict_codes,ccode,path):
	fixed = 0
	while(fixed!=1):
		if(ccode in dict_codes.keys()):
			ccode = increase_hex_color(ccode)
		else:
			dict_codes[ccode]= path
			fixed = 1
			print ('Force push sucessful')
	return dict_codes


#main
folders_list = os.listdir(input_base_path)
dict_codes = {}

for i in folders_list:
	try:
		ccode = get_color_code(input_base_path+i)
		if(ccode not in dict_codes.keys()):
			dict_codes[ccode]= i
		else:
			print("STARTING FORCE PUSH")
			print(i)
			dict_codes = force_add_photo(dict_codes,ccode,i)
	except:
		leave=1

color_list = list(dict_codes.keys())
color_list.sort(key=get_hsv)
color_list.reverse()

dict_codes_final = {}
for i in color_list:
	dict_codes_final[i]=dict_codes[i]

final_des(dict_codes_final)