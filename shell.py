#使用命令行，并连续获取输出，如ping
# import subprocess
# ps = subprocess.Popen(shuru1.Value, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#     while True:

#         sleep(0.2)
#         if ps.poll() is None:
#             data = ps.stdout.readline().decode("gbk")
#             print(data,end="")
#         else:
#             data = ps.stdout.read().decode("gbk")
#             print(data,end="")
#             return