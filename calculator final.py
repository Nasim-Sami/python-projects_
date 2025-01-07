from tkinter import *
import math
def get_digit(digit):
    global current,new
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)
    
def clear():
    result_label.config(text='')

        
def get_operator(op):
    global operator
    global first_number
    operator=op
    btn_text=['sine','cos','tan','log','exp']
    for i in range(5):
     if operator==btn_text[i]:
        new=operator
        result_label.config(text=new)
    
    if operator=='+' or operator =='-' or operator=='/' or operator=='*' or operator=='^(2)' or operator=='^': 
      try:   
       if operator != '-':
        first_number=float(result_label['text'])  
        new=str(first_number) + operator
        result_label.config(text=new)
      except:
         pass
  
     
def get_result():
    global second_number,first_number,operator
    
    if operator=='+':
        second_number=float(result_label['text'].split(operator)[1])
        result_label.config(text=str(first_number+second_number))

    elif operator=='sine':
        first_number=float(result_label['text'].split('sine')[1])* (math.pi)/180
        # print(first_number)
        try:
         result_label.config(text=str(math.sin(first_number)))
        except:
         result_label.config(text='error')
    elif operator=='cos':
        first_number=float(result_label['text'].split(operator)[1])* (math.pi)/180
        try:
         result_label.config(text=str(math.cos(first_number)))
        except:
         result_label.config(text='error')
    elif operator=='tan':
        first_number=float(result_label['text'].split(operator)[1])* (math.pi)/180
        try:
         result_label.config(text=str(math.tan(first_number)))
        except:
           result_label.config(text='error')
    elif operator=='log':
        first_number=float(result_label['text'].split(operator)[1])
        try:
         result_label.config(text=str(math.log(first_number)))
        except ValueError:
           result_label.config(text='error')
    elif operator=='exp':
       first_number=float(result_label['text'].split(operator)[1])
       result_label.config(text=str(math.exp(first_number)))
    elif operator=='^(2)':
       first_number=float(result_label['text'].split(operator)[0])
       result_label.config(text=str(first_number**2))
    elif operator=='^':
       first_number=float(result_label['text'].split(operator)[0])
       second_number=float(result_label['text'].split(operator)[1])
       result_label.config(text=str(math.pow(first_number,second_number)))
    elif operator=='-':
        try:
         splited_text=result_label['text'].split(operator)
        #  print(f"I am in  minus operator {splited_text}")
         if '^' in splited_text[0]:
            operator='^'
            get_result()
         else: 
          operator='-'
          first_number=float(splited_text[0])
          second_number=float(splited_text[1])
          result_label.config(text=str(first_number-second_number))
        except:
           splited_text=result_label['text'].split(operator)
           operator=splited_text[0]
           get_result()
        #    print(splited_text)
    
    elif operator=='*':
        second_number=float(result_label['text'].split(operator)[1])
        result_label.config(text=str(first_number*second_number))
    
    else:
       try: 
        splited_text=result_label['text'].split(operator)
        # print(f"here I am {splited_text}")
        first_number=float(splited_text[0])
        second_number=float(splited_text[1])
        
        if second_number==0:
            result_label.config(text='error')
        else:
            result_label.config(text=str((first_number/second_number)))
       except:
           pass

root=Tk()
root.title('Calculator')
root.geometry('327x387')
root.configure(background='black')
root.resizable(0,0)
result_label=Label(root,text=' ',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')
result_label.config(font=("Verdana",25,'bold'))

# row 1 design
btn_7=Button(root,text='7',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(7))
btn_7.grid(row=1,column=0)
btn_7.config(font=('Verdana',14))

btn_8=Button(root,text='8',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(8))
btn_8.grid(row=1,column=1)
btn_8.config(font=('Verdana',14))

btn_9=Button(root,text='9',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(9))
btn_9.grid(row=1,column=2)
btn_9.config(font=('Verdana',14))

btn_add=Button(root,text='+',width=5,height=2,bg='green',fg='black',command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('Verdana',14))

# row 2 design
btn_4=Button(root,text='4',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(4))
btn_4.grid(row=2,column=0)
btn_4.config(font=('Verdana',14))

btn_5=Button(root,text='5',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(5))
btn_5.grid(row=2,column=1)
btn_5.config(font=('Verdana',14))

btn_6=Button(root,text='6',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(6))
btn_6.grid(row=2,column=2)
btn_6.config(font=('Verdana',14))

btn_sub=Button(root,text='-',width=5,height=2,bg='green',fg='black',command=lambda:(get_operator('-'),get_digit('-')))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('Verdana',14))

# row 3 design
btn_1=Button(root,text='1',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(1))
btn_1.grid(row=3,column=0)
btn_1.config(font=('Verdana',14))

btn_2=Button(root,text='2',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(2))
btn_2.grid(row=3,column=1)
btn_2.config(font=('Verdana',14))

btn_3=Button(root,text='3',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(3))
btn_3.grid(row=3,column=2)
btn_3.config(font=('Verdana',14))

btn_mul=Button(root,text='x',width=5,height=2,bg='green',fg='black',command=lambda:get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('Verdana',14))

# row 4 design
btn_clr=Button(root,text='C',width=5,height=2,bg='green',fg='black',command=clear)
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('Verdana',14))

btn_0=Button(root,text='0',width=5,height=2,bg='green',fg='black',command=lambda:get_digit(0))
btn_0.grid(row=4,column=1)
btn_0.config(font=('Verdana',14))

btn_equal=Button(root,text='=',width=5,height=2,bg='green',fg='black',command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('Verdana',14))

btn_div=Button(root,text='/',width=5,height=2,bg='green',fg='black',command=lambda:get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('Verdana',14))

# row 5 design
btn_row5=['btn_sine','btn_cos','btn_tan','btn_log']
btn_text5=['sine','cos','tan','log']

for i in range(4):
 btn_row5[i]=Button(root,text=btn_text5[i],width=5,height=2,bg='green',fg='black',command=lambda value=btn_text5[i] : get_operator(value))
 btn_row5[i].grid(row=5,column=i)
 btn_row5[i].config(font=('Verdana',14))

#row 6 design
btn_row6=['btn_exp','btn_square','btn_power','btn_dot']
btn_text6=['exp','^(2)','^','.']
for i in range(3):
 btn_row6[i]=Button(root,text=btn_text6[i],width=5,height=2,bg='green',fg='black',command=lambda value=btn_text6[i] : get_operator(value))
 btn_row6[i].grid(row=6,column=i)
 btn_row6[i].config(font=('Verdana',14))

btn_row6[3]=Button(root,text=btn_text6[3],width=5,height=2,bg='green',fg='black',command=lambda : get_digit('.'))
btn_row6[3].grid(row=6,column=3)
btn_row6[3].config(font=('Verdana',14))



root.mainloop()