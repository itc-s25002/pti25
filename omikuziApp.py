import tkinter as tk
import def4
def dispLabel():
    lbl.configure(text = "運勢は" + def4.omikuzi())

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="おみくじ")
btn = tk.Button(text="引く", command = dispLabel, width=10, height = 2)

lbl.pack()
btn.pack()
tk.mainloop()
