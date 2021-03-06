from tkinter import *
# root widget
root = Tk()
# program title
root.title("Simple Calculator")
# create entry (input) field
e = Entry(root, width=35, borderwidth=5)
# columnspan=3 means field will be width of three columns, to fit three single column width buttons underneath
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter Your Name: ")

# button click function
def button_click(number):
  #e.delete(0, END) # deletes what's already in the field

  #next two lines are to reverse the order of input. Beforehand, 108 would appear on the calc field as 801.
  current = e.get() # collects what is entered
  e.delete(0, END)# deletes what's already in the field
  #next line collects number assigned to button into field and adds this to the number already in the field, as a string. Recasting the integers as strings enables changing the order of the numbers. Current and Number cocatenated as strings so + puts them together rather thn acting as operand.    
  e.insert(0, str(current) + str(number))

# clear button functions           
def button_clear():
  e.delete(0, END)

# To add two numbers together, the calculator needs to 1) receive the first number and store it in memory. 2) clear the first number. 3) recieve an 'add' symbol and store that in the memory 4) receive the second number and store that in the memory 5) clear the second number 6) receive an equals symbol and sum the two number s together 7) output the sum. Since we're dealing with two different functions here add and equals, variables can't be passed  between functions. 
  
# to get around this we're going to create a Global variable 'global'.

# using the keyword 'global' tells Python that the variable is global and therefore can be used outside of the function.

# operand functions

def button_add():
  #enter first number
  first_number = e.get()# collects first number
  global f_num # creating global variable 
  # assigning the addition function
  global math
  math = "addition"
  f_num = int(first_number) # stores first number as integer in global variable 
  e.delete(0, END) # clears first number
  

 
def button_subtract():
  #enter first number
  first_number = e.get()# collects first number
  global f_num # creating global variable 
  # assigning the addition function
  global math
  math = "subtraction"
  f_num = int(first_number) # stores first number as integer in global variable 
  e.delete(0, END) # clears first number
  
def button_multiply():
  #enter first number
  first_number = e.get()# collects first number
  global f_num # creating global variable 
  # assigning the addition function
  global math
  math = "multiplication"
  f_num = int(first_number) # stores first number as integer in global variable 
  e.delete(0, END) # clears first number
  
def button_divide():
  #enter first number
  first_number = e.get()# collects first number
  global f_num # creating global variable 
  # assigning the addition function
  global math
  math = "division"
  f_num = int(first_number) # stores first number as integer in global variable 
  e.delete(0, END) # clears first number

def button_equal():
  #enter second number and add
  second_number = e.get() # collects second number
  e.delete(0, END) # clears anything in the field
  # sends operand to equal 
  if math == "addition":
    # adds global variable f_num from button_add function and adds it to the collected second_number local variable.
    e.insert(0,f_num + int(second_number))
  if math == "subtraction":
    e.insert(0,f_num - int(second_number))
  if math == "multiplication":
    e.insert(0,f_num * int(second_number))
  if math == "division":
    e.insert(0,f_num / int(second_number))
  
  
# Define Buttons
# to pass values into the function, we would normally put the values in brackets on the end of function name at the end of each line. But here we can't use the brackets at the end of the function so we need to add in lamda to enable us to do so. 

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# lamda not required for buttons below as we are not pasing values through them
# also padx for add button slightly narrower to differentiate operand from numbers
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

# out the buttons on the screen  

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

 

root.mainloop()