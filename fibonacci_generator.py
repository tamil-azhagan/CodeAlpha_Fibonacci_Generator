import tkinter as tk
#we can import ttk ie Themed Tkinter Widgets because it has more modern themes
from tkinter import ttk

#For generating fibonacci series
def fibonacci_generator():
    try:
        n=int(entry_widget.get())
        if n<1:
            raise ValueError("Please Type Postive Number and Not Zero")
        fib_list=[0,1,1]

        for i in range(2,n-1):
            fib_list.append(fib_list[i]+fib_list[i-1])

        #Clearing The window
        text_widget.delete("1.0",tk.END)

        for i in fib_list:
            text_widget.insert(tk.END,f"{i} ","num_color")


    except ValueError as e:
        text_widget.delete("1.0",tk.END)
        text_widget.insert(tk.END,f"{e}","error_color")


#creating the window
root=tk.Tk()
root.title("FIBONACCI GENERATOR")

#entry label
entry_title=ttk.Label(root,text="WELCOME TO FIBONACCI GENERATOR",foreground='red')
entry_title.pack(pady=10)

#entry label for typing n value
entry_label=ttk.Label(root,text="Enter the number of Fibonacci Terms you want to Generate",foreground='Green')
entry_label.pack(pady=10)

#entry widget for typing n value
entry_widget=ttk.Entry(root,width=20)
entry_widget.pack(pady=10)

#Buttton for generating numbers
generate_button=ttk.Button(root,text='Generate',command=fibonacci_generator)
generate_button.pack(pady=10)

#textspace for displaying numbers
text_widget=tk.Text(root,height=20,width=70)
text_widget.pack(pady=10)

#for typing in colors
text_widget.tag_configure("num_color",foreground="blue")
text_widget.tag_configure("error_color",foreground="red")

root.mainloop()