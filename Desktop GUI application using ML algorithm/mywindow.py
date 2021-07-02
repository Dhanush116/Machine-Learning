from tkinter import *
import pickle

# ["","","","","","",""]
class LRwindow:
    def __init__(self,win):
        # load model
        f = open("LR_without_scaling.sav","rb")
        self.model = pickle.load(f)
        f.close()

        # 8 lablels
        self.lbl1=Label(win, text='housing_median_age')
        self.lbl2=Label(win, text='total_rooms')
        self.lbl3=Label(win, text='total_bedrooms')
        self.lbl4=Label(win, text='population')
        self.lbl5=Label(win, text='households')
        self.lbl6=Label(win, text='median_income')
        self.lbl7=Label(win, text='ocean_proximity')
        self.lbl8=Label(win, text='Price')

        # 8 Entries
        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.t6=Entry()
        self.t7=Entry()
        self.t8=Entry()



        self.lbl1.place(x=100, y=50)
        self.t1.place(x=300, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=300, y=100)

        self.lbl3.place(x=100, y=150)
        self.t3.place(x=300, y=150)

        self.lbl4.place(x=100, y=200)
        self.t4.place(x=300, y=200)

        self.lbl5.place(x=100, y=250)
        self.t5.place(x=300, y=250)

        self.lbl6.place(x=100, y=300)
        self.t6.place(x=300, y=300)

        self.lbl7.place(x=100, y=350)
        self.t7.place(x=300, y=350)

        self.b1=Button(win, text='Predict', command=self.predict)

        self.b1.place(x = 200,y = 400)

        self.lbl8.place(x=100, y=450)
        self.t8.place(x=300, y=450)

    def predict(self):
        housing_median_age = float(self.t1.get())
        total_rooms        = float(self.t2.get())
        total_bedrooms     = float(self.t3.get())
        population         = float(self.t4.get())
        households         = float(self.t5.get())
        median_income      = float(self.t6.get())
        ocean_proximity    = float(self.t7.get())
        result = self.model.predict([[housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity]])
        result = result[0]
        self.t8.insert(END,str(result))
