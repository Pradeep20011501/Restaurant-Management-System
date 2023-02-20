from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

#functions

def reset():
    textreceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_sabji.set('0')
    e_kabab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_roohafza.set('0')
    e_tea.set('0')
    e_badam.set('0')
    e_cold.set('0')

    e_oreo.set('0')
    e_apple.set('0')
    e_kit.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pine.set('0')
    e_choco.set('0')
    e_black.set('0')

    roti.config(state=DISABLED)
    daal.config(state=DISABLED)
    fish.config(state=DISABLED)
    sabji.config(state=DISABLED)
    kabab.config(state=DISABLED)
    chawal.config(state=DISABLED)
    mutton.config(state=DISABLED)
    paneer.config(state=DISABLED)
    chicken.config(state=DISABLED)
    
    lassi.config(state=DISABLED)
    coffee.config(state=DISABLED)
    faluda.config(state=DISABLED)
    shikanji.config(state=DISABLED)
    jaljeera.config(state=DISABLED)
    roohafza.config(state=DISABLED)
    masalatea.config(state=DISABLED)
    badammilk.config(state=DISABLED)
    colddrinks.config(state=DISABLED)
    
    oreo.config(state=DISABLED)
    apple.config(state=DISABLED)
    kit.config(state=DISABLED)
    vanilla.config(state=DISABLED)
    banana.config(state=DISABLED)
    brownie.config(state=DISABLED)
    pine.config(state=DISABLED)
    choco.config(state=DISABLED)
    black.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    foodcostvar.set('')
    drinkscostvar.set('')
    cakescostvar.set('')
    subtotalvar.set('')
    taxvar.set('')
    totalvar.set('')

    


def send():
    if textreceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='06zQTYGlhgK93SCFduDP7vMsrqn1JWILwpfyExVHabUBteZmc8qIJOSiMLWGvaHuzDBYA0VETbrfk8nt'
            url='https://www.fast2sms.com/dev/bulk'

            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result == True:
                messagebox.showinfo('Sent Successfully','Message Sent Successfully')
                
            else:
                messagebox.showerror('error','Something went Wrong')

        root2=Toplevel()
        root2.title("Send Bill")
        root2.config(bg="red4")
        root2.geometry('485x620+50+50')

        logoimage=PhotoImage(file='wallpaper1.png')
        label=Label(root2,image=logoimage)
        label.pack(pady=5)

        numberlabel=Label(root2,text="Mobile Number",font=('arial',18,'bold underline'),bg='red4',fg='white')
        numberlabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        billlabel=Label(root2,text="Bill Details",font=('arial',18,'bold underline'),bg='red4',fg='white')
        billlabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')
        
        if foodcostvar.get()!='0 Rs':
            textarea.insert(END,f'Cost Of Food\t\t\t{foodcost}Rs\n')
        if drinkscostvar.get()!='0 Rs':
            textarea.insert(END,f'Cost Of Drinks\t\t\t{drinkscost}Rs\n')
        if cakescostvar.get()!='0 Rs':
            textarea.insert(END,f'Cost Of Cakes\t\t\t{cakescost}Rs\n')

        textarea.insert(END,f'Sub Total\t\t\t{subtotal}Rs\n')
        textarea.insert(END,f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END,f'Total Cost\t\t\t{subtotal+50}Rs\n')

        sendbutton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_msg)
        sendbutton.pack(pady=5)
        
        

        root2.mainloop()

def save():
    if textreceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data=textreceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            message.showinfo('Information','Your Bill Is Successfully Saved')

def bill():
    global billnumber
    global date
    if  foodcostvar.get()!='' or drinkscostvar.get()!='' or cakescostvar.get()!='':
        textreceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL: '+str(x)
        date=time.strftime('%d/%m/%Y')
        textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textreceipt.insert(END,'***************************************************************\n')
        textreceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textreceipt.insert(END,'***************************************************************\n')
        if e_roti.get()!='0':
            textreceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')
        if e_daal.get()!='0':
            textreceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')
        if e_fish.get()!='0':
            textreceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')
        if e_sabji.get()!='0':
            textreceipt.insert(END,f'Sabji\t\t\t{int(e_sabji.get())*50}\n\n')
        if e_kabab.get()!='0':
            textreceipt.insert(END,f'Kabab\t\t\t{int(e_kabab.get())*40}\n\n')
        if e_chawal.get()!='0':
            textreceipt.insert(END,f'Chawal\t\t\t{int(e_chawal.get())*30}\n\n')
        if e_mutton.get()!='0':
            textreceipt.insert(END,f'Mutton\t\t\t{int(e_mutton.get())*120}\n\n')
        if e_paneer.get()!='0':
            textreceipt.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*100}\n\n')
        if e_chicken.get()!='0':
            textreceipt.insert(END,f'Chicken\t\t\t{int(e_chicken.get())*120}\n\n')
            
        if e_lassi.get()!='0':
            textreceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*50}\n\n')
        if e_coffee.get()!='0':
            textreceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*60}\n\n')
        if e_faluda.get()!='0':
            textreceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*60}\n\n')
        if e_shikanji.get()!='0':
            textreceipt.insert(END,f'Shikanji\t\t\t{int(e_shikanji.get())*40}\n\n')
        if e_jaljeera.get()!='0':
            textreceipt.insert(END,f'Jaljeera\t\t\t{int(e_jaljeera.get())*30}\n\n')
        if e_roohafza.get()!='0':
            textreceipt.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*50}\n\n')
        if e_tea.get()!='0':
            textreceipt.insert(END,f'Masala Tea\t\t\t{int(e_tea.get())*10}\n\n')
        if e_badam.get()!='0':
            textreceipt.insert(END,f'Badam Milk\t\t\t{int(e_badam.get())*60}\n\n')
        if e_cold.get()!='0':
            textreceipt.insert(END,f'Cold Drinks\t\t\t{int(e_cold.get())*15}\n\n')
            
        if e_oreo.get()!='0':
            textreceipt.insert(END,f'Oreo\t\t\t{int(e_oreo.get())*400}\n\n')
        if e_apple.get()!='0':
            textreceipt.insert(END,f'Apple\t\t\t{int(e_apple.get())*300}\n\n')
        if e_kit.get()!='0':
            textreceipt.insert(END,f'Kit Kat\t\t\t{int(e_kit.get())*400}\n\n')
        if e_vanilla.get()!='0':
            textreceipt.insert(END,f'Vanilla\t\t\t{int(e_vanilla.get())*440}\n\n')
        if e_banana.get()!='0':
            textreceipt.insert(END,f'Banana\t\t\t{int(e_banana.get())*300}\n\n')
        if e_brownie.get()!='0':
            textreceipt.insert(END,f'Brownie\t\t\t{int(e_brownie.get())*400}\n\n')
        if e_pine.get()!='0':
            textreceipt.insert(END,f'Pine Apple\t\t\t{int(e_pine.get())*350}\n\n')
        if e_choco.get()!='0':
            textreceipt.insert(END,f'Chocolate\t\t\t{int(e_choco.get())*600}\n\n')
        if e_black.get()!='0':
            textreceipt.insert(END,f'Black Forest\t\t\t{int(e_black.get())*650}\n\n')

        textreceipt.insert(END,'***************************************************************\n')
        if foodcostvar.get()!='0 Rs':
            textreceipt.insert(END,f'Cost Of Food\t\t\t{foodcost}Rs\n\n')
        if drinkscostvar.get()!='0 Rs':
            textreceipt.insert(END,f'Cost Of Drinks\t\t\t{drinkscost}Rs\n\n')
        if cakescostvar.get()!='0 Rs':
            textreceipt.insert(END,f'Cost Of Cakes\t\t\t{cakescost}Rs\n\n')

        textreceipt.insert(END,f'Sub Total\t\t\t{subtotal}Rs\n\n')
        textreceipt.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
        textreceipt.insert(END,f'Total Cost\t\t\t{subtotal+50}Rs\n\n')
        textreceipt.insert(END,'***************************************************************\n')
    else:
        messagebox.showerror('Error','No item is selected')
    
        

def totalcost():
    global foodcost,drinkscost,cakescost,subtotal,totalcost
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 or var7.get()!=0 or \
       var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 \
       or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0 or var21.get()!=0 \
       or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or var26.get()!=0 or var27.get()!=0:
        item1=int(e_roti.get())
        item2=int(e_daal.get())
        item3=int(e_fish.get())
        item4=int(e_sabji.get())
        item5=int(e_kabab.get())
        item6=int(e_chawal.get())
        item7=int(e_mutton.get())
        item8=int(e_paneer.get())
        item9=int(e_chicken.get())
        
        item10=int(e_lassi.get())
        item11=int(e_coffee.get())
        item12=int(e_faluda.get())
        item13=int(e_shikanji.get())
        item14=int(e_jaljeera.get())
        item15=int(e_roohafza.get())
        item16=int(e_tea.get())
        item17=int(e_badam.get())
        item18=int(e_cold.get())
        
        item19=int(e_oreo.get())
        item20=int(e_apple.get())
        item21=int(e_kit.get())
        item22=int(e_vanilla.get())
        item23=int(e_banana.get())
        item24=int(e_brownie.get())
        item25=int(e_pine.get())
        item26=int(e_choco.get())
        item27=int(e_black.get())

        foodcost=(item1*10)+(item2*60)+(item3*100)+(item4*50)+(item5*40)+(item6*30)+(item7*120)+(item8*100)+(item9*120)

        drinkscost=(item10*50)+(item11*60)+(item12*60)+(item13*40)+(item14*30)+(item15*50)+(item16*10)+(item17*60)+(item18*15)

        cakescost=(item19*400)+(item20*300)+(item21*400)+(item22*440)+(item23*300)+(item24*400)+(item25*350)+(item26*600)+(item27*650)

        foodcostvar.set(str(foodcost)+ ' Rs')
        drinkscostvar.set(str(drinkscost)+ ' Rs')
        cakescostvar.set(str(cakescost)+ ' Rs')

        subtotal=foodcost+drinkscost+cakescost
        subtotalvar.set(str(subtotal)+ ' Rs')

        taxvar.set(str('50 Rs'))

        totalcost=subtotal+50
        totalvar.set(str(totalcost)+' Rs')
    else:
        messagebox.showerror('Error','No item is selected')
    

   
def roti():
    if var1.get()==1:
        roti.config(state=NORMAL)
        roti.delete(0,END)
        roti.focus()
    else:
        roti.config(state=DISABLED)
        e_roti.set("0")

def daal():
    if var2.get()==1:
        daal.config(state=NORMAL)
        daal.delete(0,END)
        daal.focus()
    else:
        daal.config(state=DISABLED)
        e_daal.set("0")

def fish():
    if var3.get()==1:
        fish.config(state=NORMAL)
        fish.delete(0,END)
        fish.focus()
    else:
        fish.config(state=DISABLED)
        e_fish.set("0")

def sabji():
    if var4.get()==1:
        sabji.config(state=NORMAL)
        sabji.delete(0,END)
        sabji.focus()
    else:
        sabji.config(state=DISABLED)
        e_sabji.set("0")

def kabab():
    if var5.get()==1:
        kabab.config(state=NORMAL)
        kabab.delete(0,END)
        kabab.focus()
    else:
        kabab.config(state=DISABLED)
        e_kabab.set("0")

def chawal():
    if var6.get()==1:
        chawal.config(state=NORMAL)
        chawal.delete(0,END)
        chawal.focus()
    else:
        chawal.config(state=DISABLED)
        e_chawal.set("0")

def mutton():
    if var7.get()==1:
        mutton.config(state=NORMAL)
        mutton.delete(0,END)
        mutton.focus()
    else:
        mutton.config(state=DISABLED)
        e_mutton.set("0")

def paneer():
    if var8.get()==1:
        paneer.config(state=NORMAL)
        paneer.delete(0,END)
        paneer.focus()
    else:
        paneer.config(state=DISABLED)
        e_paneer.set("0")

def chicken():
    if var9.get()==1:
        chicken.config(state=NORMAL)
        chicken.delete(0,END)
        chicken.focus()
    else:
        chicken.config(state=DISABLED)
        e_chicken.set("0")

def lassi():
    if var10.get()==1:
        lassi.config(state=NORMAL)
        lassi.delete(0,END)
        lassi.focus()
    else:
        lassi.config(state=DISABLED)
        e_lassi.set("0")

def coffee():
    if var11.get()==1:
        coffee.config(state=NORMAL)
        coffee.delete(0,END)
        coffee.focus()
    else:
        coffee.config(state=DISABLED)
        e_coffee.set("0")

def faluda():
    if var12.get()==1:
        faluda.config(state=NORMAL)
        faluda.delete(0,END)
        faluda.focus()
    else:
        faluda.config(state=DISABLED)
        e_faluda.set("0")

def shikanji():
    if var13.get()==1:
        shikanji.config(state=NORMAL)
        shikanji.delete(0,END)
        shikanji.focus()
    else:
        shikanji.config(state=DISABLED)
        e_shikanji.set("0")

def jaljeera():
    if var14.get()==1:
        jaljeera.config(state=NORMAL)
        jaljeera.delete(0,END)
        jaljeera.focus()
    else:
        jaljeera.config(state=DISABLED)
        e_jaljeera.set("0")

def roohafza():
    if var15.get()==1:
        roohafza.config(state=NORMAL)
        roohafza.delete(0,END)
        roohafza.focus()
    else:
        roohafza.config(state=DISABLED)
        e_roohafza.set("0")

def masalatea():
    if var16.get()==1:
        masalatea.config(state=NORMAL)
        masalatea.delete(0,END)
        masalatea.focus()
    else:
        masalatea.config(state=DISABLED)
        e_masalatea.set("0")

def badammilk():
    if var17.get()==1:
        badammilk.config(state=NORMAL)
        badammilk.delete(0,END)
        badammilk.focus()
    else:
        badammilk.config(state=DISABLED)
        e_badammilk.set("0")

def colddrinks():
    if var18.get()==1:
        colddrinks.config(state=NORMAL)
        colddrinks.delete(0,END)
        colddrinks.focus()
    else:
        colddrinks.config(state=DISABLED)
        e_colddrinks.set("0")

def oreo():
    if var19.get()==1:
        oreo.config(state=NORMAL)
        oreo.delete(0,END)
        oreo.focus()
    else:
        oreo.config(state=DISABLED)
        e_oreo.set("0")

def apple():
    if var20.get()==1:
        apple.config(state=NORMAL)
        apple.delete(0,END)
        apple.focus()
    else:
        apple.config(state=DISABLED)
        e_apple.set("0")

def kit():
    if var21.get()==1:
        kit.config(state=NORMAL)
        kit.delete(0,END)
        kit.focus()
    else:
        kit.config(state=DISABLED)
        e_kit.set("0")

def vanilla():
    if var22.get()==1:
        vanilla.config(state=NORMAL)
        vanilla.delete(0,END)
        vanilla.focus()
    else:
        vanilla.config(state=DISABLED)
        e_vanilla.set("0")

def banana():
    if var23.get()==1:
        banana.config(state=NORMAL)
        banana.delete(0,END)
        banana.focus()
    else:
        banana.config(state=DISABLED)
        e_banana.set("0")

def brownie():
    if var24.get()==1:
        brownie.config(state=NORMAL)
        brownie.delete(0,END)
        brownie.focus()
    else:
        brownie.config(state=DISABLED)
        e_brownie.set("0")

def pine():
    if var25.get()==1:
        pine.config(state=NORMAL)
        pine.delete(0,END)
        pine.focus()
    else:
        pine.config(state=DISABLED)
        e_pine.set("0")

def choco():
    if var26.get()==1:
        choco.config(state=NORMAL)
        choco.delete(0,END)
        choco.focus()
    else:
        choco.config(state=DISABLED)
        e_choco.set("0")

def black():
    if var27.get()==1:
        black.config(state=NORMAL)
        black.delete(0,END)
        black.focus()
    else:
        black.config(state=DISABLED)
        e_black.set("0")

        
root=Tk()

root.geometry("1270x690+0+0")

root.resizable(0,0)
root.title("Restaurant Management System")
root.config(bg="firebrick4")

topFrame=Frame(root,bd=10,relief=RIDGE,bg="firebrick4")
topFrame.pack(side=TOP)

labeltitle=Label(topFrame,text="Restaurent Management System",font=('arial',30,'bold'),fg="yellow",bg="red4",width=51,bd=9)
labeltitle.grid(row=0,column=0)

#frames

menuframe=Frame(root,bd=10,relief=RIDGE,bg="firebrick4")
menuframe.pack(side=LEFT)

costframe=Frame(menuframe,bd=4,relief=RIDGE,bg="firebrick4",pady=10)
costframe.pack(side=BOTTOM)

foodframe=LabelFrame(menuframe,text="Food",font=("arial",19,'bold'),bd=10,relief=RIDGE,fg="red4")
foodframe.pack(side=LEFT)

drinkframe=LabelFrame(menuframe,text="Drinks",font=("arial",19,'bold'),bd=10,relief=RIDGE,fg="red4")
drinkframe.pack(side=LEFT)

cakesframe=LabelFrame(menuframe,text="Cakes",font=("arial",19,'bold'),bd=10,relief=RIDGE,fg="red4")
cakesframe.pack(side=LEFT)

rightframe=Frame(root,bd=15,relief=RIDGE,bg="red4")
rightframe.pack(side=RIGHT)

calci=Frame(rightframe,bd=1,relief=RIDGE,bg="red4")
calci.pack()

receipt=Frame(rightframe,bd=4,relief=RIDGE,bg="red4")
receipt.pack()

button=Frame(rightframe,bd=3,relief=RIDGE,bg="red4")
button.pack()

#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_sabji=StringVar()
e_kabab=StringVar()
e_chawal=StringVar()
e_mutton=StringVar()
e_paneer=StringVar()
e_chicken=StringVar()

e_lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_jaljeera=StringVar()
e_roohafza=StringVar()
e_tea=StringVar()
e_badam=StringVar()
e_cold=StringVar()

e_oreo=StringVar()
e_apple=StringVar()
e_kit=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_brownie=StringVar()
e_pine=StringVar()
e_choco=StringVar()
e_black=StringVar()

foodcostvar=StringVar()
drinkscostvar=StringVar()
cakescostvar=StringVar()
subtotalvar=StringVar()
taxvar=StringVar()
totalvar=StringVar()

e_roti.set("0")
e_daal.set("0")
e_fish.set("0")
e_sabji.set("0")
e_kabab.set("0")
e_chawal.set("0")
e_mutton.set("0")
e_paneer.set("0")
e_chicken.set("0")

e_lassi.set("0")
e_coffee.set("0")
e_faluda.set("0")
e_shikanji.set("0")
e_jaljeera.set("0")
e_roohafza.set("0")
e_tea.set("0")
e_badam.set("0")
e_cold.set("0")

e_oreo.set("0")
e_apple.set("0")
e_kit.set("0")
e_vanilla.set("0")
e_banana.set("0")
e_brownie.set("0")
e_pine.set("0")
e_choco.set("0")
e_black.set("0")

#food
roti=Checkbutton(foodframe,text="Roti",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodframe,text="Daal",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodframe,text="Fish",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodframe,text="Sabji",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

kabab=Checkbutton(foodframe,text="Kabab",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=kabab)
kabab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodframe,text="Chawal",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodframe,text="Mutton",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(foodframe,text="Paneer",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodframe,text="Chicken",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

#entry fields
roti=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
roti.grid(row=0,column=1)

daal=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
daal.grid(row=1,column=1)

fish=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
fish.grid(row=2,column=1)

sabji=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sabji)
sabji.grid(row=3,column=1)

kabab=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kabab)
kabab.grid(row=4,column=1)

chawal=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chawal)
chawal.grid(row=5,column=1)

mutton=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
mutton.grid(row=6,column=1)

paneer=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
paneer.grid(row=7,column=1)

chicken=Entry(foodframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
chicken.grid(row=8,column=1)

#drinks
lassi=Checkbutton(drinkframe,text="Lassi",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinkframe,text="Coffee",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinkframe,text="Faluda",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinkframe,text="Shikanji",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

jaljeera=Checkbutton(drinkframe,text="Jaljeera",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=jaljeera)
jaljeera.grid(row=4,column=0,sticky=W)

roohafza=Checkbutton(drinkframe,text="Roohafza",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=roohafza)
roohafza.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinkframe,text="Masala Tea",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=masalatea)
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinkframe,text="Badam Milk",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=badammilk)
badammilk.grid(row=7,column=0,sticky=W)

colddrinks=Checkbutton(drinkframe,text="Cold Drinks",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=colddrinks)
colddrinks.grid(row=8,column=0,sticky=W)

#entry fields
lassi=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
lassi.grid(row=0,column=1,sticky=W)

coffee=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
coffee.grid(row=1,column=1,sticky=W)

faluda=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
faluda.grid(row=2,column=1,sticky=W)

shikanji=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shikanji)
shikanji.grid(row=3,column=1,sticky=W)

jaljeera=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jaljeera)
jaljeera.grid(row=4,column=1,sticky=W)

roohafza=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
roohafza.grid(row=5,column=1,sticky=W)

masalatea=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
masalatea.grid(row=6,column=1,sticky=W)

badammilk=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_badam)
badammilk.grid(row=7,column=1,sticky=W)

colddrinks=Entry(drinkframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cold)
colddrinks.grid(row=8,column=1,sticky=W)

#cakes
oreo=Checkbutton(cakesframe,text="Oreo",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreo)
oreo.grid(row=0,column=0,sticky=W)

apple=Checkbutton(cakesframe,text="Apple",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=apple)
apple.grid(row=1,column=0,sticky=W)

kit=Checkbutton(cakesframe,text="KitKat",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=kit)
kit.grid(row=3,column=0,sticky=W)

vanilla=Checkbutton(cakesframe,text="Vanilla",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanilla)
vanilla.grid(row=4,column=0,sticky=W)

banana=Checkbutton(cakesframe,text="Banana",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=banana)
banana.grid(row=5,column=0,sticky=W)

brownie=Checkbutton(cakesframe,text="Brownie",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=brownie)
brownie.grid(row=6,column=0,sticky=W)

pine=Checkbutton(cakesframe,text="PineApple",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=pine)
pine.grid(row=7,column=0,sticky=W)

choco=Checkbutton(cakesframe,text="Chocolate",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=choco)
choco.grid(row=8,column=0,sticky=W)

black=Checkbutton(cakesframe,text="Black Forest",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=black)
black.grid(row=9,column=0,sticky=W)

#entry cakes
oreo=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
oreo.grid(row=0,column=1,sticky=W)

apple=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
apple.grid(row=1,column=1,sticky=W)

kit=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kit)
kit.grid(row=3,column=1,sticky=W)

vanilla=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
vanilla.grid(row=4,column=1,sticky=W)

banana=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
banana.grid(row=5,column=1,sticky=W)

brownie=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
brownie.grid(row=6,column=1,sticky=W)

pine=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pine)
pine.grid(row=7,column=1,sticky=W)

choco=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_choco)
choco.grid(row=8,column=1,sticky=W)

black=Entry(cakesframe,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_black)
black.grid(row=9,column=1,sticky=W)

#costlabels and entry
labelcostoffood=Label(costframe,text="Cost of Food",font=('arial',16,'bold'),bg="firebrick4",fg="white")
labelcostoffood.grid(row=0,column=0)

textfood=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state="readonly",textvariable=foodcostvar)
textfood.grid(row=0,column=1,padx=41)

labelcostofdrinks=Label(costframe,text="Cost of Drinks",font=('arial',16,'bold'),bg="firebrick4",fg="white")
labelcostofdrinks.grid(row=1,column=0)

textdrinks=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state="readonly",textvariable=drinkscostvar)
textdrinks.grid(row=1,column=1,padx=41)

labelcostofcakes=Label(costframe,text="Cost of Cakes",font=('arial',16,'bold'),bg="firebrick4",fg="white")
labelcostofcakes.grid(row=2,column=0)

textcakes=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state="readonly",textvariable=cakescostvar)
textcakes.grid(row=2,column=1,padx=41)

labelsubtotal=Label(costframe,text="Sub Total",font=('arial',16,'bold'),bg="firebrick4",fg="white")
labelsubtotal.grid(row=0,column=2)

textsubtotal=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state="readonly",textvariable=subtotalvar)
textsubtotal.grid(row=0,column=3,padx=41)

labelservice=Label(costframe,text="Service Tax",font=('arial',16,'bold'),bg="firebrick4",fg="white")
labelservice.grid(row=1,column=2)

textservice=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state="readonly",textvariable=taxvar)
textservice.grid(row=1,column=3,padx=41)

labeltotal=Label(costframe,text="Total Cost",font=('arial',16,'bold'),bg="firebrick4",fg="white")
labeltotal.grid(row=2,column=2)

texttotal=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state="readonly",textvariable=totalvar)
texttotal.grid(row=2,column=3,padx=41)

#buttons

buttontotal=Button(button,text="Total",font=('arial',14,'bold'),fg="white",bg="red4",bd=3,padx=5,command=totalcost)
buttontotal.grid(row=0,column=0)

buttonreceipt=Button(button,text="Receipt",font=('arial',14,'bold'),fg="white",bg="red4",bd=3,padx=5,command=bill)
buttonreceipt.grid(row=0,column=1)

buttonsave=Button(button,text="Save",font=('arial',14,'bold'),fg="white",bg="red4",bd=3,padx=5,command=save)
buttonsave.grid(row=0,column=2)

buttonsend=Button(button,text="Send",font=('arial',14,'bold'),fg="white",bg="red4",bd=3,padx=5,command=send)
buttonsend.grid(row=0,column=3)

buttonreset=Button(button,text="Reset",font=('arial',14,'bold'),fg="white",bg="red4",bd=3,padx=5,command=reset)
buttonreset.grid(row=0,column=4)

#text area for receipt
textreceipt=Text(receipt,font=('arial',12,'bold'),bd=3,width=42,height=14)
textreceipt.grid(row=0)

#calculator
operator=""
def buttonclick(num):
    global operator
    operator+=num
    calculatorfield.delete(0,END)
    calculatorfield.insert(END,operator)

def answer():
    global operator
    result=str(eval(operator))
    calculatorfield.delete(0,END)
    calculatorfield.insert(0,result)
    operator=""
    
def clear():
    global operator
    operator=""
    calculatorfield.delete(0,END)
    

calculatorfield=Entry(calci,font=('arial',16,"bold"),width=32,bd=4)
calculatorfield.grid(row=0,column=0,columnspan=4)

button7=Button(calci,text="7",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calci,text="8",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calci,text="9",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calci,text="+",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calci,text="4",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calci,text="5",font=('arial',16,"bold"),fg="red4",bg="white",bd=6,width=6,command=lambda:buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calci,text="6",font=('arial',16,"bold"),fg="red4",bg="white",bd=6,width=6,command=lambda:buttonclick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calci,text="-",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calci,text="1",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calci,text="2",font=('arial',16,"bold"),fg="red4",bg="white",bd=6,width=6,command=lambda:buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calci,text="3",font=('arial',16,"bold"),fg="red4",bg="white",bd=6,width=6,command=lambda:buttonclick('3'))
button3.grid(row=3,column=2)

buttonmulti=Button(calci,text="*",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('*'))
buttonmulti.grid(row=3,column=3)

buttonans=Button(calci,text="Ans",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=answer)
buttonans.grid(row=4,column=0)

buttonclear=Button(calci,text="Clear",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calci,text="0",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('0'))
button0.grid(row=4,column=2)

buttondivide=Button(calci,text="/",font=('arial',16,"bold"),fg="yellow",bg="red4",bd=6,width=6,command=lambda:buttonclick('/'))
buttondivide.grid(row=4,column=3)

root.mainloop()
