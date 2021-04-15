import tkinter as tk
import time
from scalper import chromescalp
from threading import Thread

root = tk.Tk()

canvas = tk.Canvas(root, height=700,width=700, bg='#0844bc', borderwidth = 0, highlightthickness = 0)
canvas.pack()

bestbuyimage = tk.PhotoImage(file='bestbuypic.png')
bestbuylabel = tk.Label(root, image=bestbuyimage, borderwidth=0)
bestbuylabel.place(x = 2,y=2)

frame = tk.Frame(root, bg='#0844bc', borderwidth = 0)
frame.place(relx=0.5, rely=0.2, relwidth=0.75,relheight=0.2, anchor='n')

label = tk.Label(frame, font='Helvetica 13 bold', text="Email Address:", bg='#0844bc')
label.place(relheight=0.15)

entry1= tk.Entry(frame, bg="#e0e6ef", font='Helvetica 13')
entry1.place(rely=0.2, relwidth=0.6,relheight=0.15)

label = tk.Label(frame, font= 'Helvetica 13 bold', text="Password:", bg='#0844bc')
label.place(rely=0.4, relheight=0.15)

entry2= tk.Entry(frame, bg="#e0e6ef", font='Helvetica 13')
entry2.place(rely=0.6, relwidth=0.6,relheight=0.15)

mainbutton = tk.Button(frame, text="Start Scalper", bg='#fff100', font='Helvetica 13 bold',command=lambda: runscalp())
mainbutton.place(relx=0.7,rely= 0.2, relheight=0.55,relwidth=0.3)

lower_frame = tk.Frame(root, bg='#0844bc')
lower_frame.place(relx= 0.6, rely= 0.4, relwidth= 0.9, relheight= 0.5, anchor='n')

label = tk.Label(lower_frame, font='Helvetica 13 bold', text="FE Editions: ", bg='#0844bc')
label.place(relx = 0)

label = tk.Label(lower_frame, font='Helvetica 13 bold', text="EVGA Editions: ", bg='#0844bc')
label.place(relx = 0.25)

label = tk.Label(lower_frame, font='Helvetica 13 bold', text="MSI Editions: ", bg='#0844bc')
label.place(relx = 0.53)

final_frame = tk.Frame(root, borderwidth = 0, bg='#0844bc')
final_frame.place(relx=0.55, rely=0.8, relwidth=0.75,relheight=0.2, anchor='n')

label = tk.Label(final_frame, font='Helvetica 13 bold', text="Add any and all GPU's.\n Warning: computer will run slower the more you run, \n4-6 is recommended.", bg='#0844bc')
label.place(relx = 0)

increment = 0

class gpubutton(chromescalp):

    def __init__(self, link):
        self.is_off = True
        self.link = link

    def buttonplace(self,gpu,xpos,ypos,price):
        global increment
        self.button = tk.Button(lower_frame, text=gpu, bg='#fff100', font='Helvetica 13 bold',command=lambda: self.switch())
        increment += 1
        self.button.place(relx=xpos,rely= ypos, relheight=0.05,relwidth=0.1)
        self.price = tk.Label(lower_frame, text=price, bg='#0844bc', font='Helvetica 13 bold')
        self.price.place(relx=xpos+.12,rely= ypos, relheight=0.05,relwidth=0.1)

    def switch(self):
        self.is_off
        if self.is_off:
            self.button.config(bg="#e0e6ef")
            self.is_off = False
        else:
            self.button.config(bg="#fff100")
            self.is_off = True

first = gpubutton("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")
second = gpubutton("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")
third = gpubutton("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
fourth = gpubutton("https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434")
fifth = gpubutton("https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454329.p?skuId=6454329")
sixth = gpubutton("https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-ftw3-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444444.p?skuId=6444444")
seventh = gpubutton("https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439299.p?skuId=6439299")
eigth = gpubutton("https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400")
ninth = gpubutton("https://www.bestbuy.com/site/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6434198.p?skuId=6434198")
tenth = gpubutton("https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3060-ventus-3x-12g-oc-12gb-gddr6-pci-express-4-0-graphics-card-black/6452940.p?skuId=6452940")
eleventh = gpubutton("https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3060-ventus-3x-12g-oc-12gb-gddr6-pci-express-4-0-graphics-card-black/6452940.p?skuId=6452940")
twelfth = gpubutton("https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3070-ventus-3x-oc-bv-8gb-gddr6-pci-express-4-0-graphics-card/6438278.p?skuId=6438278")
thirteenth = gpubutton("https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3080-ventus-3x-10g-oc-bv-gddr6x-pci-express-4-0-graphic-card-black-silver/6430175.p?skuId=6430175")
fourteenth = gpubutton("https://www.bestbuy.com/site/msi-amd-radeon-rx-6900-xt-16g-gddr6-pci-express-4-0-graphics-card-black-silver/6444716.p?skuId=6444716")
first.buttonplace("3060ti", 0.025,0.1, '~$399')
second.buttonplace("3070", 0.025,0.2, '~$499')
third.buttonplace("3080", 0.025,0.3, '~$699')
fourth.buttonplace("3090", 0.025,0.4, '~$1499')
fifth.buttonplace("3060", 0.29,0.1, '~$389')
sixth.buttonplace("3060ti", 0.29,0.2, '~$499')
seventh.buttonplace("3070", 0.29,0.3, '~$629')
eigth.buttonplace("3080", 0.29,0.4,'~$879')
ninth.buttonplace("3090", 0.29,0.5, '~$1699')
tenth.buttonplace("3060", .56, 0.1, "~$499")
eleventh.buttonplace("3060ti", .56, 0.2, "~$579")
twelfth.buttonplace("3070", .56, 0.3, "~$749")
thirteenth.buttonplace("3080", .56, 0.4, "~$1069")
fourteenth.buttonplace("6900xt", .56, 0.5, "~$999")
allbuttons = [first, second, third, fourth, fifth, sixth, seventh, eigth, ninth,tenth,eleventh,twelfth,thirteenth,fourteenth]

def runscalp():
    for i in range(0, increment):
        if allbuttons[i].is_off == False:
            thread = Thread(target = allbuttons[i].start, args=(allbuttons[i].link,entry1.get(), entry2.get(),))
            thread.start()
            while not allbuttons[i].flag:
                pass
            
root.mainloop()