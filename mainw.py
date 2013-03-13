#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class MainWindow(object):
    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self,title="My Main Window",width=200,height=200):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title(title)
        self.window.set_size_request(width, height)
        self.window.connect("delete_event", self.delete_event)

    def get_widget(self):
        pass

    def main(self):
        widget=self.get_widget()
        if widget:
            self.window.add(widget)
            self.window.show_all()
            gtk.main()
