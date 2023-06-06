from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("600x600")
root.title("Planetpedia")
root.configure(bg="PeachPuff2")

ipath = ""

def openimg():
    global ipath
    ipath = filedialog.askopenfilename(title="Open Image File", type="*.jpg *.gif *.png *.jpeg")
    img = ImageTk.PhotoImage(file=ipath)
    lblImg.configure(image=img)
    lblImg.image = img
    # I forgot/i don't know about the close function.
    
lblImg = Label(root, bg="yellow", highlightthickness=5, borderwidth=3, relief=SOLID)
lblImg.place(relx=0.5, rely=0.5, anchor=CENTER)

obtn = Button(text="Open Image", relief="ridge", bg="skyblue", command=openimg)
obtn.place(relx=0.5, rely=0.25, anchor=CENTER)

root.mainloop()