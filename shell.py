#使用命令行，并连续获取输出，如ping
import subprocess
from time import sleep
ps = subprocess.Popen("ping 127.0.0.1", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
while ps.poll() is None:
    sleep(0.2)
    data = ps.stdout.readline().decode("gbk")
    print(data,end="")

data = ps.stdout.read().decode("gbk")
print(data,end="")

#Popen参考：https://blog.csdn.net/super_he_pi/article/details/99713374