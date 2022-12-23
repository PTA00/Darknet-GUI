# 导入wxPython包
from asyncio.windows_events import NULL
from cProfile import label
from multiprocessing.sharedctypes import Value
from time import sleep
from tkinter.messagebox import YESNOCANCEL
from tkinter.ttk import Style
from turtle import color
import wx
import os
#from mytest import *
import mytest

dlgstr1name=""
"""数据选择-目录-名称"""
dlgstr1=""
"""数据选择-目录"""
dlgstr2=""
"""训练集选择-txt文件"""
dlgstr3=""
"""测试集选择-txt文件"""
dlgstr4=""
"""类别名称-names文件"""
dlgstr5=""
"""保存路径-目录"""
dlgstr6=""
"""预训练模型-conv文件"""

rdlgstr1=""
"右侧-选择模型"
rdlgstr2=""
"右侧-选择cfg"
rdlgstr3=""
"右侧-选择data"


def an1(event):
    """数据选择-打开文件"""
    dlg = wx.DirDialog(mb,"选择文件夹",style=wx.DD_DEFAULT_STYLE)
    if dlg.ShowModal() == wx.ID_OK:
        global dlgstr1
        dlgstr1 = "."+dlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        shuru3.Value = dlgstr1
        print("文件夹路径 "+dlgstr1)#文件夹路径结尾不带斜杠
        global dlgstr1name
        dlgstr1name = dlgstr1.split('/')[-2]
        print("数据集名称:"+dlgstr1name)
    dlg.Destroy()
    pass

def an2(event):
    """训练集选择-打开文件"""
    fdlg = wx.FileDialog(mb,"选择文件",wildcard="TXT files (*.txt)|*.txt",style=wx.FD_OPEN)
    if fdlg.ShowModal() == wx.ID_OK:
        global dlgstr2
        dlgstr2 = "."+fdlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        shuru5.Value = dlgstr2
        print("txt路径 "+dlgstr2)
    fdlg.Destroy()
    pass

def an3(event):
    """测试集选择-打开文件"""
    fdlg = wx.FileDialog(mb,"选择文件",wildcard="TXT files (*.txt)|*.txt",style=wx.FD_OPEN)
    if fdlg.ShowModal() == wx.ID_OK:
        global dlgstr3
        dlgstr3 = "."+fdlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        shuru7.Value = dlgstr3
        print("txt路径 "+dlgstr3)
    fdlg.Destroy()
    pass

def an4(event):
    """类别名称-打开文件"""
    fdlg = wx.FileDialog(mb,"选择文件",wildcard="NAMES files (*.names)|*.names",style=wx.FD_OPEN)
    if fdlg.ShowModal() == wx.ID_OK:
        global dlgstr4
        dlgstr4 = "."+fdlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        shuru9.Value = dlgstr4
        print("names路径 "+dlgstr4)
    fdlg.Destroy()
    pass

def an5(event):
    """保存路径-打开文件"""
    dlg = wx.DirDialog(mb,"选择文件夹",style=wx.DD_DEFAULT_STYLE)
    if dlg.ShowModal() == wx.ID_OK:
        global dlgstr5
        dlgstr5 = "."+dlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        shuru11.Value = dlgstr5
        print("文件夹路径 "+dlgstr5)#文件夹路径结尾不带斜杠
    dlg.Destroy()
    pass

def an6(event):
    """预训练模型-打开文件"""
    fdlg = wx.FileDialog(mb,"选择文件",wildcard="CONV files (*.*)|*.*",style=wx.FD_OPEN)
    if fdlg.ShowModal() == wx.ID_OK:
        global dlgstr6
        dlgstr6 = "."+fdlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        shuru13.Value = dlgstr6
        print("conv路径 "+dlgstr6)
    fdlg.Destroy()
    pass

def an7(event):
    """生成训练测试集"""
    if(shuru15.Value == '' or dlgstr2 == '' or dlgstr3 == '' or dlgstr4 == '' or dlgstr5 == ''):
        msg = wx.MessageDialog(mb,"写入data文件:必须的路径或值为空","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return

    #生成train
    mytest.list_save(dlgstr2,mytest.list_search(dlgstr1,"png"))
    
    #生成valid
    mytest.list_save(dlgstr3,mytest.list_search(dlgstr1,"png"))
        
    #生成 数据目录名.data 保存到data文件夹
    data=[]
    data.append("classes = "+shuru15.Value)
    data.append("train = "+dlgstr2)
    data.append("valid = "+dlgstr3)
    data.append("names = "+dlgstr4)
    data.append("backup = "+dlgstr5)
    #print(data)
    mytest.list_save("./data/"+dlgstr1name+".data",data)
    print("写入("+"./data/"+dlgstr1name+".data"+")成功")

    if(dlgstr6=='' or shuru15.Value=='' or shuru17.Value=='' or shuru19.Value=='' or shuru20.Value=='' or shuru22.Value==''):
        msg = wx.MessageDialog(mb,"写入cfg文件:必须的路径或值为空","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return
    if(xuanze1.GetStringSelection()=='yolov3-tiny'):
        print("模型选择为:"+xuanze1.GetStringSelection())
        lstr = mytest.cfg_read("./cfg/"+xuanze1.GetStringSelection()+".cfg")
        #print(lstr)
        yolov3_tiny_lint=[
            20, # max_batches = 训练次数
            22, # steps=变化步数1,变化步数2
            135,# classes=类别数量
            177,# ↑
            127,# filters=特征数量
            171 # ↑
        ]
        # 测试行表对应内容
        # cc = mytest.list_getlines(yolov3_tiny_lint,lstr)
        # print(cc)
        yolov3_tiny_lstr=[
            "max_batches = "+shuru17.Value,
            "steps="+shuru19.Value+","+shuru20.Value,
            "classes="+shuru15.Value,
            "classes="+shuru15.Value,
            "filters="+shuru22.Value,
            "filters="+shuru22.Value
        ]
        #测试字符串表对应输入框内容
        #print(yolov3_tiny_lstr)

        #替换列表行
        mytest.list_setlines(yolov3_tiny_lint,lstr,yolov3_tiny_lstr)
        #输出teat版本(原始版本)cfg文件到temp目录
        mytest.cfg_write("./temp/"+xuanze1.GetStringSelection()+"-test.cfg",lstr)
        print("写入("+"./temp/"+xuanze1.GetStringSelection()+"-test.cfg"+")成功")

        #更改为train模式
        yolov3_tiny_train_lint=[
            3,#mytest
            4,
            6,#train
            7 
        ]
        yolov3_tiny_train_lstr=[str(temp).replace('#','') for temp in mytest.list_getlines(yolov3_tiny_train_lint,lstr)]
        #设置为train模式
        yolov3_tiny_train_lstr[0]="#"+yolov3_tiny_train_lstr[0]
        yolov3_tiny_train_lstr[1]="#"+yolov3_tiny_train_lstr[1]
        #print(yolov3_tiny_train_lstr)
        mytest.list_setlines(yolov3_tiny_train_lint,lstr,yolov3_tiny_train_lstr)
        mytest.cfg_write("./temp/"+xuanze1.GetStringSelection()+"-train.cfg",lstr)
        print("写入("+"./temp/"+xuanze1.GetStringSelection()+"-train.cfg"+")成功")
    
    
    
    
    pass

def an8(event):
    """开始训练"""
    
    #temp0=dlgstr6.split('/')[-1].split('.')[0]
    #print(temp0)
    # if(temp0!=xuanze1.GetStringSelection()):
    #     msg = wx.MessageDialog(mb,"模型类型和预训练模型不符","错误",wx.OK|wx.ICON_WARNING)
    #     msg.ShowModal()
    #     msg.Destroy()
    #     return
    
    
    # if(xuanze1.GetStringSelection()=='yolov3-tiny'):
    #     lstr=mytest.cfg_read("./cfg/"+xuanze1.GetStringSelection()+".cfg")
    #     yolov3_tiny_train_lint=[
    #         3,#mytest
    #         4,
    #         6,#train
    #         7 
    #     ]
    #     yolov3_tiny_train_lstr=[str(temp).replace('#','') for temp in mytest.list_getlines(yolov3_tiny_train_lint,lstr)]
    #     #设置为train模式
    #     yolov3_tiny_train_lstr[0]="#"+yolov3_tiny_train_lstr[0]
    #     yolov3_tiny_train_lstr[1]="#"+yolov3_tiny_train_lstr[1]
    #     #print(yolov3_tiny_train_lstr)
    #     mytest.list_setlines(yolov3_tiny_train_lint,lstr,yolov3_tiny_train_lstr)
    #     mytest.cfg_write("./cfg/"+xuanze1.GetStringSelection()+".cfg",lstr)
    #     print("已设置cfg文件为train模式")

    if(dlgstr1name=='' or shuru3.Value==''):
        msg = wx.MessageDialog(mb,"数据选择为空或无效","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return
    if(dlgstr6=='' or shuru13.Value==''):
        msg = wx.MessageDialog(mb,"预训练模型为空或无效","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return
    if(not os.path.exists("./temp/"+xuanze1.GetStringSelection()+"-train.cfg")):
        msg = wx.MessageDialog(mb,"没有从temp目录找到"+xuanze1.GetStringSelection()+"-train.cfg文件","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return
    shellstr="darknet detector train "+"./data/"+dlgstr1name+".data "+"./temp/"+xuanze1.GetStringSelection()+"-train.cfg "+dlgstr6
    #print(shellstr)
    os.system(shellstr)
    print("训练完成")

    pass

def an9(event):
    """继续训练"""
    # if(xuanze1.GetStringSelection()=='yolov3-tiny'):
    #     lstr=mytest.cfg_read("./cfg/"+xuanze1.GetStringSelection()+".cfg")
    #     yolov3_tiny_train_lint=[
    #         3,#mytest
    #         4,
    #         6,#train
    #         7 
    #     ]
    #     yolov3_tiny_train_lstr=[str(temp).replace('#','') for temp in mytest.list_getlines(yolov3_tiny_train_lint,lstr)]
    #     #设置为train模式
    #     yolov3_tiny_train_lstr[0]="#"+yolov3_tiny_train_lstr[0]
    #     yolov3_tiny_train_lstr[1]="#"+yolov3_tiny_train_lstr[1]
    #     #print(yolov3_tiny_train_lstr)
    #     mytest.list_setlines(yolov3_tiny_train_lint,lstr,yolov3_tiny_train_lstr)
    #     mytest.cfg_write("./cfg/"+xuanze1.GetStringSelection()+".cfg",lstr)
    #     print("已设置cfg文件为train模式")

    if(dlgstr5=='' or shuru11.Value==''):
        msg = wx.MessageDialog(mb,"保存路径为空或无效","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return

    if(dlgstr1name=='' or shuru3.Value==''):
        msg = wx.MessageDialog(mb,"数据选择为空或无效","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return

    wlist = mytest.list_search(dlgstr5,"weights")
    if(wlist==[]):
        msg = wx.MessageDialog(mb,"没有从保存路径的目录内找到任何weights文件","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return
    
    if(not os.path.exists("./temp/"+xuanze1.GetStringSelection()+"-train.cfg")):
        msg = wx.MessageDialog(mb,"没有从temp目录找到"+xuanze1.GetStringSelection()+"-train.cfg文件","错误",wx.OK|wx.ICON_WARNING)
        msg.ShowModal()
        msg.Destroy()
        return

    print("选择weights文件:"+wlist[-1])
    shellstr="darknet detector train "+"./data/"+dlgstr1name+".data "+"./temp/"+xuanze1.GetStringSelection()+"-train.cfg "+wlist[-1]
    #print(shellstr)
    os.system(shellstr)
    print("继续训练完成")

    pass

def an10(event):
    """选择模型"""
    fdlg = wx.FileDialog(mb,"选择文件",wildcard="WEIGHTS files (*.weights)|*.weights",style=wx.FD_OPEN)
    if fdlg.ShowModal() == wx.ID_OK:
        global rdlgstr1
        rdlgstr1 = "."+fdlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        print("weights路径 "+rdlgstr1)
    fdlg.Destroy()
    pass

def an11(event):
    """选择cfg"""
    fdlg = wx.FileDialog(mb,"选择文件",wildcard="CFG files (*.cfg)|*.cfg",style=wx.FD_OPEN)
    if fdlg.ShowModal() == wx.ID_OK:
        global rdlgstr2
        rdlgstr2 = "."+fdlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        print("weights路径 "+rdlgstr2)
    fdlg.Destroy()
    pass

def an12(event):
    """选择data"""
    fdlg = wx.FileDialog(mb,"选择文件",wildcard="DATA files (*.data)|*.data",style=wx.FD_OPEN)
    if fdlg.ShowModal() == wx.ID_OK:
        global rdlgstr3
        rdlgstr3 = "."+fdlg.GetPath().replace(os.getcwd(),'').replace('\\', '/')
        print("weights路径 "+rdlgstr3)
    fdlg.Destroy()
    pass

def an13(event):
    """图片测试"""
    pass

def an14(event):
    """视频测试"""
    pass

def xz1(event):
    print("选择:"+xuanze1.GetStringSelection())



# 创建一个应用程序对象
app = wx.App()

# 框架
frm = wx.Frame(None, title="gui",pos=wx.DefaultPosition,size=(800,450))
frm.SetBackgroundColour((240,240,240))
mb=wx.Panel(frm)

shuru1 = wx.TextCtrl(mb,pos=(5,5),size=(174,25),value="模型类型:",style=wx.TE_CENTER|wx.TE_READONLY)
"""模型类型"""
#从cfg文件夹中读取模型类型
file_list=os.listdir("./cfg")
#获取到纯文件名
list1=[os.path.splitext(file)[0] for file in file_list]
xuanze1=wx.Choice(mb,choices=list1,pos=(184,5),size=(170,25))
#模型类型默认选第一个
xuanze1.Selection = 0
"""模型类型-选择"""
xuanze1.Bind(wx.EVT_CHOICE,xz1)

shuru2 = wx.TextCtrl(mb,pos=(5,35),size=(70,25),value="数据选择:",style=wx.TE_CENTER|wx.TE_READONLY)
"""数据选择"""
shuru3 = wx.TextCtrl(mb,pos=(80,35),size=(200,25),value="")
"""数据选择-内容"""
anniu1 = wx.Button(mb,pos=(285,33),size=(70,29),label="打开文件")
"""数据选择-打开文件"""
anniu1.Bind(wx.EVT_BUTTON,an1)

shuru4 = wx.TextCtrl(mb,pos=(5,65),size=(80,25),value="训练集选择:",style=wx.TE_CENTER|wx.TE_READONLY)
"""训练集选择"""
shuru5 = wx.TextCtrl(mb,pos=(90,65),size=(200,25),value="")
"""训练集选择-内容"""
anniu2 = wx.Button(mb,pos=(295,63),size=(60,29),label="打开文件")
"""训练集选择-打开文件"""
anniu2.Bind(wx.EVT_BUTTON,an2)

shuru6 = wx.TextCtrl(mb,pos=(5,95),size=(80,25),value="测试集选择:",style=wx.TE_CENTER|wx.TE_READONLY)
"""测试集选择"""
shuru7 = wx.TextCtrl(mb,pos=(90,95),size=(200,25),value="")
"""测试集选择-内容"""
anniu3 = wx.Button(mb,pos=(295,93),size=(60,29),label="打开文件")
"""测试集选择-打开文件"""
anniu3.Bind(wx.EVT_BUTTON,an3)

shuru8 = wx.TextCtrl(mb,pos=(5,125),size=(80,25),value="类别名称:",style=wx.TE_CENTER|wx.TE_READONLY)
"""类别名称"""
shuru9 = wx.TextCtrl(mb,pos=(90,125),size=(200,25),value="")
"""类别名称-内容"""
anniu4 = wx.Button(mb,pos=(295,123),size=(60,29),label="打开文件")
"""类别名称-打开文件"""
anniu4.Bind(wx.EVT_BUTTON,an4)

shuru10 = wx.TextCtrl(mb,pos=(5,155),size=(80,25),value="保存路径:",style=wx.TE_CENTER|wx.TE_READONLY)
"""保存路径"""
shuru11 = wx.TextCtrl(mb,pos=(90,155),size=(200,25),value="")
"""保存路径-内容"""
anniu5 = wx.Button(mb,pos=(295,153),size=(60,29),label="打开文件")
"""保存路径-打开文件"""
anniu5.Bind(wx.EVT_BUTTON,an5)

shuru12 = wx.TextCtrl(mb,pos=(5,185),size=(80,25),value="预训练模型:",style=wx.TE_CENTER|wx.TE_READONLY)
"""预训练模型"""
shuru13 = wx.TextCtrl(mb,pos=(90,185),size=(200,25),value="")
"""预训练模型-内容"""
anniu6 = wx.Button(mb,pos=(295,183),size=(60,29),label="打开文件")
"""预训练模型-打开文件"""
anniu6.Bind(wx.EVT_BUTTON,an6)

shuru14 = wx.TextCtrl(mb,pos=(5,215),size=(160,25),value="类别数量:",style=wx.TE_CENTER|wx.TE_READONLY)
"""类别数量"""
shuru15 = wx.TextCtrl(mb,pos=(170,215),size=(184,25),value="",style=wx.TE_CENTER)
"""类别数量-内容"""

shuru16 = wx.TextCtrl(mb,pos=(5,245),size=(160,25),value="训练次数:",style=wx.TE_CENTER|wx.TE_READONLY)
"""训练次数"""
shuru17 = wx.TextCtrl(mb,pos=(170,245),size=(184,25),value="",style=wx.TE_CENTER)
"""训练次数-内容"""

shuru18 = wx.TextCtrl(mb,pos=(5,275),size=(116,25),value="变化步数:",style=wx.TE_CENTER|wx.TE_READONLY)
"""变化步数"""
shuru19 = wx.TextCtrl(mb,pos=(126,275),size=(112,25),value="",style=wx.TE_CENTER)
"""变化步数-内容1"""
shuru20 = wx.TextCtrl(mb,pos=(242,275),size=(112,25),value="",style=wx.TE_CENTER)
"""变化步数-内容2"""

shuru21 = wx.TextCtrl(mb,pos=(5,305),size=(160,25),value="特征数量:",style=wx.TE_CENTER|wx.TE_READONLY)
"""特征数量"""
shuru22 = wx.TextCtrl(mb,pos=(170,305),size=(184,25),value="",style=wx.TE_CENTER)
"""特征数量-内容"""

anniu7 = wx.Button(mb,pos=(5,340),size=(114,48),label="生成训练测试集")
"""生成训练测试集"""
anniu7.Bind(wx.EVT_BUTTON,an7)
anniu8 = wx.Button(mb,pos=(124,340),size=(113,48),label="开始训练")
"""开始训练"""
anniu8.Bind(wx.EVT_BUTTON,an8)
anniu9 = wx.Button(mb,pos=(242,340),size=(113,48),label="继续训练")
"""继续训练"""
anniu9.Bind(wx.EVT_BUTTON,an9)

anniu10 = wx.Button(mb,pos=(360,340),size=(100,48),label="选择模型")
"""选择模型"""
anniu10.Bind(wx.EVT_BUTTON,an10)
anniu11 = wx.Button(mb,pos=(465,338),size=(80,26),label="选择cfg")
"""选择cfg"""
anniu11.Bind(wx.EVT_BUTTON,an11)
anniu12 = wx.Button(mb,pos=(465,364),size=(80,26),label="选择data")
"""选择data"""
anniu12.Bind(wx.EVT_BUTTON,an12)
anniu13 = wx.Button(mb,pos=(550,340),size=(100,48),label="图片测试")
"""图片测试"""
anniu13.Bind(wx.EVT_BUTTON,an13)
anniu14 = wx.Button(mb,pos=(654,340),size=(100,48),label="视频测试")
"""视频测试"""
anniu14.Bind(wx.EVT_BUTTON,an14)


# 指定居中对齐的的静态文本  
label1 = wx.StaticText(mb,label="测试显示框",pos=(490,150),size=(-1,-1),style=wx.ALIGN_CENTER)  
font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
label1.SetFont(font)

#显示图片
# image = wx.Image('1.png',wx.BITMAP_TYPE_PNG)
# if image.Width > 400 or image.Height > 330:
#     if image.Width > image.Height:
#         image.Rescale(400,image.Height*(400/image.Width),wx.IMAGE_QUALITY_HIGH)
#     else:
#         image.Rescale(int(image.Width*(330/image.Height)),330,wx.IMAGE_QUALITY_HIGH)
# temp = image.ConvertToBitmap()
# bmp = wx.StaticBitmap(mb, bitmap=temp,pos=(360,5),size=(400,330))








# 显示
frm.Show()

# 启动事件循环
app.MainLoop()

