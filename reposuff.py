from Tkinter import *
tk = Tk()
tk.wm_title("Lockers")
entry = Spinbox(master = tk, from_ = 1, to = 1000)

def makeGUI():
    entry.pack()
    button = Button(master = tk, text = "Done", command = calculate)
    button.pack()

def finish(text):
    output = ""
    j = 0
    for i in text :
        output += str(i) + ("" if j == len(text) - 1 else ", ")
        output += "\n" if (j + 1) % 15 == 0 else ""
        j += 1
    text = Label(master = tk, text = output)
    text.pack()
    
def calculate():
    size = int(entry.get())
    reposuff = [0] * size
    for i in range(1, size + 1) :
        for j in range(1, size + 1) :
            if j % i == 0 :
                reposuff[j - 1] -= reposuff[j - 1] * 2 - 1
    finish(reposuff)

makeGUI()

mainloop()
