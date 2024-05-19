import tkinter as tk  
from tkinter import filedialog, messagebox ,simpledialog

import pandas as pd  
import os  
import uuid  
from PIL import Image  

def open_image_file():  
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])  
    if filepath:  
        return filepath  
    return None  
  
def open_text_file():  
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  
    if filepath:  
        return filepath  
    return None  
  
# GUID生成函数  
def generate_guid():  
    return str(uuid.uuid4())  
  
# 数据保存函数  
def save_data(df, data):  
    new_data_df = pd.DataFrame([data])  
    if not os.path.exists('data.csv'):  
        df.to_csv('data.csv', sep='\t', index=False)  
        existing_df = pd.read_csv('data.csv', sep='\t')  # 使用相同的分隔符读取数据  
        combined_df = pd.concat([existing_df, new_data_df], ignore_index=True)  
        combined_df.to_csv('data.csv', sep='\t', index=False)  # 使用相同的分隔符保存数据  
    else:  
        # 如果文件已存在，则读取现有数据，追加新数据，并保存回文件  
        existing_df = pd.read_csv('data.csv', sep='\t')  # 使用相同的分隔符读取数据  
        combined_df = pd.concat([existing_df, new_data_df], ignore_index=True)  
        combined_df.to_csv('data.csv', sep='\t', index=False)  # 使用相同的分隔符保存数据  


  
# 数据标注函数（此处简化为一个输入框，输入标签）  
def annotate_data(image_path, text_path,df):  
    '''
    image_path:图片
    text_path：文本
    '''
    csv_file_path='data.csv'
    label = simpledialog.askstring("输入标签", "请输入这条数据的标签：")  
    if label is None:  # 用户取消操作  
        return  
    guid = generate_guid()  
    image_tag=True
    if image_path =='':
        new_image_path=""
        image_tag=False
    else:
        new_image_path = f"{guid}{os.path.splitext(image_path)[1]}"  
    new_text_path = f"{guid}.txt"  
      
    # 重命名文件  
    if image_tag:
       os.rename(image_path, new_image_path)  
    os.rename(text_path, new_text_path)  
      
    # 添加到数据框  
    data = {  
        'guid': guid,  
        'label': label  
    }  
    save_data(df,data)  
    messagebox.showinfo("成功", "数据已标注并保存！")  
  

