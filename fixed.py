#!/usr/bin/python
# Filename: fixed.py

import gtk, sys

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()

		self.set_title("Fixed")
		self.set_size_request(300, 380)
		self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400,6400))
		self.set_position(gtk.WIN_POS_CENTER)

		try:
			self.bardejov = gtk.gdk.pixbuf_new_from_file("bardejov.jpg")
			self.rotunda = gtk.gdk.pixbuf_new_from_file("rotunda.jpg")
			self.mincol = gtk.gdk.pixbuf_new_from_file("mincol.jpg")
		except Exception, e:
			print(e.message)
			sys.exit(1)

		image1 = gtk.Image()
		image2 = gtk.Image()
		image3 = gtk.Image()

		image1.set_from_pixbuf(self.bardejov)
		image2.set_from_pixbuf(self.rotunda)
		image3.set_from_pixbuf(self.mincol)

		fixed = gtk.Fixed()

		fixed.put(image1, 20, 30)
		fixed.put(image2, 20, 100)
		fixed.put(image3, 20, 160)

		self.add(fixed)

		self.connect("destroy", gtk.main_quit)

		self.show_all()

PyApp()
gtk.main()
