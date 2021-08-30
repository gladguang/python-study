class User:
    def __init__(self):
        self.usr_info = {"seven": "123", "alex": "456"}

    def register(self):       # 定义注册方法
        print("&lt;注册模式&gt;".center(50, "*"))
        usr = input("请输入用户名：")
        pwd = input("请输入密码：")
        if usr in self.usr_info.keys():
            print("该用户已被注册，请重新输入新用户名！")
            self.register()
        else:
            self.usr_info[usr] = pwd
            print("注册成功，您的登录用户名是：%s 密码是：%s，" % (usr, pwd))
            x = input("是否使用新用户名密码登录?登录请输入1，退出请输入2：")
            if x == "1":
                self.login()
            else:
                print("退出系统，欢迎下次使用。")
                return

    def login(self):       # 定义登录方法

        print("&lt;登录模式&gt;".center(50, "*"))
        for i in range(3):
            usr = input("请输入用户名：")
            pwd = input("请输入密码：")
            if usr in self.usr_info.keys():
                if pwd == self.usr_info[usr]:
                    print("登录成功！")
                    break
                else:
                    print("密码输入错误，请重新输入！")
            else:
                print("用户名错误，请重新输入！")
            print("这是第%s次输入错误，还剩%s次机会。" % (i + 1, 2 - i))
        else:
            print("超过最大验证次数，登录失败！")


def main():             # 定义主函数
    user = User()     # 创建user对象
    print("欢迎使用智能XX管理系统-v1.0".center(100, "-"))
    print("注册请输入0,登录请输入1,退出请输入2".center(95, "-"))
    select = input("请选择您需要进行的操作：")
    if select == "0":
        user.register()     # 调用注册成员方法
    elif select == "1":
        user.login()
    elif select == "2":
        print("退出系统！欢迎再次使用。")
        return
    else:
        print("输入有误，请重新输入！")


main()