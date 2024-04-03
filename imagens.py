import requests
from os import mkdir, path

class Imagens:
    def __init__(self):
        '''
        Inicialização da classe
        Cria o diretorio 'images/' se não existir
        '''
        
        if not path.isdir('images'):
            mkdir('./images')

    def get_links_img(self, categoria=str, quant=1):
        '''
        Retorna uma lista de URLs de imagens
        :param categoria: str Categoria da imagem: 'husbando', 'kitsune', 'neko' ou 'waifu'
        :param quant: int Numero de imagens a serem retornadas
        :return: list
        '''

        img_urls = []
        
        for i in range(quant):
            r = requests.get(f'https://nekos.best/api/v2/{categoria}')
            data = r.json()
            img_urls.append(data["results"][0]["url"])
        return img_urls
    
    def get_img(self, link_img):
        '''
        Realiza o Download da imagem a parti da URL
        :param link_img: str Link a ser realizado o Download
        :ruturn: Image
        '''

        img = requests.get(link_img).content
        return img

    def get_imgs(self, link_imgs):
        '''
        Realiza o Download das imagens e as devolve em formato de lista 
        :param link_imgs: list Lista com os URLs das imagens
        :return: list
        '''

        imgs = []
        for link_img in link_imgs:
            imgs.append(self.get_img(link_img))
        return imgs

    def save_imgs(self, data_imgs):
        '''
        Salva uma lista de imagens no diretorio 'images/'
        :param data_imgs: list Lista contendo imagens
        :return: None
        '''

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
