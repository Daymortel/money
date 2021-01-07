from tkinter import *

root = Tk()
root.title("Money Render")

# Object's price
p = Entry(root, width = 35, borderwidth = 5)
p.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
p.insert(0, "Combien coûte le bien ?")

# Money gived
m = Entry(root, width = 35, borderwidth = 5)
m.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)
m.insert(0, "Combien est-ce que tu payes ?")

# Money returned
r = Entry(root, width = 35, borderwidth = 5)
r.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)
r.insert(0, " euros de rendus !")

def click_ok():
    first = m.get()
    global object_price
    object_price = float(first)
    second = p.get()
    r.insert(0, object_price - float(second))

button_ok = Button(root, text="Calculer", command = click_ok, padx = 100, pady = 20, fg = "#ffffff", bg = "#123456")
button_ok.grid(row = 3, column = 0)

root.mainloop()