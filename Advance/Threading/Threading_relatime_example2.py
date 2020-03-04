import time
import requests
import concurrent.futures

img_urls = [
     'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
]

def download_img(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img = img_url.split('/')[0]
    print(img)
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded')

t1 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, img_urls)
t2 = time.perf_counter()
print(f'script complted in {round(t2 -t1)} second (s)')
