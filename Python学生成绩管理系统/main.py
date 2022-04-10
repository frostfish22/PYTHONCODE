from tkinter import *
from Login import *
import tkinter as tk

root = tk.Tk() #定义窗口
root.title('欢迎进入学生成绩管理系统') #定义窗口标题
LoginPage(root) #调用类（窗口所有功能在类里面实现） （这种方式类似继承）
root.mainloop() #打开窗口