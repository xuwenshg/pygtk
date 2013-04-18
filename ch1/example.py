#!/usr/bin/env python

import gtk, sys

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()
		 
		self.set_title("Icon")
		self.set_size_request(255, 200)
		self.set_position(gtk.WIN_POS_CENTER)

		try:
			self.set_icon_from_file("/home/xws/Pictures/2010073109223694.png")
		except Exception, e:
			print(e.message)
			sys.exit(1)

		btn1 = gtk.Button("Button")
		btn1.set_sensitive(False)
		btn1.set_tooltip_text("Btn1")
		btn2 = gtk.Button("Button")
		btn2.set_tooltip_text("btn2")
		btn3 = gtk.Button(stock = gtk.STOCK_CLOSE)
		btn3.set_tooltip_text("btn3")
		btn4 = gtk.Button("Button")
		btn4.set_size_request(80, 40)
		btn4.set_tooltip_text("btn4")

		fixed = gtk.Fixed()
		fixed.set_tooltip_text("fixed")

		fixed.put(btn1, 20, 30)
		fixed.put(btn2, 100, 30)
		fixed.put(btn3, 20, 80)
		fixed.put(btn4, 100, 80)

		self.connect("destroy", gtk.main_quit)
		self.add(fixed)
		self.show_all()

PyApp()
gtk.main()
