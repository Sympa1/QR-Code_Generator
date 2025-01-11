import qrcode
import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, filedialog
from PIL import Image, ImageTk

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
fl_color = "Black"
bg_color = "White"
t = QrCodeGenerieren(qr_data, fl_color, bg_color)
t.qr_erzeugen()


# TODO: GUI Klasse hier
class Gui(tk.Tk):
    """Die Klasse GUI erbt von der TKinter Klasse und beinhaltet alle GUI Komponenten.
    """
    def __init__(self):
        super().__init__()

        self.title("QR-Code Generator")
        # self.geometry("400x430")

        # Icon laden und in ein unterstütztes Format konvertieren um Linux kompatiblität zu ermöglichen
        self.icon_image = Image.open("qr-code-outline.ico")
        self.icon_photo = ImageTk.PhotoImage(self.icon_image)
        # Icon setzen
        self.iconphoto(False, self.icon_photo)
        
        # TODO: Fenstergröße anpassen

        self.gui_widgets()

    def gui_widgets(self):
        """ Funktion um alle GUI Komponenten zu erstellen.
        """

        # LÄd den QR mit dem GitHub Repo Link & zeigt diesen an
        self.qr_image = Image.open("qrcode_gui.png")
        self.qr_image.thumbnail((200, 200))
        self.qr_photo = ImageTk.PhotoImage(self.qr_image)
        self.qr_label = ttk.Label(self, image=self.qr_photo)
        self.qr_label.pack(pady=20)

        # Erstellt den Rahmen für die Nutzereingaben
        self.user_eingaben_lfrm = ttk.Labelframe(self, text="QR-Code Einstellung")
        self.user_eingaben_lfrm.pack(pady=20)
        # QR-Code Texteingabe
        self.user_entr_lfrm = ttk.Labelframe(self.user_eingaben_lfrm, text="QR-Code Text")
        self.user_entr_lfrm.pack(pady=10, padx=10)
        self.user_entr = ttk.Entry(self.user_entr_lfrm, width="60")
        self.user_entr.pack(pady=5, padx=5)


def main():
    app = Gui()
    app.mainloop()

if __name__ == "__main__":
    main()