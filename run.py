import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from src.main import App

app = App()
Gtk.main()
