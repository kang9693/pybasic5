import wx
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Key Press Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        btn = wx.Button(panel, label="OK")
 
        btn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
 
    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        print ("입력코드:%d" % keycode)
        if keycode == wx.WXK_SPACE:
            print ("you pressed the spacebar!")
        event.Skip()
 
 
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm()
    frame.Show()
    app.MainLoop()