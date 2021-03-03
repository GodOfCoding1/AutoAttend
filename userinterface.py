import tkinter as tk
from tkinter import messagebox
import os
import gmeet
import webex
number = 0
allclassdetails=[]

def setup():
    root = tk.Tk()
    root.title("Set Up")
    root.geometry('250x180')
    messagebox.showinfo("Alert", "You have to go through this setup process only once.")
    messagebox.showinfo("Don't",
                        "Some actions like clicking join on google meet  has a delay of 10 seconds. Don't try to help the program by clciking join")
    messagebox.showinfo("Imp info",
                        "All classes are started with a delay of 2 minutes. Eg: if u set a class for 13:05 the program will attend the class only at 13:07.")
    tk.Label(root, text="Which platform").pack(padx=10, pady=5)

    tk.Button(root, text="WebEx", padx=15, pady=5, fg="black", bg="white", command=lambda: web(root)).pack(padx=10,
                                                                                                           pady=5)

    tk.Button(root, text="G-Meet", padx=15, pady=5, fg="black", bg="white", command=lambda: gm(root)).pack(padx=10,
                                                                                                           pady=5)

    tk.Button(root, text="Both", padx=15, pady=5, fg="black", bg="white", command=lambda: both(root)).pack(padx=10,
                                                                                                           pady=5)

    root.mainloop()


def web(root):
    root.destroy()
    root = tk.Tk()
    root.title("WebEx Set UP")

    tk.Label(root, text="Name :").grid(row=0, padx=10, pady=2.5)
    tk.Label(root, text="Email :").grid(row=1, padx=10, pady=2.5)

    name = tk.Entry(root)
    email = tk.Entry(root)

    name.grid(row=0, column=1)
    email.grid(row=1, column=1)
    tk.Button(root, text="Next", padx=15, pady=2.5, fg="black", bg="white",
              command=lambda: addtoweb(name.get(), email.get(), root)).grid(row=3, column=4, padx=5, pady=5)

    root.mainloop()


def gm(root):
    root.destroy()
    root = tk.Tk()
    root.title("G-Meet Set UP")
    cam=tk.StringVar()
    tk.Label(root, text="Gmail :").grid(row=0, padx=10, pady=2.5)
    tk.Label(root, text="Password :").grid(row=1, padx=10, pady=2.5)
    tk.Label(root, text="Do you have camera?").grid(row=2, column=0, padx=10, pady=2.5)

    gmail = tk.Entry(root)
    password = tk.Entry(root)
    tk.Checkbutton(root, text="Yes", var=cam, offvalue="", onvalue="YES").grid(row=2, column=1, padx=10,
                                                                                    pady=5)
    tk.Checkbutton(root, text="No", var=cam, offvalue="", onvalue="NO").grid(row=2, column=2, padx=10,
                                                                                      pady=5)
    gmail.grid(row=0, column=1)
    password.grid(row=1, column=1)
    tk.Button(root, text="Next", padx=15, pady=2.5, fg="black", bg="white",
              command=lambda: addtogm(gmail.get(), password.get(),cam.get() ,root)).grid(row=3, column=4, padx=5, pady=5)

    root.mainloop()


def gmboth():
    root = tk.Tk()
    root.title("G-Meet Set UP")

    cam = tk.StringVar()
    tk.Label(root, text="Gmail :").grid(row=0, padx=10, pady=2.5)
    tk.Label(root, text="Password :").grid(row=1, padx=10, pady=2.5)
    tk.Label(root, text="Do you have camera?").grid(row=2, column=0, padx=10, pady=2.5)

    gmail = tk.Entry(root)
    password = tk.Entry(root)
    tk.Checkbutton(root, text="Yes", var=cam, offvalue="", onvalue="YES").grid(row=2, column=1, padx=10,
                                                                               pady=5)
    tk.Checkbutton(root, text="No", var=cam, offvalue="", onvalue="NO").grid(row=2, column=2, padx=10,
                                                                             pady=5)
    gmail.grid(row=0, column=1)
    password.grid(row=1, column=1)
    tk.Button(root, text="Next", padx=15, pady=2.5, fg="black", bg="white",
              command=lambda: addtogm(gmail.get(), password.get(), cam.get(), root)).grid(row=3, column=4, padx=5,
                                                                                          pady=5)

    root.mainloop()


def addtoweb(name, email, root):
    root.destroy()

    with open("user_data/webex_mail_name.txt", "w") as f:
        f.write(f"{name}\n")
        f.write(f"{email}")


def addtogm(name, email,cam ,root):
    root.destroy()

    with open("user_data/gmeet_mail_password.txt", "w") as f:
        f.write(f"{name}\n")
        f.write(f"{email}\n")
        f.write(f"{cam}")


def both(root):
    web(root)
    gmboth()


def main():
    with open("user_data/firsttime.txt", "r+") as f:
        if f.readline() == "YES":
            setup()
            f.truncate(0)
        mainmenu()



def nextbuttonofdetails(root, nameoftt, day, plat, link, start, end):
    root.destroy()
    fileTT(nameoftt, day, plat, link, start, end)


def getnumber(root, number1):
    root.destroy()
    global number
    number = int(number1)


def getclassdetails(day, nameoftt):
    # getnumberof classes
    root = tk.Tk()
    root.title(f"Deatils of {day}")

    tk.Label(root, text=f"Number of classes on {day}:").grid(row=0, column=0, padx=10, pady=5)

    numbere = tk.Entry(root)
    numbere.grid(row=0, column=1)
    tk.Button(root, text="Next", padx=15, pady=2.5, fg="black", bg="white",
              command=lambda: getnumber(root, numbere.get())).grid(row=2, column=2, padx=10, pady=5)
    tk.Label(root, text=f'(If there are no classes on {day}, enter 0)', borderwidth=1).grid(row=2, column=0, padx=5,
                                                                                            pady=5)
    root.mainloop()

    # getdetails of classes
    for i in range(number):
        root = tk.Tk()
        plat = tk.StringVar()
        root.title(f"Deatils of {day}, Class - {i + 1}")

        tk.Label(root, text="Platform :").grid(row=0, column=0, padx=10, pady=5)
        tk.Checkbutton(root, text="WebEx", var=plat, offvalue="", onvalue="WebEx").grid(row=0, column=1, padx=10,
                                                                                         pady=5)
        tk.Checkbutton(root, text="G-Meet", var=plat, offvalue="", onvalue="G-Meet").grid(row=0, column=2, padx=10,
                                                                                         pady=5)

        tk.Label(root, text="Link of Class:").grid(row=1, column=0, padx=10, pady=2.5)

        linke = tk.Entry(root)
        linke.grid(row=1, column=1)

        # starttime
        tk.Label(root, text="Enter Starting Time:").grid(row=2, column=0, padx=10, pady=2.5)

        tk.Label(root, text="Hour:").grid(row=2, column=1, padx=10, pady=2.5)
        shour = tk.StringVar(value="Select an Hour")
        options = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
                   "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "00"]
        h = tk.OptionMenu(root, shour, *options)
        h.grid(row=2, column=2, padx=10, pady=2.5)

        tk.Label(root, text="Minute:").grid(row=3, column=1, padx=10, pady=2.5)
        sminute = tk.StringVar(value="Select an Minute")
        options = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
        h = tk.OptionMenu(root, sminute, *options)
        h.grid(row=3, column=2, padx=10, pady=2.5)

        # endingtime
        tk.Label(root, text="Enter Ending Time:").grid(row=4, column=0, padx=10, pady=2.5)

        tk.Label(root, text="Hour:").grid(row=4, column=1, padx=10, pady=2.5)
        ehour = tk.StringVar(value="Select an Hour")
        options = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
                   "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "00"]
        h = tk.OptionMenu(root, ehour, *options)
        h.grid(row=4, column=2, padx=10, pady=2.5)

        tk.Label(root, text="Minute:").grid(row=5, column=1, padx=10, pady=2.5)
        eminute = tk.StringVar(value="Select an Minute")
        options = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
        h = tk.OptionMenu(root, eminute, *options)
        h.grid(row=5, column=2, padx=10, pady=2.5)

        tk.Button(root, text="Next", padx=15, pady=2.5, fg="black", bg="white",
                  command=lambda: nextbuttonofdetails(root, nameoftt, day, plat.get(), linke.get(),
                                                      f"{shour.get()}:{sminute.get()}",
                                                      f"{ehour.get()}:{eminute.get()}")).grid(row=10, column=10, padx=5,
                                                                                              pady=5)
        root.mainloop()


def fileTT(nameoftt, day, plat, link, start, end):
    with open(f"timetables/{nameoftt}", "a") as f:
        f.write(f"{day}\n")
        f.write(f"{plat}\n")
        f.write(f"{link}\n")
        f.write(f"{start}\n")
        f.write(f"{end}\n")
    with open(f"timetables/{nameoftt}", "r") as f:
        print(f.read())


def getmnameoftt(root, name):
    root.destroy()
    global nameofT
    nameofT = name
    print("Name of TimeTAble: ",name)
    makett()


def getname(root):
    root.destroy()
    root = tk.Tk()
    root.title("Make A TimeTable")

    tk.Label(root, text="Name of Time-Table:").grid(row=0, padx=10, pady=2.5)

    name = tk.Entry(root)
    name.grid(row=0, column=1)

    tk.Button(root, text="Next", padx=15, pady=2.5, fg="black", bg="white",
              command=lambda: getmnameoftt(root, name.get())).grid(row=3, column=4, padx=5, pady=5)
    root.mainloop()


def makett():

    #messagebox.showinfo("Imp info", "All classes are started with a delay of 2 minutes. Eg: if u set a class for 13:05 the program will attend the class only at 13:07.")


    getclassdetails("Monday", nameofT)

    getclassdetails("Tuesday", nameofT)

    getclassdetails("Wednesday", nameofT)

    getclassdetails("Thursday", nameofT)

    getclassdetails("Friday", nameofT)

    getclassdetails("Saturday", nameofT)

    getclassdetails("Sunday", nameofT)
    print("TimeTable Created")
    mainmenu()


def loadtt():
    root = tk.Tk()
    root.title("Load Time-Table")


    if len(os.listdir("timetables")) == 0:
        tk.Label(root, text="There are no TimeTables. Create one using the Create button the main menu").pack(padx=10,pady=5)

    else:
      tk.Label(root, text="Chose a existing TimeTable").pack(padx=10, pady=5)
      for i in os.listdir("timetables"):
         tk.Button(root, text=f"{i}", padx=15, pady=5, fg="black", bg="white", command=lambda j=i: openit(j)).pack(padx=50, pady=5)

    root.mainloop()


def openit(file):
    messagebox.showinfo("Dont worry", "The TimeTable u selected is now loaded and working even though the program shows *not-responding*. Also, please dont close the chrome window that has been opened")
    f = open(f"timetables/{file}", "r")
    handletimetable(f)


def closeandload(root):
    root.destroy()
    loadtt()

def closeandsetup(root):
    root.destroy()
    setup()

def mainmenu():
    root = tk.Tk()
    root.title("Menu")
    root.geometry('210x150')

    tk.Button(root, text="Do Set-Up again", padx=15, pady=5, fg="black", bg="white",command=lambda: closeandsetup(root)).pack(padx=10, pady=10)

    tk.Button(root, text="Make a Time-Table", padx=15, pady=5, fg="black", bg="white",
              command=lambda: getname(root)).pack(padx=10,
                                                  pady=5)

    tk.Button(root, text="Load a Time-Table", padx=15, pady=5, fg="black", bg="white",
              command=lambda: closeandload(root)).pack(padx=10, pady=5)

    root.mainloop()


def handletimetable(file):
    global allclassdetails
    listoflines=file.readlines()
    allclassdetails=[]
    singlgeclass=[]
    c=0

    for i in listoflines:
        singlgeclass.append(i[:-1])
        c+=1
        if c%5==0:
            allclassdetails.append(singlgeclass)
            singlgeclass=[]
    print("Starting Classes")
    runclasses()

def runclasses():
    for i in allclassdetails:
        if i[1]=="G-Meet":
            print("Starting gMeet")
            with open("user_data/gmeet_mail_password.txt", "r") as f:
                list1 = f.readlines()
                email=list1[0]
                password=list1[1]
            classG=gmeet.gmeet(i[3],i[4],i[0],email[:-1],password[:-1],i[2])
            classG.run()
        if i[1]=="WebEx":
            print("Starting WebEx")
            with open("user_data/webex_mail_name.txt", "r") as f:
                list1 = f.readlines()
                name=list1[0]
                email=list1[1]
            classW=webex.webex(i[3],i[4],i[0],name[:-1],email[:-1],i[2])
            classW.run()



def runthatshit():
    main()
