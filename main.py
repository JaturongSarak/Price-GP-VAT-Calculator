import tkinter

App = tkinter.Tk()
App.title('Price Calculator')

# Label
gp_label = tkinter.Label(App, text='+ GP (%)')
vat_label = tkinter.Label(App, text='+ VAT (%)')
price_label = tkinter.Label(App, text='Price')
best_label = tkinter.Label(App, text='Recommend')
best_label2 = tkinter.Label(App, text='')

gp_label.grid(column=0, row=0, padx=10, pady=5)
vat_label.grid(column=0, row=1, padx=10, pady=5)
price_label.grid(column=0, row=2, padx=10, pady=5)
best_label.grid(column=0, row=3, padx=10, pady=5)
best_label2.grid(column=1, row=3, padx=10, pady=5)

# Entry
gp_entry = tkinter.Entry(App)
vat_entry = tkinter.Entry(App)
price_entry = tkinter.Entry(App)

gp_entry.grid(column=1, row=0, padx=10, pady=5)
vat_entry.grid(column=1, row=1, padx=10, pady=5)
price_entry.grid(column=1, row=2, padx=10, pady=5)


#App
def start():
    gp = float(gp_entry.get())
    vat = float(vat_entry.get())
    price = float(price_entry.get())
    
    gp_vat = (gp+(gp*(vat/100)))/100
    best_price = price
    while best_price-(best_price*gp_vat) < price:
        best_price+=1
    best_label2.config(text=best_price)

#Button
calculate_button = tkinter.Button(App, text='Calculate', command=start)

calculate_button.grid(column=2, row=1, padx=10, pady=5, ipadx=5)

App.mainloop()