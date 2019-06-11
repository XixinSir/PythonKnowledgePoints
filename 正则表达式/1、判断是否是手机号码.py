import re
def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":  # 注意str[0]字符形式 判断的时候要注意这一点
        return False
    elif str[1:3]!= "38" and str[1:3]!="39":
        return False
    for i in range(3,11):
        if str[i]>"9" or str[i]<"0":
            return False
    return True
print(checkPhone("13812345678"))
print(checkPhone("13912345678"))
print(checkPhone("138012345678"))
print(checkPhone("138a12345678"))




def checkPhone1(str):
    # 13912345678
    pat=r"^1[34578]\d{9}$"
    # pat=r"^1(([3578]\d)|(47))\d{8}$"
    res = re.match(pat,str)
    print(res)

checkPhone1("13812345678")
checkPhone1("13912345678")
checkPhone1("138012345678")
checkPhone1("138a12345678")



def checkPhone12(str):
    # 13912345678
    # pat=r"^1[34578]\d{9}$"
    pat=r"(1(([3578]\d)|(47))\d{8})"
    res = re.findall(pat,str)   # 返回的是组 要看括号的个数
    print(res)


print("从一串字符中提取出电话号码")
checkPhone12("fsdf13212345678jwoe4354fsf13523456789")

'''
QQ      6到10位,全是数字
'''
re_QQ=re.compile(r"^[1-9]\d{5,9}$") # 5到9个数字结尾
print(re_QQ.search("1234567890"))
print(re_QQ.search("0234567890"))
print(re_QQ.search("123456a890"))
print(re_QQ.search("12345674657890"))























'''
mail    1a@163.com
phone   010-55348765
user    数字、字母、下划线   6-12位
passwd
ip 
url  
'''
