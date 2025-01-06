import qrcode
import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, filedialog

class QrCodeGenerieren:
    """Diese Klasse erzeugt die QR Codes. Data = Inhalt des QR Codes | fl_color = Füllfarbe | bg_color = Hintergrundfarbe"""

    def __init__(self, data: str, fl_color, bg_color):
        # Objekt der Bibliotheksklasse "QRCode" als Klassenattribut speichern
        self.qr = qrcode.QRCode(box_size=10, border=2)
        self.data = data
        self.fl_color = fl_color
        self.bg_color = bg_color

    def qr_erzeugen(self):
        # Datensatz hinzufügen
        self.qr.add_data(self.data)

        # QR-Code generieren und optimieren
        self.qr.make(fit=True)

        # Bild des QR-Codes erzeugen
        img = self.qr.make_image(fill_color=self.fl_color, back_color=self.bg_color)

        # Bild speichern
        img.save("qrcode.png")

        print("QR-Code erfolgreich generiert und als 'qrcode.png' gespeichert.")


# TODO: später löschen
qr_data = "Hallo Welt!"
fl_color = "Green"
bg_color = "Black"
t = QrCodeGenerieren(qr_data, fl_color, bg_color)
t.qr_erzeugen()


# TODO: GUI Klasse hier
class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("QR-Code Generator")
        #TODO: App Icon vom GUI zu einem QR-Code ändern

        self.gui_widgets()

    def gui_widgets(self):
        pass


# TODO: IF Name Main