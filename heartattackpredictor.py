from sklearn import svm
import pandas as pd
from tkinter import *
from tkinter import messagebox

root=Tk()
resData=[]

def predictor():
    data1=pd.read_csv('bpchart.csv')
    x1field=['Age','MinBP','AvgBP','MaxBP','TimeInCare']
    x2field=['Age','MinBP','AvgBP','MaxBP','TimeInCare','Chances']
    x1=data1.iloc[:,:-2] 
    y1=data1['Chances']   #Finding
    x2=data1.iloc[:,:-1] 
    y2=data1['TimeTillDeath']   #Finding
    
    #Training
    clf1=svm.SVC(kernel='linear')
    clf2=svm.SVC(kernel='linear')
    clf1.fit(x1[x1field],y1)
    clf2.fit(x2[x2field],y2)

    avgbp=int(int(Minbp.get())+int(Maxbp.get()))/2
    if(Age.get()>0):
        x1_test=[[Age.get(),Minbp.get(),avgbp,Maxbp.get(),Tincare.get()]]
        pred_chance=clf1.predict(x1_test)
        x2_test=[[Age.get(),Minbp.get(),avgbp,Maxbp.get(),Tincare.get(),int(pred_chance)]]
        pred_timeOD=clf2.predict(x2_test)
        resData=[int(pred_chance), int(pred_timeOD)]
        result='Chances of Heart-attacks are High\nTime until pronounced dead: '+str(resData[1])+' day(s)'
        if(resData[0]==1): msg1=messagebox.showinfo('Results', result)
        else: msg1=messagebox.showinfo('Results','Chances of Heart-attacks are Low')
        fp=open('bpchart.csv','a')
        data='\n'+Name.get()+','+str(Age.get())+','+str(Minbp.get())+','+str(avgbp)+','+str(Maxbp.get())+','+str(Tincare.get())+','+str(int(pred_chance))+','+str(int(pred_timeOD[0]))
        fp.write(data)
        

C = Canvas(root, height = 250, width = 300)
w2 = Label(root, justify=LEFT, text="Heart Attack Predictor")
w2.config(font=("Candara", 16))
w2.grid(row=1, column=0, columnspan=2, padx=100)
Name=StringVar()
NameLb = Label(root, text="Name of the Patient")
NameLb.grid(row=6, column=0, pady=5, sticky=W, padx=15)
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1, padx=15, pady=5)
Age=IntVar()
Minbp=IntVar()
Maxbp=IntVar()
Tincare=IntVar()
AgeLb = Label(root, text="Age of the Patient")
AgeLb.grid(row=7, column=0, pady=5, sticky=W, padx=15)
AgeEn = Entry(root, textvariable=Age)
AgeEn.grid(row=7, column=1, padx=15, pady=5)
MinbpLb = Label(root, text="Minimum Recorded Blood Pressure")
MinbpLb.grid(row=8, column=0, pady=5, sticky=W, padx=15)
MinbpEn = Entry(root, textvariable=Minbp)
MinbpEn.grid(row=8, column=1, padx=15, pady=5)
MaxbpLb = Label(root, text="Maximum Recorded Blood Pressure")
MaxbpLb.grid(row=9, column=0, pady=5, sticky=W, padx=15)
MaxbpEn = Entry(root, textvariable=Maxbp)
MaxbpEn.grid(row=9, column=1, padx=15, pady=5)
TincareLb = Label(root, text="Time in care")
TincareLb.grid(row=10, column=0, pady=5, sticky=W, padx=15)
TincareEn = Entry(root, textvariable=Tincare)
TincareEn.grid(row=10, column=1, padx=15, pady=5)
Res = Button(root, text="Predict Results", command=predictor)
Res.grid(row=11, column=1,padx=10, pady=15)
root.mainloop()   