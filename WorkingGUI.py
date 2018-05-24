from tkinter import * #hey
 
window = Tk()

window.title("First Python GUI")

window.geometry('550x400')

#Create a label widget
#To add a label to our previous example, we will create a label using the label class like this:
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

#Then we will set its position on the form using the grid function and give it the location like this:
lbl.grid(column=0, row=0)

#You can create a textbox using Tkinter Entry class like this:

txt = Entry(window,width=10)   

txt.grid(column=1, row=0)

 #set focus to text box txt.focus() but where to put ?

def clicked():
    
    result = txt.get()
    words = result.split()
    words.sort()
    lbl.configure(text= words)

#You can change foreground for a button or any other widget using fg property.
#Also, you can change the background color for any widget using bg property.
#Let’s start by adding the button to the window, the button is created and added to the window the same as the label:
#Handle button click event
#First, we will write the function that we need to execute when the button is clicked:
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
 
btn.grid(column=2, row=0) # Note that we place the button on the second column of the window which is 1.
# If you forget and place the button on the same column which is 0, it will show the button only, since the button will
# be on the top of the label.#You can change foreground for a button or any other widget using fg property.
#Also, you can change the background color for any widget using bg property.

window.mainloop()
