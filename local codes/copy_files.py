from shutil import copyfile

src_base = '/Volumes/UNTITLED/DCIM/142ND750/'
dst_base = '/Users/chethankarur/Documents/Elene selct/'

l = [9478,9475,9473,9471,9470,9469,9466,9462,9461,9460,9457,9444,9442,9441,9440,9439,9438,9429,9427,9415,9413,9410,9407,9406,9405,9403,9401,9397,9392,9381,9378,9372,9371,9370,9369,9368,9365,9362,9361]

for i in l:
	src = src_base+'DSC_'+str(i)+'.NEF'
	dst = dst_base+'DSC_'+str(i)+'.NEF'
	try:
		copyfile(src, dst)
		print (str(i)+' Done')
	except Exception as e:
		print (e)
		print (str(i)+' Skipped')