import math
import tkinter

app = tkinter.Tk()
app.title('Price Calculator')

price_front = 26 # (฿)
gp = 30 # (%)
vat = 7 # (%)
gp_vat = gp+(gp*(vat/100)) # (%)

def start():
    return math.ceil((price_front/(100-gp_vat))*100)

print(start())
