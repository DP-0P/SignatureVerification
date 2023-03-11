from PIL import ImageFilter, Image

img = Image.open('forgeries_1_1.png')

# im = im.convert('RGB')
# img.convert('RGB')

img = img.convert('RGB')

img = img.filter(ImageFilter.SMOOTH_MORE)
img = img.filter(ImageFilter.DETAIL)
img = img.resize((350,350))
img.show()

# im2 = im.filter(ImageFilter.MinFilter(3))
# im3 = im.filter(ImageFilter.MinFilter)  

# from PIL import ImageFilter
# from tqdm import tqdm
# from os import listdir
# import os
# from PIL import Image

# def imageDenoise(location,newLocation):
# 	for images in tqdm(os.listdir(location),desc='denoizzing...'):
# 		# print(images)
# 		if images.endswith(".png"):
# 			img = Image.open(r""+location+'/'+images)
# 			img = img.filter(ImageFilter.SMOOTH_MORE)
# 			img = img.filter(ImageFilter.DETAIL)
# 			img.save(f'C:\\Users\\ASUS\\Desktop\\SDP\\modifiedSignatures\\{newLocation}\\'+'denoised'+images.capitalize()+'.png')
			
# imageDenoise('C:\\Users\\ASUS\\Desktop\\SDP\\signatures\\full_forg','denoisedForged')
# imageDenoise('C:\\Users\\ASUS\\Desktop\\SDP\\signatures\\full_org','denoisedOG')