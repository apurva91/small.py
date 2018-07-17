from PIL import Image, ImageDraw, ImageFont


def add_text(img,text,font,fontsize,top,left,right=-1,bottom=-1,color="#000000"):
	'''
	If right will be mentioned that text will be aligned in center of left and right else it will be left aligned, similarly for bottom
	'''

	draw = ImageDraw.Draw(img)
	fontc = ImageFont.truetype(font,fontsize)
	w, h = draw.textsize(text,font=fontc)
	area = (left,top)
	if right != -1 and bottom == -1:
		area = (left + (right-left-w)/2,top)
	elif right == -1 and bottom != -1:
		area = (left,top + (top-bottom-h)/2)
	elif right != -1 and bottom != -1:
		area = (left + (right-left-w)/2,top + (top-bottom-h)/2)
	elif right == -1 and bottom == -1:
		area = (left,top)
	draw.text((area),text,font=fontc, fill=color)	
	return img

image_template="template.png"
font_address = "Montserrat-ExtraLight.ttf"
destination_folder = "."

x = [["ID","Name","Phone Number","City Name"]]

for y in x:	

	img = Image.open(image_template)
	img = add_text(img,y[0],font_address,36,462,0,right=img.size[0],bottom=-1,color="#838383")
	img = add_text(img,y[1].title(),font_address,90,296,0,right=img.size[0],bottom=-1,color="#424242")
	img = add_text(img,y[2],font_address,48,603,963,color="#838383")
	img = add_text(img,y[3].title(),font_address,48,603,372,color="#838383")
	img.save(destination_folder+"/"+y[1]+"."+img.format,img.format)
	print("Image Saved Successfully for "+y[1])