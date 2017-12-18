import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import sqlite3
store = Gtk.ListStore(str, str, float)



treeiter = store.append(["The Art of Computer Programming",
                         "Donald E. Knuth", 25.46])



store = Gtk.ListStore(str, str, float,str)
Listaproductos = [
("VDE5","Figura1",65,"WarhammerType"),
("VAD3","Figura2",32,"Warhammer40Type"),
("HYH5","MaquetaTank1",48,"TanksWII"),
("ACE2","Pinturas1",67,"PinturasType"),
("HTR5", "Figura3",21,"WarhammerType"),
]


treeView = Gtk.TreeView(store)

cellRenderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Title", store, text=0)
