import os
import json
import tkinter as tk

class app:
    def __init__(self):
        # loading data
        self.settingPath = "notepad/settings.json"
        self.Settings = self.loadSettings()

        # initiating tkinter window
        self.root=tk.Tk(className="notepad")
        self.root.geometry(self.Settings["startup_layout"])
        self.root.configure(background="#444444")

        # creating widgets
        self.T_field = tk.Text(self.root,height=40,
        background=self.Settings["settings"]["background"],
        foreground=self.Settings["settings"]["foreground"])    
        self.T_field.grid(column=0,row=0)

        # making shortcuts
        self.root.bind('<Control-s>', self.Export)
        self.root.bind('<Control-q>', self.showSettings)
        # loading data.txt
        self.Import()
        # initiated main loop
        self.root.mainloop()
    def loadSettings(self):
        f = open(self.settingPath,'r')
        Settings = json.load(f)
        f.close()
        return Settings
    def showSettings(self,arg):
        wk.Worker(self.settingPath)
    def Import(self):
        self.T_field.insert(tk.INSERT,open(self.Settings["save_path"], "r",encoding="utf8").read())
    def Export(self,arg):
        result = self.T_field.get("1.0",'end')
        file1 = open(self.Settings["save_path"], "w",encoding="utf8")
        file1.write(result)
        file1.close()
app()