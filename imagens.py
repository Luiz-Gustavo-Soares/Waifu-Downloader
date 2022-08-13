from genericpath import isfile
import requests
from os import mkdir, path

class Imagens:
    def __init__(self):
        if not path.isdir('images'):
            mkdir('./images')

    def get_links_img(self, categoria=str, quant=1):
        img_urls = []
        
        for i in range(quant):
            r = requests.get(f'https://nekos.best/api/v2/{categoria}')
            data = r.json()
            img_urls.append(data["results"][0]["url"])
        return img_urls

    def get_imgs(self, link_imgs):
        imgs = []
        for link_img in link_imgs:
            imgs.append(requests.get(link_img).content)
        return imgs
    
    def get_img(self, link_img):
        img = requests.get(link_img).content
        return img

    def save_imgs(self, data_imgs):
        
        indice_img = 0
        for data_img in data_imgs:
            while True:
                nome_img = f'img{indice_img}.png'
                
                if path.isfile('images/'+nome_img):
                    indice_img += 1
                else:
                    break
            
            with open(f'./images/{nome_img}', 'wb') as img:
                img.write(data_img)

            indice_img += 1
