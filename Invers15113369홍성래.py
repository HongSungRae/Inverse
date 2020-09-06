# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:24:10 2019

@author: 82109
"""


'''step 1 : window and functions'''
import tkinter
from tkinter import *
import numpy as np
from tkinter.simpledialog import *

window=Tk()
window.title('Inverse_Matrix__==__15113369_홍성래')
window.resizable(width=True, height=True)

n=0
matrix=np.array([[]])
In=np.array([])
adj=np.array([])
det=0
entlist=[]

def zeros(a, b):
    temp_in = []
    temp_out = []
    for i in range(b):
        temp_in.append(0)
    for j in range(a):
        temp_out.append(temp_in)
    mat = np.array(temp_out)
    return mat

def matmul(A, B):
    mat = zeros(n,n)
    for i in range(n):
        for j in range(n):
            value = 0
            for k in range(n):
                value += A[i,k] * B[k,j]
            mat[i,j] = round(value, 10)
    return mat

def delete(A, b, c):
    rows = A.shape[0]
    columns = A.shape[1]
    if c == 0: # delete 'b'th row
        mat = zeros(rows - 1, columns)
        k = 0
        for i in range(rows):
            if i != b:
                for j in range(columns):
                    mat[k,j] = A[i,j]
                k += 1
            elif i == b:
                pass
        return mat
    elif c == 1: # delete 'b'th column
        mat = zeros(rows, columns - 1)
        k = 0
        for i in range(columns):
            if i != b:
                for j in range(rows):
                    mat[j,k] = A[j,i]
                k += 1
            elif i == b:
                pass

        return mat
    elif c != 0 and c != 1:
        print("Caution! 3rd parameter can be only 0 or 1")
    

'''step 2 : Is determinant = 0 or != 0 ?'''
#np.delete(matrix,i_th,0=row and 1=column)
#matrix.shape : returns m and n by tuple (m,n)
#matrix.shape[0=row and 1=column] : returns the number of compnents of rows or columns
def det(A):
    if A.shape != (1,1):
        return sum([(-1)**i * A[i, 0] * det(delete(delete(A, 0, 1), i, 0)) for i in range(A.shape[0])])
    else:
        return A[0,0]
    


'''step 3 : GUI'''
def ok():
    global n
    if (ent1.get()).isdigit()==True and (ent1.get())!=0:
        n=int(ent1.get())
        matrixEnt(n)
    else:
        messagebox.showinfo('ERROR','Invalid value')
        

def matrixEnt(n):
    for j in range(n):
        for i in range(n):
            ent=tkinter.Entry(window, width=3)
            ent.grid(row=j+4,column=2*i+1)
            entlist.append(ent)
            pass

    label1.grid(row=0,column=0,columnspan=n*2)
    ent1.grid(row=1,column=0,columnspan=n*2)
    okButton.grid(row=1,column=1,columnspan=n*2)
    label2.grid(row=3,column=0,columnspan=n*2)
    searchButton.grid(row=n+4,column=0,columnspan=n*2)





'''step 4 : DEF; Search Inverse Function'''
def inverse():
    global matrix
    matrix=zeros(n,n)
    for i in range(n):
        for j in range(n):
            matrix[i,j]=entlist[i*n+j].get()
            
    if det(matrix)==0:
        messagebox.showinfo('ERROR','det(A)=0, No inv. matrix exists.')
    else:
        global adj
        adj=zeros(n,n)
        for i in range(n):
            for j in range(n):
                adj[j,i]=((-1)**(i+j))*det(delete(delete(matrix,i,0),j,1))
        
        global inverseMatrix
        inverseMatrix=(1/det(matrix))*adj
        print(matmul(matrix, inverseMatrix))
        
        
        label1=tkinter.Label(window,text="▼InverseMatrix")
        label1.grid(row=n+10,column=0,columnspan=n*2)
        label2=tkinter.Label(window,text=inverseMatrix)
        label2.grid(row=n+11,column=0,columnspan=n*2)
        label3=tkinter.Label(window,text="▼A x InverseMatrix")
        label3.grid(row=n+12,column=0,columnspan=n*2)
        label=tkinter.Label(window,text=matmul(inverseMatrix,matrix))
        label.grid(row=n+13,column=0,columnspan=n*2)
        label3=tkinter.Label(window,text='Coded by 15113369 HONG')
        label3.grid(row=n+14,column=0,columnspan=n*2)


label1=tkinter.Label(window,text="Only (n X n) matrix is calculated. \nWrite down the value of 'n'"
             ,font=('',15))
label1.grid(row=0,column=0,columnspan=2)
ent1=tkinter.Entry(window,width=3)
ent1.grid(row=1,column=0,columnspan=2)
okButton=tkinter.Button(window,text='OK',bg='blue',fg='white',command=ok)
okButton.grid(row=1,column=1,columnspan=2)
label2=tkinter.Label(window,text="------------------------------",font=('',10))
label2.grid(row=3,column=0)
searchButton=tkinter.Button(window,text='GET Inverse',command=inverse)




window.mainloop() 