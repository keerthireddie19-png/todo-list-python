import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    listbox.delete(tk.ACTIVE)

root = tk.Tk()
root.title("TO-DO list")

entry = tk.Entry(root, width=30)
entry.pack()

add_button = tk.Button(root, text="add task",command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="detele ask", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(root, width=40)
listbox.pack()

root.mainloop()
