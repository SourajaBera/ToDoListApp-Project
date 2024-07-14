
from tkinter import *

from tkinter import messagebox
task_List=[]
counter=1

def inputError():

    if enterTaskField.get()=="":
        messagebox.showerror("InputError!!","Enter your Task")
        return 0
    return 1
def cleartaskField():
    enterTaskField.delete(0,END)
def cleartaskNumberField():
    taskNumberField.delete(0.0,END)

def insertTask():
    global counter

    value=inputError()
    if value==0:
        return
    
    task=enterTaskField.get()
    content=task+"\n"

    task_List.append(content)
    TextArea.insert('end-1 chars',"["+str(counter)+"]"+content)

    counter+=1
    cleartaskField()
def delete():
    global counter
    if len(task_List) == 0 :
        messagebox.showerror("No task","enter a valid value")
        return
    number = taskNumberField.get(1.0,END)
    if number == "\n" :
        messagebox.showerror("input error")
        return
    else :
        task_no = int(number)
    cleartaskNumberField()
	
	
    task_List.pop(task_no - 1)
 
    counter -= 1
	
	
    TextArea.delete(1.0, END)

	
    for i in range(len(task_List)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + task_List[i])
	


if __name__=="__main__":
    gui=Tk()
    gui.configure(bg="cadetblue3")
   # img=PhotoImage(file=r"c:\Users\SOURAJA\OneDrive\Pictures\todolist.png")
    #gui.iconphoto(False,img)
    gui.title("ToDoListApp")
    gui.geometry("250x300")

    enterTask=Label(gui,text="::Enter Your Tasks::",bg="lightslateblue")
    enterTaskField=Entry(gui)
    submit=Button(gui,text="Submit tasks",fg="black",bg="paleturquoise3",command=insertTask)
    
    TextArea=Text(gui,height=5,width=25,font="lucida 13")
    
    TaskNumber=Label(gui,text="Delete task number",bg="lightslateblue")
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
    delete=Button(gui,text="Delete",fg="black",bg="paleturquoise3",command=delete)

    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

    enterTask.grid(row = 0, column = 2)
                 
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
    submit.grid(row=2,column=2)
    TextArea.grid(row=3,column=2,padx=10,sticky=W)
    TaskNumber.grid(row=4,column=2,pady=5)
    taskNumberField.grid(row=5,column=2)
    delete.grid(row=6,column=2,pady=5)
    Exit.grid(row=7,column=2)
    
    gui.mainloop()