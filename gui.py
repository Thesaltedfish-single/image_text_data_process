import tkinter as tk  
from tkinter import font,messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD  
import re
from logic import annotate_data
import pandas as pd
file_list=["",""]
df = pd.DataFrame(columns=['guid', 'label'])  
def update_file_display(file_path, label): 
    if (".jpg" in file_path) :
        file_list[0]=file_path
        label.config(text=file_path)
    elif (".txt" in file_path):
        file_list[1]=file_path
        label.config(text=file_path)
def clear_file_display():  
    annotate_button.config(state='disabled')

def on_annotate():  
    has_txt_file = any(filename.endswith('.txt') for filename in file_list)
    if has_txt_file:  
        annotate_data(file_list[0], file_list[1],df)  
        clear_file_display()
    else:  
        print("No text file selected.")  

def on_drop(event):  
    # 获取拖放的文件列表  
    files = event.data.split()  # event.data 是一个包含所有文件路径的字符串  
    for file in files:
        file_path = re.sub('^.','',file,1)  # 将文件路径重新组合成一个字符串，用空格分隔  
        file_path = re.sub('.$','',file_path)
        if file_path.lower().endswith(('.jpg','.txt')):
            # 更新已存在的 file_info_label 而不是创建一个新的 Label    
            update_file_display(file_path,file_info_label)
            annotate_button.config(state='normal')  
        else:
            messagebox.showerror("Error", "请拖入txt或者jpg文件")  
  
root = TkinterDnD.Tk()  
root.title("数据打包处理")  
  
# 创建一个可以接收文件的区域  
frame = tk.Frame(root, width=300, height=200, bg='lightgrey')  
frame.pack(pady=20, fill=tk.BOTH, expand=True)  
initial_text = "请把文件拖入这里"  
label_font = font.Font(family='Helvetica', size=20, weight='bold')  
label = tk.Label(frame, text=initial_text, bg='lightgrey', font=label_font)  
label.pack()  
  
# 创建一个Frame用于显示文件信息  
info_frame = tk.Frame(root, bg='white', bd=1, relief='sunken')  
info_frame.pack(fill=tk.X, expand=False)  # 修改为使用 pack 而不是 place  
  
# 在Frame中添加一个Label用于显示文件信息  
file_info_label = tk.Label(info_frame, text="", bg='white', wraplength=300, justify='left')  
file_info_label.pack(fill=tk.X, expand=True)  # 水平填充并允许扩展  

# 禁用按钮直到有文本文件被拖入  
annotate_button = tk.Button(root, text="Annotate", command=on_annotate, state='disabled')  
annotate_button.pack(pady=10) 


# 绑定拖放文件事件  
frame.drop_target_register(DND_FILES)  
frame.dnd_bind('<<Drop>>', on_drop)  
  
root.mainloop()