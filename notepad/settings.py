import tkinter as tk
import json

print("opening Settiings For the console")

path = "data/settings.json"
f = open(path,'r')
Settings = json.load(f)
f.close()

new=tk.Tk(className='Settings')
new.geometry("350x350")
def updateSettings():
    ndata = {
        "save_path" : file_path.get("1.0",'end-1c'),
        "startup_layout" : startup_layout.get("1.0",'end-1c'),
        "settings" : {
            "foreground" : foreground.get("1.0",'end-1c'),
            "background" : background.get("1.0",'end-1c'),
        }
    }
    json_object = json.dumps(ndata,indent=4)
    print("Settings Updated SuccessFully")
    with open(path, "w") as outfile:
        outfile.write(json_object)

tk.Label(new, text= "data file path").grid(row = 1, column=0)
file_path = tk.Text(new, height=5, width=20)
file_path.insert(tk.END, Settings["save_path"])

tk.Label(new, text= "Layout ").grid(row = 2, column=0)
startup_layout = tk.Text(new, height=1, width=10)
startup_layout.insert(tk.END, Settings["startup_layout"])

tk.Label(new, text= "Foreground ").grid(row = 2, column=0)
foreground = tk.Text(new, height=1, width=10)
foreground.insert(tk.END, Settings["settings"]["foreground"])

tk.Label(new, text= "Background ").grid(row = 3, column=0)
background = tk.Text(new, height=1, width=10)
background.insert(tk.END, Settings["settings"]["background"])

tk.Button(new,text = 'Update', command = updateSettings).grid(row=7,column=0)

file_path        .grid(row = 1, column=1)
startup_layout         .grid(row = 2, column=1)
foreground             .grid(row = 3, column=1)
background             .grid(row = 4, column=1)

new.mainloop()