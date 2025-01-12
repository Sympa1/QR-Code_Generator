import sys
import os
from tkinter import filedialog, colorchooser, messagebox, ttk
from PIL import Image, ImageTk
import qrcode
import tkinter as tk


def resource_path(relative_path):
    """Bestimmt den Pfad zu einer eingebetteten Ressource (z. B. Bilder)"""
    try:
        # PyInstaller erstellt beim Packen ein temporäres Verzeichnis
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


class QrCodeGenerieren:
    """Diese Klasse erzeugt die QR Codes. Data = Inhalt des QR Codes | fl_color = Füllfarbe | bg_color = Hintergrundfarbe"""

    def __init__(self, data: str, fl_color: str, bg_color: str, pfad: str):
        # Objekt der Bibliotheksklasse "QRCode" als Klassenattribut speichern
        self.qr = qrcode.QRCode(box_size=10, border=2)
        self.data = data
        self.fl_color = fl_color
        self.bg_color = bg_color
        self.pfad = pfad

    def qr_erzeugen(self):
        # Datensatz hinzufügen
        self.qr.add_data(self.data)

        # QR-Code generieren und optimieren
        self.qr.make(fit=True)

        # Bild des QR-Codes erzeugen
        img = self.qr.make_image(fill_color=self.fl_color, back_color=self.bg_color)

        # Bild speichern
        img.save(self.pfad)

        print("QR-Code erfolgreich generiert und als 'qrcode.png' gespeichert.")


class Gui(tk.Tk):
    """Die Klasse GUI erbt von der TKinter Klasse und beinhaltet alle GUI Komponenten."""

    def __init__(self):
        super().__init__()

        self.title("QR-Code Generator")

        # Icon laden und in ein unterstütztes Format konvertieren um Linux Kompatibilität zu ermöglichen
        self.icon_image = Image.open(resource_path("img/qr-code-outline.ico"))
        self.icon_photo = ImageTk.PhotoImage(self.icon_image)
        # Icon setzen
        self.iconphoto(False, self.icon_photo)

        # Deklaration der Hilfsvariablen
        self.farbwahl_fuell = "Black"
        self.farbwahl_bg = "White"
        self.dateipfad = self.user_verzeichnis()

        self.gui_widgets()

    def gui_widgets(self):
        """Funktion um alle GUI Komponenten zu erstellen."""

        # Läd den QR mit dem GitHub Repo Link & zeigt diesen an
        self.qr_image = Image.open(resource_path("img/qrcode_gui.png"))
        self.qr_image.thumbnail((200, 200))
        self.qr_photo = ImageTk.PhotoImage(self.qr_image)
        self.qr_label = ttk.Label(self, image=self.qr_photo)
        self.qr_label.pack(pady=20)

        # Erstellt den Rahmen für die Nutzereingaben
        self.user_eingaben_lfrm = ttk.Labelframe(self, text="QR-Code Einstellung")
        self.user_eingaben_lfrm.pack(pady=(0, 20), padx=10)

        # QR-Code Texteingabe
        self.user_entr_lfrm = ttk.Labelframe(self.user_eingaben_lfrm, text="QR-Code Text")
        self.user_entr_lfrm.pack(pady=10, padx=10)
        self.user_entr = ttk.Entry(self.user_entr_lfrm, width="60")
        self.user_entr.pack(pady=5, padx=5)

        # QR-Code Farbwahl
        self.farbwahl_lfrm = ttk.Labelframe(self.user_eingaben_lfrm, text="Farbwahl")
        self.farbwahl_lfrm.pack(pady=10, padx=10, side="left")
        self.fuell_btn = ttk.Button(self.farbwahl_lfrm, text="Füllfarbe", command=lambda: self.farbwahl(1))
        self.fuell_btn.pack(side="left", pady=5, padx=5)
        self.bg_btn = ttk.Button(self.farbwahl_lfrm, text=" Hintergrundfarbe ", command=lambda: self.farbwahl(2))
        self.bg_btn.pack(pady=5, padx=5)

        # QR-Code Speicherort
        self.farbwahl_lfrm = ttk.Labelframe(self.user_eingaben_lfrm, text="Speicherort wählen")
        self.farbwahl_lfrm.pack(pady=10, padx=10, side="right")
        self.fuell_btn = ttk.Button(self.farbwahl_lfrm, text=" Durchsuchen ", command=lambda: self.speicherort())
        self.fuell_btn.pack(pady=5, padx=5)

        # Darstellung der Usereinstellungen
        self.usereinstellungen_lfrm = ttk.Labelframe(self, text="Gewählte Einstellungen")
        self.usereinstellungen_lfrm.pack(pady=(20, 0), padx=10)
        self.usereinstellungen_fuell_label = ttk.Label(self.usereinstellungen_lfrm, text="Gewählte Füllfarbe: ")
        self.usereinstellungen_fuell_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.usereinstellungen_fuell_label_farbe = ttk.Label(self.usereinstellungen_lfrm, text="      ", background=self.farbwahl_fuell)
        self.usereinstellungen_fuell_label_farbe.grid(row=0, column=1, pady=5, padx=5)
        
        self.usereinstellungen_bg_label = ttk.Label(self.usereinstellungen_lfrm, text="Gewählte Hintergrundfarbe: ")
        self.usereinstellungen_bg_label.grid(row=1, column=0, pady=5, padx=5)
        self.usereinstellungen_bg_label_farbe = ttk.Label(self.usereinstellungen_lfrm, text="      ", background=self.farbwahl_bg)
        self.usereinstellungen_bg_label_farbe.grid(row=1, column=1, pady=5, padx=5)

        self.usereinstellungen_pfad_label = ttk.Label(self.usereinstellungen_lfrm, text="Gewählter Speicherort:")
        self.usereinstellungen_pfad_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.usereinstellungen_pfad_label_text = ttk.Label(self.usereinstellungen_lfrm, text=self.user_verzeichnis())
        self.usereinstellungen_pfad_label_text.grid(row=2, column=1, pady=5, padx=5)

        # Steuerbuttons
        self.btn_frm = ttk.Frame(self, width=60)
        self.btn_frm.pack(pady=10, side="right")
        self.erstelle_qr_btn = ttk.Button(self.btn_frm, text="QR-Code Generieren", command=lambda: self.erstelle_qr())
        self.erstelle_qr_btn.pack(side="left", padx=5, pady=10)
        self.abbrechen_btn = ttk.Button(self.btn_frm, text="Abbrechen", command=lambda: self.destroy())
        self.abbrechen_btn.pack(side="right", padx=(5, 10), pady=10)

    def farbwahl(self, btn_id):
        """Öffnet den Colochooser und speichert diesen in der Variable self.farbwahl_fuell / self.farbwahl_bg
            btn_id (int): Eine eindeutige ID des Buttons
        """
        if btn_id == 1:
            farbe = colorchooser.askcolor(title="Farbauswahl")
            self.farbwahl_fuell = farbe[1]
            self.usereinstellungen_fuell_label_farbe.config(background=self.farbwahl_fuell)
        elif btn_id == 2:
            farbe = colorchooser.askcolor(title="Farbauswahl")
            self.farbwahl_bg = farbe[1]
            self.usereinstellungen_bg_label_farbe.config(background=self.farbwahl_bg)

    def user_verzeichnis(self):
        # Dynamisch das Benutzerverzeichnis ermitteln
        benutzer_verzeichnis = os.path.expanduser("~")
        
        # Mögliche Dokumentenordner-Namen (deutsch und englisch)
        dokument_ordner = ["Dokumente", "Documents"]
        
        # Prüfe welcher Ordner existiert
        initial_verzeichnis = None
        for ordner in dokument_ordner:
            test_pfad = os.path.join(benutzer_verzeichnis, ordner)
            if os.path.exists(test_pfad):
                initial_verzeichnis = test_pfad
                break
        return initial_verzeichnis + "/qrcode.png"

    def speicherort(self):
        initial_verzeichnis = self.user_verzeichnis()
        
        # Öffnet den Dateidialog zum Speichern der Datei
        self.dateipfad = filedialog.asksaveasfilename(
            defaultextension=".png",
            initialfile="qrcode.png",
            initialdir=initial_verzeichnis,
            filetypes=[
                ("PNG Dateien", "*.png"),
                ("JPG Dateien", "*.jpg"),
                ("SVG Dateien", "*.svg"),
                ("Alle Dateien", "*.*")
            ],
            title="Speicherort auswählen"
        )
        self.usereinstellungen_pfad_label_text.config(text=self.dateipfad)

    def erstelle_qr(self):
        if os.path.exists(self.dateipfad):
            if messagebox.askyesnocancel("Speicherort vergeben", "Der gewählte Speicherort existiert bereits."):
                ueberschreibe = True
        else:
            ueberschreibe = True
        
        if ueberschreibe:
            self.data = self.user_entr.get()
            qr = QrCodeGenerieren(self.data, self.farbwahl_fuell, self.farbwahl_bg, self.dateipfad)
            qr.qr_erzeugen()
            if os.path.exists(self.dateipfad):
                messagebox.showinfo("Erfolg!", "Der QR-Code wurde Erfolgreich gespeichert.")
                self.qr_image = Image.open(self.dateipfad)
                self.qr_image.thumbnail((200, 200))
                self.qr_photo = ImageTk.PhotoImage(self.qr_image)
                self.qr_label.config(image=self.qr_photo)
            else:
                messagebox.showerror("Fehler!", "Der QR-Code konnte nicht gespeichert werden.")

def main():
    app = Gui()
    app.mainloop()

if __name__ == "__main__":
    main()