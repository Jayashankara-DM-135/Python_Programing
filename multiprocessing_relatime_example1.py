import time
from PIL import Image, ImageFilter



img_names = [
    'photo-1516117172878-fd2c41f4a759',
    'photo-1532009324734-20a7a5813719',
    'photo-1524429656589-6633a470097c',
    'photo-1530224264768-7ff8c1789d79',
]

t1 = time.perf_counter()
size = (1200, 1200)
for img_name in img_names:
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed')

t2 = time.perf_counter()

print("Script is completed in {round(t2-t1)} second (s)")


