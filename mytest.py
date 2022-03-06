import os
import glob

def list_save(filename, data):
    """filename 写入文件路径,data 列表."""
    file = open(filename,'w')#覆盖写入
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'  #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件("+filename+")成功")

def list_search(fpath,sx):
    """fpath 搜索路径,sx 后缀名 如txt"""
    #获取指定后缀文件全路径，反斜杠转正斜杠
    file_list=[name.replace('\\', '/') for name in glob.glob(fpath+"/*."+sx)]
    #print(file_list)
    return file_list

def cfg_read(fpath):
    """读取自动列表"""
    file = open(fpath,'r')#可读
    temp = file.readlines()
    file.close()
    return temp

def cfg_write(fpath,list):
    """写入自动列表"""
    file = open(fpath,'w')#覆盖写入
    file.writelines(list)
    file.close()

def cfg_getline(list,i):
    """读取第i行(真实行序号,非索引)"""
    return str(list[i-1]).replace('\n','')

def cfg_setline(list,i,text):
    """将text写入list的第i行(真实行序号,非索引)"""
    list[i-1]=text+'\n'

def list_getlines(ilist,_list):
    """一次性从_list中读取多行,
    ilist为int列表(真实行序号,非索引),
    返回值为新的list[str]"""
    #print(ilist)
    lines=[str(_list[i-1]).replace('\n','') for i in ilist]
    return lines

def list_setlines(ilist,_list,strlist):
    """一次性在_list中写入多行,
    strlist为要覆写的新字符串的列表,
    ilist为int列表(真实行序号,非索引)"""
    for i in range(len(ilist)):
        _list[ilist[i]-1]=strlist[i]+'\n'

def main():
    if(not os.path.exists("./temp/yolov3-tiny-train.cfg")):
        print("没有文件")
    pass
    

if __name__=='__main__':
    main()