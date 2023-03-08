'''IMPORTS'''
from PIL import Image

'''PRE-PROCESSING: RESIZING'''
for person in range(1,11):
  for attempt in range(1,6):
    img_path = f"D:\cedar_minimal\\real\original_{person}_{attempt}.png"
    print("-----------------------------")
    print(img_path)
    print("-----------------------------")
    img = Image.open(img_path)
    img = img.resize((500,500))
    img = img.save(img_path)