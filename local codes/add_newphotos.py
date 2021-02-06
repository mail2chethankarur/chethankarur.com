folder_name = 'nature'
start_num = 125
end_num = 137
outputpath = '/Users/chethankarur/Pictures/addon.txt'
mainstring = ''

count  =1
for i in range(start_num,end_num+1):
    iterstring = """<div class="mbr-gallery-item mbr-gallery-item__mobirise3 mbr-gallery-item--p0" data-tags="Animated" data-video-url="false">
    <div href="#lb-gallery1-6" data-slide-to="{0}"data-toggle="modal">
        <img alt="" src="img/{1}/{2}.webp">
        <span class="icon-focus"></span>
    </div>
</div> \n""".format(i,folder_name,i+1)
    iterstring2 = """<div class="carousel-item">
<img alt="" src="img/{0}/{1}.webp">
</div>""".format(folder_name,i)
	
    if (count==1):
		i1 = iterstring
		i2 = iterstring2
		count+=1
    else:
		i1 += iterstring
		i2 += iterstring2

mainstring += i1+"\n"+"\n"+i2

text_file = open(outputpath, "w")
n = text_file.write(mainstring)
text_file.close()
