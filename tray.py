#
#! PyQt5 Tray icon

# from PyQt5 import QtCore, QtGui, QtWidgets
# # code source: https://stackoverflow.com/questions/893984/pyqt-show-menu-in-a-system-tray-application  - add answer PyQt5
# #PyQt4 to PyQt5 version: https://stackoverflow.com/questions/20749819/pyqt5-failing-import-of-qtgui
# class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

#     def __init__(self, icon, parent=None):
#         QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
#         menu = QtWidgets.QMenu(parent)
#         exitAction = menu.addAction("Exit")
#         self.setContextMenu(menu)

# def main(image):
#     app = QtWidgets.QApplication(sys.argv)

#     w = QtWidgets.QWidget()
#     trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)

#     trayIcon.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     on=r'icon.ico'# ADD PATH OF YOUR ICON HERE .png works
#     main(on)

#! Tkinter icon

# import tkinter as tk
# root = tk.Tk()
# # The image must be stored to Tk or it will be garbage collected.
# root.image = tk.PhotoImage(file='icon.png')
# label = tk.Label(root, image=root.image, bg='white')
# root.overrideredirect(True)
# root.geometry("+250+250")
# root.lift()
# root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", "white")
# label.pack()
# label.mainloop()

#TODO": Interface not done

# from pystray import MenuItem as item
# import pystray
# from PIL import Image
# import tkinter as tk

# window = tk.Tk()
# window.title("Title")

# def quit_window(icon, item):
#     icon.stop()
#     window.destroy()

# def show_window(icon, item):
#     icon.stop()
#     window.after(0,window.deiconify)

# def withdraw_window():
#     window.withdraw()
#     image = Image.open("icon.ico")
#     menu = (item('Quit', quit_window), item('Show', show_window))
#     icon = pystray.Icon("name", image, "title", menu)
#     icon.run()

# window.protocol('WM_DELETE_WINDOW', withdraw_window)
# window.mainloop()

#TODO: Interface end
