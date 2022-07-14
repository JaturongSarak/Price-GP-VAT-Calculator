import math
import tkinter

app = tkinter.Tk()
app.title('Price Calculator')

def start():
    price_front = int(price_entry.get()) # (฿)
    gp = int(gp_entry.get()) # (%)
    vat = int(vat_entry.get()) # (%)
    gp_vat = gp+(gp*(vat/100)) # (%)
    result_recommend_label.configure(text=math.ceil((price_front/(100-gp_vat))*100))

gp_label = tkinter.Label(app, text='GP (%) : ')
vat_label = tkinter.Label(app, text='VAT (%) : ')
price_label = tkinter.Label(app, text='Price (฿) : ')
recommend_label = tkinter.Label(app, text='Recommend (฿) : ')
result_recommend_label = tkinter.Label(app, text='')

gp_entry = tkinter.Entry(app)
vat_entry = tkinter.Entry(app)
price_entry = tkinter.Entry(app)

calculator_button = tkinter.Button(app, text='Calculate', command=start)

gp_label.grid(column=0, row=0, padx=5, pady=5)
vat_label.grid(column=0, row=1, padx=5, pady=5)
price_label.grid(column=0, row=2, padx=5, pady=5)
recommend_label.grid(column=0, row=3, padx=5, pady=5)
result_recommend_label.grid(column=1, row=3, padx=5, pady=5)

gp_entry.grid(column=1, row=0, padx=5)
vat_entry.grid(column=1, row=1, padx=5)
price_entry.grid(column=1, row=2, padx=5)

calculator_button.grid(column=2, row=1, padx=5)

app.mainloop()
