from PIL import Image as im
import os

Input_Folder = "input"
Output_Folder = "output"
Watermark_Path="logo.png"
Percent_Width=30
Alpha_Percent=60
# Currently places in the bottom left corner

files_list = [f for f in os.listdir(Input_Folder) if f.lower().endswith("jpg") or f.lower().endswith("png") or f.lower().endswith("jpeg")]

if not os.path.isdir(Output_Folder):
	os.mkdir(Output_Folder)

watermark = im.open(Watermark_Path)
w_size = watermark.size
watermark.putalpha(Alpha_Percent * 255 //100)

for file in files_list:
	file_path = Input_Folder + "/" + file
	img = im.open(file_path)
	size = img.size
	w_width = size[0] * Percent_Width // 100
	w_height = w_width * w_size[1] // w_size[0]
	wm = watermark.resize((w_width, w_height), im.ANTIALIAS)
	img.paste(wm , (0,img.size[1] - w_height),mask=wm)
	img.save(Output_Folder + "/" + file)
	print ("Converted " + file)