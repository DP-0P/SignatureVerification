# dataset resized
import os
from os import listdir
from PIL import Image
from tqdm import tqdm

def imageResize(location,newLocation):
	for images in tqdm(os.listdir(location),desc='processing...'):
		if images.endswith(".png"):
			img = Image.open(r""+location+'/'+images)
			img = img.resize((350,350))
			img.save(f'C:\\Users\\ASUS\\Desktop\\SDP\\modifiedSignatures\\{newLocation}\\'+'resized'+images.capitalize()+'.png')

# imageResize('C:\\Users\\ASUS\\Desktop\\SDP\\signatures\\full_forg','modifiedForged')
# imageResize('C:\\Users\\ASUS\\Desktop\\SDP\\signatures\\full_org','modifiedOG')

# dataset split into train validation test

