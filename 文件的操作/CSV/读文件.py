""""
过程：
1、打开文件
2、读文件内容
3、关闭文件
"""

'''
1、打开文件
open(path,flag[,encoding][,errors])
path:要打开文件的路径
flag:打开方式
r     *以只读的方式打开文件,文件的描述符放在文件的开头
rb    *以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
r+    打开一个文件用于读写,文件的描述符放在文件的开头
w     *打开一个文件只用于写入，如果该文件已经存在会覆盖,如果不存在则创建新文件
wb    *打开一个文件只用于写入二进制，如果该文件已经存在会覆盖,如果不存在则创建新文件
w+    打开一个文件用于读写
a     打开一个文件用于追加，如果文件存在，文件描述符将会放到文件末尾
a+    
encoding:编码方式
errors:错误处理
'''