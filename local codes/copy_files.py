from shutil import copyfile

src_base = '/Volumes/UNTITLED/DCIM/142ND750/'
dst_base = '/Users/chethankarur/Documents/Elene selct2/'

l= ["DSC_8095","DSC_8116","DSC_8124","DSC_8142","DSC_8147","DSC_8148","DSC_8175","DSC_8180","DSC_8181","DSC_8187","DSC_8195","DSC_8220","DSC_8237","DSC_8247","DSC_8252","DSC_8257","DSC_8289","DSC_8320","DSC_8335","DSC_8365","DSC_8381","DSC_8407","DSC_8413","DSC_8447","DSC_8454","DSC_8473","DSC_8475","DSC_8497","DSC_8498","DSC_8504","DSC_8506","DSC_8523"]

for i in l:
	src = src_base+str(i)+'.NEF'
	dst = dst_base+str(i)+'.NEF'
	try:
		copyfile(src, dst)
		print (str(i)+' Done')
	except Exception as e:
		print (e)
		print (str(i)+' Skipped')