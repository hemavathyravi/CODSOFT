import tkinter
from tkinter import *

root=Tk()
root.title("TODO LIST")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list= []

def openTaskFile():
    try:
        global task_list
        with open("C:/Users/Hemavathy/OneDrive/Documents/Todo list/tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open("C:/Users/Hemavathy/OneDrive/Documents/Todo list/tasklist.txt","w")
        file.close()
            

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("C:/Users/Hemavathy/OneDrive/Documents/Todo list/tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

            
def editTask():
    selection_index = listbox.curselection()
    if selection_index:
        edit_window = Toplevel(root)
        edit_window.title("Edit Task")

        def on_edit_button_click():
            edited_task = edit_entry.get()
            if edited_task:
                original_task = listbox.get(selection_index)
                listbox.delete(selection_index)
                listbox.insert(selection_index, edited_task)

                if original_task in task_list:
                    task_list.remove(original_task)
                task_list.append(edited_task)

                with open("C:/Users/Hemavathy/OneDrive/Documents/Todo list/tasklist.txt", "w") as taskfile:
                    for t in task_list:
                        taskfile.write(t + "\n")

                edit_window.destroy()

        edit_label = Label(edit_window, text="Edit Task:")
        edit_label.pack()

        edit_entry = Entry(edit_window)
        edit_entry.pack()

        edit_button = Button(edit_window, text="Edit", command=on_edit_button_click)
        edit_button.pack()

def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open ("C:/Users/Hemavathy/OneDrive/Documents/Todo list/tasklist.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
    listbox.delete(ANCHOR)
                   
#icon
Image_icon=PhotoImage(file="C:/Users/Hemavathy/OneDrive/Documents/Todo list/Image/task.png")
root.iconphoto(False,Image_icon)

#topbar
TopImage=PhotoImage(file="C:/Users/Hemavathy/OneDrive/Documents/Todo list/Image/topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="C:/Users/Hemavathy/OneDrive/Documents/Todo list/Image/dock.png")
Label(root,image=dockImage,bg="#355E3B").place(x=30,y=25)

noteImage=PhotoImage(file="C:/Users/Hemavathy/OneDrive/Documents/Todo list/Image/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=30,y=25)


heading=Label(root,text="TODO List",font="arial 20 bold",fg="white",bg="#355E3B")
heading.place(x=130,y=20)

#main
frame=Frame(root,width=400,height=50,bg="blue")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button=Button(frame,text="add",font="arial 20 bold",width=6,bg="#355E3B",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1= Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side= RIGHT ,fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
#openTaskFile()

#delete
Delete_icon=PhotoImage(file="C:/Users/Hemavathy/OneDrive/Documents/Todo list/Image/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=LEFT, anchor=SE,pady=7)

Edit_icon=PhotoImage(file="C:/Users/Hemavathy/OneDrive/Documents/Todo list/Image/edit.png")
Button(root,image=Edit_icon,bd=0,command=editTask).pack(side=RIGHT, anchor=SW,pady=7)




root.mainloop()
