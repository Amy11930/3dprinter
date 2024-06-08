import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook 

def save_to_excel():
    printer_number = printer_number_entry.get()
    print_mechanism = print_mechanism_entry.get()
    estimated_time = estimated_time_entry.get()
    print_person = print_person_entry.get()

    if not (printer_number and print_mechanism and estimated_time and print_person):
        messagebox.showwarning("警告", "所有字段都必须填写!")
        return

    # 创建或加载Excel工作簿
    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "3D打印申请"
        
        # 如果文件已存在，则加载现有工作簿
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "3D打印申请"
        
        # 添加表头
        headers = ["打印机编号", "打印机制", "预计打印时间", "打印人员"]
        sheet.append(headers)
        
        # 添加数据行
        data = [printer_number, print_mechanism, estimated_time, print_person]
        sheet.append(data)
        
        # 保存Excel文件
        workbook.save("3D_Print_Application.xlsx")
        messagebox.showinfo("成功", "申请已保存到Excel文件。")
    except Exception as e:
        messagebox.showerror("错误", f"保存Excel文件时发生错误: {e}")

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
save_button = tk.Button(root, text="保存申请", command=save_to_excel)
save_button.grid(row=4, column=1, sticky="ew", pady=5)

# 运行主循环
root.mainloop()
