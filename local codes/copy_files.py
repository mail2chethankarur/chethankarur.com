from shutil import copyfile

src_base = '/Volumes/UNTITLED/DCIM/141ND750/'
dst_base = '/Users/chethankarur/Documents/Elene selct/'

# l = [9478,9475,9473,9471,9470,9469,9466,9462,9461,9460,9457,9444,9442,9441,9440,9439,9438,9429,9427,9415,9413,9410,9407,9406,9405,9403,9401,9397,9392,9381,9378,9372,9371,9370,9369,9368,9365,9362,9361]
l = ["DSC_7472","DSC_7478","DSC_7483","DSC_7485","DSC_7500","DSC_7522","DSC_7532","DSC_7536","DSC_7558","DSC_7577","DSC_7579","DSC_7620","DSC_7625","DSC_7638","DSC_7665","DSC_7685","DSC_7697","DSC_7741","DSC_7758","DSC_7759","DSC_7767","DSC_7779","DSC_7785","DSC_7791","DSC_7797","DSC_7801","DSC_7803","DSC_7815","DSC_7835","DSC_7846","DSC_7849","DSC_7944","DSC_7962","DSC_8001"]
for i in l:
	src = src_base+str(i)+'.NEF'
	dst = dst_base+str(i)+'.NEF'
	try:
		copyfile(src, dst)
		print (str(i)+' Done')
	except Exception as e:
		print (e)
		print (str(i)+' Skipped')