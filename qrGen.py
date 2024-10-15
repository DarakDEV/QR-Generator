import wx
import qrGenBackend as qr

class MiGUI(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Generador de QR")

        #Montaje de la primera ventana de la interfaz
        self.panel = wx.Panel(self)

        self.label_1 = wx.StaticText(self.panel, label="Nombre de fichero:")
        self.text_component_1 = wx.TextCtrl(self.panel)

        self.label_2 = wx.StaticText(self.panel, label="URL a convertir a QR:")
        self.text_component_2 = wx.TextCtrl(self.panel)

        self.boton = wx.Button(self.panel, label="Generar QR")
        self.boton.Bind(wx.EVT_BUTTON, self.on_boton_click)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.label_1, 0, wx.ALL, 5)
        sizer.Add(self.text_component_1, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.label_2, 0, wx.ALL, 5)
        sizer.Add(self.text_component_2, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.boton, 0, wx.ALL | wx.CENTER, 5)

        self.panel.SetSizer(sizer)
        self.Show()

    def on_boton_click(self, event):
        name = self.text_component_1.GetValue()
        url = self.text_component_2.GetValue()
        qr.generate(name,url)

        img_path = qr.path()  # Reemplaza con la ruta real de tu archivo PNG
        img = wx.Image(img_path, wx.BITMAP_TYPE_PNG)

        # Mostrar imagen en popup
        bitmap = wx.Bitmap(img)
        dialog = wx.Dialog(self, title="QR")
        dialog.SetSize((400, 400))  # Set the size of the dialog

        static_bitmap = wx.StaticBitmap(dialog, wx.ID_ANY, bitmap)
        copy_button = wx.Button(dialog, label="Copiar imagen")
        copy_button.Bind(wx.EVT_BUTTON, self.on_copy_button_click(img_path))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(copy_button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(static_bitmap, 0, wx.ALL | wx.CENTER, 5)
        
        dialog.SetSizer(sizer)
        dialog.Fit()

        dialog.ShowModal()
        dialog.Destroy()

    def on_copy_button_click(self, img_path):
    # Copiar imagen al portapapeles
        img = wx.Image(img_path, wx.BITMAP_TYPE_PNG)
        bitmap = wx.Bitmap(img)
        clipboard = wx.Clipboard()
        clipboard.SetData(wx.BitmapDataObject(bitmap))
        clipboard.Flush()

if __name__ == "__main__":
    app = wx.App()
    gui = MiGUI()
    app.MainLoop()