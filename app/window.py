# coding:utf-8
import tkinter.filedialog
from tkinter import *
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Openfile(object):
    """创建文件类"""

    def __init__(self, pattern):
        self.pattern = pattern

    def handle_cad(self):
        """处理CAD矢量图片"""
        pass

    def select_picture(self):
        """确定目标文件并打开文件列表"""
        filename = tkinter.filedialog.askopenfilenames(
            filetypes=[("." + self.pattern + "格式", "." + self.pattern), ('All Files', '*')])
        length = len(filename)
        if length == 0:
            label.config(text="您当前没有选择任何文件")
        else:
            picture = list(filename)[0]
            label.config(text="您选择的文件是：" + picture)
            print("您选择的文件是：" + picture)
            # 读取图片文件
            lena = mpimg.imread(picture, format=self.pattern)
            # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理, (512, 512, 3)
            lena.shape
            # 显示图片
            plt.imshow(lena)
            # 是否显示坐标轴 on/off
            plt.axis('off')
            plt.show()


if __name__ == "__main__":
    # 初始化 Tk
    root = Tk()
    # 菜单标题
    root.wm_title("选择要打开的文件")
    # 设置 窗口位置
    root.geometry('600x500+600+300')
    # 创建一个label
    label = Label(root, text='')
    # 显示label，必须含有此语句
    label.pack()
    # 实例化 Openfile 类
    opf = Openfile("svg")
    btn = Button(root, text="弹出选择文件对话框", command=opf.select_picture)
    # 窗口显示，持续显示
    btn.pack()
    root.mainloop()
