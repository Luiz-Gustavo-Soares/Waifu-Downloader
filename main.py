import PySimpleGUI as sg
from imagens import Imagens

im = Imagens()

categoria_nekos = ['husbando', 'kitsune', 'neko', 'waifu']


sg.theme('reddit')

layout_inputs = [[sg.Text("Selecione a categoria: "), sg.OptionMenu(categoria_nekos, key='categoria')],
                 [sg.Text("Quantidade de imagens: "), sg.Input('1', size=(5, 1), justification='right', key='quantidade')],
                 [sg.ProgressBar(100, bar_color=('green', 'white'), size_px=(150, 10), border_width=1, key='progreco')],
                 [sg.Sizer(1, 30)]]

layout = [[sg.Text("Image Waifu Download", font=('', 15))],
          [sg.Sizer(1, 20)],
          [sg.Column(layout_inputs), sg.Image('waifu.png')],
          [sg.Button("Download", key='download'), sg.Text('', key='mensagem', font=('', 7), justification='right', size=(40, 1), text_color='red')]]


janela = sg.Window('Waifu Downloader', layout)

numero_download = 0
quant_barra_progreco_vez = 1
quant_barra_progreco = 0

while True:
    event, values = janela.read(40)

    if event == sg.WIN_CLOSED:
        break


    if numero_download > 0:
        janela['download'].update(disabled=True)
        janela['progreco'].update(visible=True)
        numero_download -= 1
        quant_barra_progreco += quant_barra_progreco_vez

        links = im.get_links_img(categoria)
        imagens = im.get_imgs(links)
        im.save_imgs(imagens)
        
        janela['progreco'].update(quant_barra_progreco)
        
        
    else:
        janela['progreco'].update(visible=False)
        janela['progreco'].update(0)
        janela['download'].update(disabled=False)
   

    if event == 'download':
        categoria = str(values['categoria'])
        quantidade = str(values['quantidade'])
        
        if categoria == '':
            janela['mensagem'].update('Categoria não selecionada')
        elif not quantidade.isnumeric():
            janela['mensagem'].update('Quantidade precisa ser um número')
        
        else:
            numero_download = int(quantidade)
            quant_barra_progreco_vez = int(100/numero_download)
            quant_barra_progreco = 0
            janela['mensagem'].update('')

