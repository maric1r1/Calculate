import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox
from Operations import Operation

root = tb.Window(themename="vapor")
root.title("Math")
# root.geometry("500x500")

def calculate():
    global entry_number

    f = tuple(entry_number.get().split(","))

    if len(f) == 2 :
        op = Operation(f)
        result_sum.config(text=str(op.sum())) 
        result_sub.config(text=str(op.dim())) 
        result_mul.config(text=str(op.mult())) 
        result_div.config(text=str(op.div())) 
    else:
        Messagebox.show_info("Please, enter only two numbers", "Error")

frame = tb.Frame(root)
frame.pack(pady=20,padx = 20)

entry_text = tb.Label(frame, text = "Enter Two Number", bootstyle = "primary", font=("Helvetica",20))
entry_text.grid(row = 0, column = 0 , pady =20, padx = 20,sticky="news")

entry_number = tb.Entry(frame, bootstyle = "info")
entry_number.grid(row = 0, column = 1, pady =10, padx = 10, ipadx=50)

button = tb.Button(frame, text="Entry", command=calculate)
button.grid(row = 0, column = 6 , pady =20, padx = 10, ipadx=50)

label = tb.Label(frame, text = "Enter only two numbers, separated by a comma", bootstyle = "primary", font=("Helvetica",10))
label.grid(row = 1, column = 0 , pady =5, padx = 20,sticky="news")

res_sum = tb.Label(frame, text = "\u2795", bootstyle = "secondary", font=("Helvetica",20))
res_sum.grid(row = 2, column = 0 , pady =5, padx = 20, ipadx = 20,sticky="news")

result_sum = tb.Label(frame, bootstyle = "secondary", font=("Helvetica",20))
result_sum.grid(row = 3, column = 0 , pady =20, padx = 20, ipadx = 20,sticky="news")

sep1 = tb.Separator(frame, orient="vertical", bootstyle = "warning")
sep1.grid(row = 2, column = 1 , pady =5, padx = 20, ipadx = 20, rowspan=3)

res_sub = tb.Label(frame, text = "\u2796", bootstyle = "sucess", font=("Helvetica",20))
res_sub.grid(row = 2, column = 2 , pady =5, padx = 20, ipadx = 20,sticky="news")

result_sub = tb.Label(frame, bootstyle = "sucess", font=("Helvetica",20))
result_sub.grid(row = 3, column = 2 , pady =5, padx = 20, ipadx = 20,sticky="news")

sep2 = tb.Separator(frame, orient="vertical", bootstyle = "warning")
sep2.grid(row = 2, column = 3 , pady =5, padx = 20, ipadx = 20,rowspan=3)

res_mul = tb.Label(frame, text = "\u2715", bootstyle = "danger", font=("Helvetica",20))
res_mul.grid(row = 2, column = 4 , pady =5, padx = 20, ipadx = 20,sticky="news")

result_mul = tb.Label(frame, bootstyle = "danger", font=("Helvetica",20))
result_mul.grid(row = 3, column = 4 , pady =5, padx = 20, ipadx = 20,sticky="news")

sep3 = tb.Separator(frame, orient="vertical", bootstyle = "warning")
sep3.grid(row = 2, column = 5 , pady =5, padx = 20, ipadx = 20,rowspan=3)

res_div = tb.Label(frame, text = "\u2797", bootstyle = "info", font=("Helvetica",20))
res_div.grid(row = 2, column = 6 , pady =5, padx = 20, ipadx = 20,sticky="news")

result_div = tb.Label(frame, bootstyle = "info", font=("Helvetica",20))
result_div.grid(row = 3, column = 6 , pady =5, padx = 20, ipadx = 20,sticky="news")

root.mainloop()