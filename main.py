#importing
from tkinter import*
from datetime import datetime
import random
# from tkinter import filedialog
import tkinter.messagebox
from datetime import timedelta

 #windowcreation
window=Tk()
window.geometry("700x600")
window.title("COMSATS UNIVERSITY ISLAMABAD")
window.configure(background="#ffffff")
window.resizable(0,0)


#question strings
questions=["Who is the last prophet send by ALLAH SWT",
               "PROPHET PBUH MIGRATED FROM MECCCA TO WHCIH CITY??",
               "WHO WAS FIRST PROPHET",
               "WHICH PROPHET WAS SON IN LAW OF HAZRAT SHOAIB",
               "WHICH HOLY BOOK WAS REVEALED ON PROPHET DAUD A.S ?",
               "FOR WHOM PROPHET SAWW I AM FROM HIM AND HE IS FROM ME ",
                "WHO IS THE AUTHOR OF SAHI BUKHARI",
               "IN THE BATTLE OF KARBALA WHO WAS THE FLAG HOLDER OF IMAM HUSAIN'S A.S ARMY",
               "WHO IS KNOWN AS LION OF GOD",
               "AT WHICH PLACE HAZRAT JIBRAIL A.S BROUGHT THE FIRST REVELATION TO PROPHET SAWW? " ]
answere_options = [
    ["HAZRAT YUSUF","HAZRAT MUHAMMAD","HAZRAT ZAKRIYA","HAZRAT IDREES"],
    ["MADINA","TAIF","KUFA","MADAIN"],
    ["HAZRAT YUSUF","HAZRAT MUSA ","HAZRAT ADAM","HAZRAT IDREES"],
    ["HAZRAT IBRAHIM","HAZRAT MUSA","HAZRAT YAHYA","HAZRAT ISA"],
    ["TORAT","ZABOOR","INJEEL","QURAN MAJEED"],
    ["TALHA BIN ZUBAIR","IBN E MASOOD","HAZRAT IMAM HUSSAIN A.S","SAAD BIN ABI WAQAS"],
    ["AHMED BIN HAMBAL","MUHAMMAD AL BUKHARI","Abdur-Rahman ibn","SHEIKH ABBAS QUMI"],
    ["HAZRAT JAFFAR E TYAR","HAZRAT ABDULLAH","HAZRAT MUSLIM BIN AQEEL A.S","HAZRAT ABBAS IBN E ALI A.S"],
    ["HAZRAT ALI A.S","AHMAD BIN HAMBAL","TALHA BIN ZUBAIR","UMMAYA"],
    ["HABSHA","MADAIN","CAVE OF HIRA","DAMASCUS"],
]
correct_ans= [1,0,2,1,1,2,1,3,0,3]
user_ans=[]

def windowend():
    window.destroy()
    window2=Tk()
    window2.geometry="500X800"
    window2.config(bg="red")
    _quit=Label(window2,text="YOU HAVE ENDED THE QUIZ",bg="red4",fg="white")
    _quit.pack()

def update_time():
    import time
    format = "%H:%M:%S"

    now = datetime.now()
    now = now.strftime(format)
    s2 = '12:9:20'



    string = datetime.strptime(s2, format) - datetime.strptime(now, format)







    l = Label(window, font=("calibari,70,bold"), bg="black", fg="white",width=10)
    l.place(x=40, y=150)

    l.config(text=string)
    l.after(1000, update_time)


indexes = []
def gen():
    global indexes
    while(len(indexes) < 5 ):
        x = random . randint(0,9)
        if x in indexes:
            continue

        else:
            indexes.append(x)
def showresult(score):
    lblquestions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    # labelimage=Label(window,)
    # labelimage.pack()
    labelresult=Label(window,font=("consolas",23,"bold"),bg="red4")
    labelresult.place(x=30,y=200)
    _score= Label(window,font=("consolas",23,"bold"),bg="red4",text =("Your score is",score))
    _score.place(x=30,y=350)

    if score >=20:

        # img=PhotoImage(file="great.png")
        # labelimage.configure(image=img)
        # labelimage.img=img
        labelresult.configure(text="CONGRATULATION YOU ARE SELECTED AT MERIT")
    elif (score >=10 and score < 20):
        # img = PhotoImage(file="ok.png")
        # labelimage.configure(image=img)
        # labelimage.img = img
        labelresult.configure(text="you have passed the exam")
    else:
        # img = PhotoImage(file="bad.png")
        # labelimage.configure(image=img)
        # labelimage.img = img
        labelresult.configure(text="YOU SHOULD WORK HARD")



def calc():
    global indexes,user_ans,correct_ans
    x=0
    score=0
    for i in indexes:
        if user_ans[x] == correct_ans[i]:
            score = score + 5
        x+=1
        print(score)
        showresult(score)




ques = 1
def selected():
    global  radiovar,user_ans
    global lblquestions,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_ans.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblquestions.config(text=questions[indexes[ques]])
        r1['text']=answere_options[indexes[ques]][0]
        r2['text'] = answere_options[indexes[ques]][1]
        r3['text'] = answere_options[indexes[ques]][2]
        r4['text'] = answere_options[indexes[ques]][3]
        ques+=1
    else:
        print(indexes)
        print(user_ans)
        calc()



def starquiz():
    global  lblquestions,r1,r2,r3,r4
    # lbl2=Label(window,textvariable=name,font=("arial",20),fg="black")
    # lbl2.pack(pady=(50,40))
    lblquestions = Label(window, text=questions[indexes[0]]
                        , font=("Consolas", 16), width=500, justify="center", wraplength=400,bg="white",fg="red4")
    lblquestions.pack(pady=(180,30))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(window, text=answere_options[indexes[0]][0], font=("times", 12, "bold"), value=0,
                     variable=radiovar,bg="white",fg="red4")
    r1.pack(pady=5)

    r2 = Radiobutton(window, text=answere_options[indexes[0]][1], font=("times", 12, "bold"), value=1,
                     bg="white",variable=radiovar,fg="red4")
    r2.pack(pady=5)

    r3 = Radiobutton(window, text=answere_options[indexes[0]][2], font=("times", 12, "bold"), value=2,
                     bg="white",variable=radiovar,fg="red4")
    r3.pack(pady=5)

    r4 = Radiobutton(window, text=answere_options[indexes[0]][3], font=("times", 12, "bold"), value=3,
                     bg="white",variable=radiovar,fg="red4")
    r4.pack(pady=5)


def startpressed():

    global window,now,s2,l,string
    name.destroy()
    nameentery.destroy()
    # labelimage.destroy()
    roll.destroy()
    rollentery.destroy()
    next.destroy()
    welcome.destroy()
    gen()
    starquiz()
    update_time()





    # pics = PhotoImage(file="comsats.png")
    frame0=Frame(window,bg="green",width=700,height=100)
    frame0.place(x=0, y=0)

    gonext=Button(window,bg="blue",text="NEXT",font=("consolas",12,"bold"),fg="white",width=10,command=selected)
    gonext.place(x=300, y=450)

    quit = Button(window, bg="black", text="QUIT", font=("consolas", 12, "bold"), fg="white", width=10, command=windowend)
    quit.place(x=580, y=150)




    sad=namevalue.get()
    print(sad)
    name1=Label(frame0,text=sad,font=("arial",12),fg="red4",bg="light green")
    name1.place(x=3, y=45)
    _roll=rollvalue.get()
    print(_roll)
    roll2 = Label(frame0, text=_roll, font=("arial", 12), fg="red4", bg="light green")
    roll2.place(x=3, y=70)

    cui=Label(frame0,text="COMSATS UNIVERSITY ISLAMABAD",font=("consolas,",15,"bold"),fg="white",bg="blue")
    cui.place(relx=0.5,rely=0.5,anchor=CENTER)





# logo = PhotoImage(file="C:\Users\Zamin\Documents\quiz\comsats.png")

# labelimage = Label(
#     window,
#     image = logo,
#     background = "#ffffff",
# )
# labelimage.pack(pady=(30,0))

welcome = Label(
    window,
    text = "WELCOME TO COMSATS UNIVERSITY",
    font = ("Comic sans MS",20,"bold"),
    background = "#ffffff",
)
welcome.pack(pady=(0,30))

name = Label(window, text="NAME OF CANDIDATE", font=("arial",15,"bold" ),bg="yellow")
name.place(x=250, y=375)

namevalue = StringVar()

nameentery = Entry(window, textvariable=namevalue,width=30,bd=2,relief=SUNKEN,font=("arial",12,"bold"),justify="center")
nameentery.place(x=220, y=425)

roll = Label(window, text="ROLL NUMBER", font=("arial",15,"bold" ))
roll.place(x=272, y=465)

rollvalue = StringVar()

rollentery = Entry(window, textvariable=rollvalue,width=30,bd=2,relief=SUNKEN,font=("arial",12,"bold"),justify="center",fg="red")
rollentery.place(x=220, y=500)

next = Button( window, text = "GO NEXT",font=("arial",14),fg="white",bg="red",command=startpressed)
next.place(x=287, y=540)
window.mainloop()
