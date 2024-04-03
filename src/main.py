import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import threading

from src.imagens import Imagens


categoria_nekos = ['husbando', 'kitsune', 'neko', 'waifu']
imdown = Imagens()

def download(p, qnt, cat, button):
    '''
    Realiza o download das imagens de acordo com os os parametros informados
    :param p: Gtk.ProgressBar
    :param qnt: int quantidade de imagens para serem baixadas
    :param cat: str Categoria selecionada
    :param button: Gtk.Button botão a ser abilitado apos o terminio dos downloads
    :return: None
    '''

    qnt_passo = 1/qnt
    p.set_fraction(0)
    
    for i in range(qnt):
        links = imdown.get_links_img(cat)
        imagens = imdown.get_imgs(links)

        imdown.save_imgs(imagens)
        increment = (i/qnt) + qnt_passo

        p.set_fraction(increment)

    button.set_sensitive(True)

class App:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("src/layout/layout_waifu.glade")
        builder.connect_signals(self)

        win = builder.get_object('window')
        win.set_title('Waifu Images')
        win.set_icon_from_file('src/imgs/icon.png')
        win.show_all()
        
        self.progress_bar = builder.get_object('progress_bar')

        for c in categoria_nekos:
            builder.get_object('categorias').append(c,c)

        self.categoria = categoria_nekos[3]
        self.qnt_imgs = 1

    def on_window_destroy(self, *args):
        Gtk.main_quit()

    def on_categorias_changed(self, categorias):
        self.categoria = categorias.get_active_text()

    def on_quantidade_value_changed(self, quantidade):
        self.qnt_imgs = quantidade.get_value_as_int()

    def download_clicked_cb(self, button):
        button.set_sensitive(False)

        down = threading.Thread(target=download, args=(self.progress_bar, self.qnt_imgs, self.categoria, button,))
        down.start()
