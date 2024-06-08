import tkinter as tk
from tkinter import messagebox

def save_to_text():
    printer_number = printer_number_entry.get()
    print_mechanism = print_mechanism_entry.get()
    estimated_time = estimated_time_entry.get()
    print_person = print_person_entry.get()

    if not (printer_number and print_mechanism and estimated_time and print_person):
        messagebox.showwarning("警告", "所有字段都必须填写!")
        return

    with open("3D_Print_Application.txt", "w") as file:
        file.write(f"打印机编号: {printer_number}\n")
        file.write(f"打印机制: {print_mechanism}\n")
        file.write(f"预计打印时间: {estimated_time}\n")
        file.write(f"打印人员: {print_person}\n")

    messagebox.showinfo("成功", "申请已保存到文本文件。")

# 创建主窗口
root = tk.Tk()
root.title("3D打印申请")

# 设置输入字段
printer_number_label = tk.Label(root, text="打印机编号:")
printer_number_label.grid(row=0, column=0, sticky="e")
printer_number_entry = tk.Entry(root)
printer_number_entry.grid(row=0, column=1)

print_mechanism_label = tk.Label(root, text="打印机制:")
print_mechanism_label.grid(row=1, column=0, sticky="e")
print_mechanism_entry = tk.Entry(root)
print_mechanism_entry.grid(row=1, column=1)

estimated_time_label = tk.Label(root, text="预计打印时间:")
estimated_time_label.grid(row=2, column=0, sticky="e")
estimated_time_entry = tk.Entry(root)
estimated_time_entry.grid(row=2, column=1)

print_person_label = tk.Label(root, text="打印人员:")
print_person_label.grid(row=3, column=0, sticky="e")
print_person_entry = tk.Entry(root)
print_person_entry.grid(row=3, column=1)

# 设置保存按钮
save_button = tk.Button(root, text="保存申请", command=save_to_text)
save_button.grid(row=4, column=1, sticky="ew", pady=5)

# 运行主循环
root.mainloop()
