import tkinter as tk
from tkinter import messagebox

users = [
    {"Login": "John", "Password": "1", "Balance": 100},
    {"Login": "James", "Password": "4", "Balance": 1000}
]
balance = 0
iphone = 0
island = 0
car = 0
house = 0
helicopter = 0
yacht = 0

root = tk.Tk()
root.title("Step Bank")
root.geometry("400x400+200+300")


# Функции
# ======================================================================================================================
def addtocart(label1, label2, labelobject, price):
    label1.config(text=int(label1['text']) + price)
    label2.config(text=int(label2['text']) - price)
    labelobject.config(text=int(labelobject['text']) + 1)


# countpay, balance, countitem, price

def checkin(log, password, confirm, mon):
    for i in users:
        if i["Login"] == log:
            messagebox.showinfo("Username ERROR", "User Exists")
            return
        if password != confirm:
            messagebox.showinfo("Password ERROR", "Passwords don't match")
            return
    new_user = {"Login": log, "Password": password, "Balance": mon}
    users.append(new_user)
    messagebox.showinfo("Info", "User added!")


def reg():
    regWindow = tk.Toplevel(root)
    regWindow.title("Registry Window")
    regWindow.geometry("300x300+600+300")

    login1 = tk.StringVar()
    login1_entry = tk.Entry(regWindow, textvariable=login1)
    login1_entry.place(x=50, y=50)

    password1 = tk.StringVar()
    password1_entry = tk.Entry(regWindow, textvariable=password1,
                               show="*")
    password1_entry.place(x=50, y=75)

    confirm_password = tk.StringVar()
    confirm_password_entry = tk.Entry(regWindow, textvariable=confirm_password,
                                      show="*")
    confirm_password_entry.place(x=50, y=100)

    money1 = tk.StringVar()
    money1_entry = tk.Entry(regWindow, textvariable=money1)
    money1_entry.place(x=50, y=150)

    add = tk.Button(regWindow, text="Add user",
                    command=lambda: checkin(login1.get(), password1.get(), confirm_password.get(),
                                            money1.get()))
    add.place(x=50, y=250)


def store():
    global balance
    for i in users:
        if login.get() == i['Login'] and enterpass.get() == i['Password']:
            balance = i["Balance"]
            break
        elif users.index(i) == len(users) - 1:
            messagebox.showinfo("Info", "Wrong Password or Name!")
            return
    storeWindow = tk.Toplevel(root)
    storeWindow.title("Store")
    storeWindow.geometry("1500x700")
    for i in users:
        if login.get() == i['Login']:
            balance = i["Balance"]
        else:
            balance = 0

    iphone_button = tk.Button(storeWindow, text="iPhone: 1500",
                              height="4",
                              width="10",
                              command=lambda: addtocart(countpay, cash, countiphone, 1500)
                              )
    iphone_button.place(x=25, y=150)

    island_button = tk.Button(storeWindow, text="Island: 4500",
                              height="4",
                              width="10",
                              command=lambda: addtocart(countpay, cash, countisland, 4500)
                              )
    island_button.place(x=150, y=150)

    car_button = tk.Button(storeWindow, text="Car: 25000",
                           height="4",
                           width="10",
                           command=lambda: addtocart(countpay, cash, countcar, 25000)
                           )
    car_button.place(x=275, y=150)

    house_button = tk.Button(storeWindow, text="House: 500000",
                             height="4",
                             width="10",
                             command=lambda: addtocart(countpay, cash, counthouse, 500000)
                             )
    house_button.place(x=25, y=250)

    heli_button = tk.Button(storeWindow, text="Helicopter: 200000",
                            height="4",
                            width="13",
                            command=lambda: addtocart(countpay, cash, counthelicopter, 200000)
                            )
    heli_button.place(x=140, y=250)

    yacht_button = tk.Button(storeWindow, text="Yacht: 400000",
                             height="4",
                             width="10",
                             command=lambda: addtocart(countpay, cash, countyacht, 400000)
                             )
    yacht_button.place(x=275, y=250)
    # ==================================================================================================================
    cash = tk.Label(storeWindow,
                    text=balance,
                    padx="10",
                    pady="10",
                    font="50",
                    height="1",
                    width="10")
    cash.place(x=25, y=50)

    pay = tk.Label(storeWindow,
                   text="Sum:",
                   padx="10",
                   pady="10",
                   font="50",
                   height="1",
                   width="10"
                   )
    pay.place(x=350, y=600)

    countpay = tk.Label(storeWindow,
                        text=0,
                        padx="10",
                        pady="10",
                        font="50",
                        height="1",
                        width="10"
                        )
    countpay.place(x=425, y=600)

    labeliPhone = tk.Label(storeWindow,
                           text="iPhone:",
                           padx="10",
                           pady="10",
                           font="50",
                           height="1",
                           width="10")

    labeliPhone.place(x=50, y=400)

    labelIsland = tk.Label(storeWindow,
                           text="Island:",
                           padx="10",
                           pady="10",
                           font="50",
                           height="1",
                           width="10")
    labelIsland.place(x=50, y=440)

    labelCar = tk.Label(storeWindow,
                        text="Car:",
                        padx="10",
                        pady="10",
                        font="50",
                        height="1",
                        width="10")
    labelCar.place(x=50, y=480)

    labelHouse = tk.Label(storeWindow,
                          text="House:",
                          padx="10",
                          pady="10",
                          font="50",
                          height="1",
                          width="10")
    labelHouse.place(x=50, y=520)

    labelHeli = tk.Label(storeWindow,
                         text="Helicopter:",
                         padx="10",
                         pady="10",
                         font="50",
                         height="1",
                         width="10")
    labelHeli.place(x=50, y=560)

    labelYacht = tk.Label(storeWindow,
                          text="Yacht:",
                          padx="10",
                          pady="10",
                          font="50",
                          height="1",
                          width="10")
    labelYacht.place(x=50, y=600)

    countiphone = tk.Label(storeWindow,
                           text="0",
                           padx="10",
                           pady="10",
                           font="50",
                           height="1",
                           width="10")
    countiphone.place(x=150, y=400)

    countisland = tk.Label(storeWindow,
                           text="0",
                           padx="10",
                           pady="10",
                           font="50",
                           height="1",
                           width="10")
    countisland.place(x=150, y=440)

    countcar = tk.Label(storeWindow,
                        text="0",
                        padx="10",
                        pady="10",
                        font="50",
                        height="1",
                        width="10")
    countcar.place(x=150, y=480)

    counthouse = tk.Label(storeWindow,
                          text="0",
                          padx="10",
                          pady="10",
                          font="50",
                          height="1",
                          width="10")
    counthouse.place(x=150, y=520)

    counthelicopter = tk.Label(storeWindow,
                               text="0",
                               padx="10",
                               pady="10",
                               font="50",
                               height="1",
                               width="10")
    counthelicopter.place(x=150, y=560)

    countyacht = tk.Label(storeWindow,
                          text="0",
                          padx="10",
                          pady="10",
                          font="50",
                          height="1",
                          width="10")
    countyacht.place(x=150, y=600)


# ======================================================================================================================

login_button = tk.Button(root, text="Log in",
                         command=store)
login_button.place(x=50, y=150)

register_button = tk.Button(root, text="Register",
                            command=reg)
register_button.place(x=100, y=150)

login = tk.StringVar()
login_entry = tk.Entry(root, textvariable=login)
login_entry.place(x=50, y=50)

enterpass = tk.StringVar()
enterpass_entry = tk.Entry(root, textvariable=enterpass,
                           show="*")
enterpass_entry.place(x=50, y=75)

root.mainloop()
