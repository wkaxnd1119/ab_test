# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 11:45:54 2022

@author: myj
"""


from tkinter import * 
tk = Tk()
tk.title("AB TEST")
tk.geometry("700x300")

for i in range(1,8):
    globals()['entry{}'.format(i)] = Entry(tk)

def execute(): # 카이제곱분포 함수 실행 
    try:
        a_pos = float(entry1.get())
        total_a = float(entry2.get()) 
        b_pos = float(entry3.get()) 
        total_b = float(entry4.get())
        
        positive= [a_pos, b_pos]
        negative = [total_a- a_pos, total_b - b_pos]
        chi, p, d_f, expected = chi2_contingency([positive, negative])
        entry5.delete(0, END)
        entry5.insert(0, round(chi, 2))
        entry6.delete(0, END)
        entry6.insert(0, round(p,2))
        if p<= 0.05:
            text = "A와 B의 차이는 유의미합니다"
        else: text = "A와 B의 차이는 무의미합니다"
        entry7.delete(0, END)
        entry7.insert(0, text)
    except: 
        error_text = "오류: 입력값 확인 필요"
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        entry7.insert(0, error_text)

def clear(): # 프로그램 리셋을 위한 함수
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    

label1 = Label(tk, text='A 집단 전환 고객수').grid(row=1, column=0)
label2 = Label(tk, text='A 집단 전체 수').grid(row=1, column=10)
label3 = Label(tk, text='B 집단 전환 고객수').grid(row=5, column=0)
label4 = Label(tk, text='B 집단 전체 수').grid(row=5, column=10)
label5 = Label(tk, text='chi2통계량').grid(row=15, column=0)
label6 = Label(tk, text='p_value').grid(row=16, column=0)
label7 = Label(tk, text='검정 결과').grid(row=17, column=0)


entry1.grid(row=1, column = 5)
entry2.grid(row=1, column = 15)
entry3.grid(row=5, column = 5)
entry4.grid(row=5, column = 15)
entry5.grid(row=15, columns=15)
entry6.grid(row=16, columns=15)
entry7.grid(row=17, columns=15)


button1 = Button(tk, text='실행', command=execute).grid(row=12 ,column=7)
button2 = Button(tk, text='Reset', command=clear).grid(row=12, column=10)

tk.mainloop()
