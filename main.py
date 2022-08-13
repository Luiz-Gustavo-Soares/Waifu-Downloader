import PySimpleGUI as sg
from imagens import Imagens

im = Imagens()

categoria_nekos = ['husbando', 'kitsune', 'neko', 'waifu']


sg.theme('reddit')

layout = [[sg.Text("Image Waifu Download", font=('Arial', 15))],
          [sg.Sizer(1, 20)],
          [sg.Text("Selecione a categoria: "), sg.OptionMenu(categoria_nekos, key='categoria')],
          [sg.Text("Quantidade de imagens: "), sg.Input('1', size=(5, 1), justification='right', key='quantidade')],
          [sg.Button("Download", key='download')]
          ]


janela = sg.Window('Waifu Downloader', layout)

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'download':
        categoria = str(values['categoria'])
        quantidade = str(values['quantidade'])
        
        if categoria == '':
            print('categoria não selecionada')
        elif not quantidade.isnumeric():
            print('Quantidade precisa ser um número')
        
        else:
            quantidade = int(quantidade)
            
            links = im.get_links_img(categoria, quantidade)
            imagens = im.get_imgs(links)
            im.save_imgs(imagens)

