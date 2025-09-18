"""
用python的基础知识，数据类型，函数，面向对讲以及json做一个学生管理系统
实现：
学生信息添加，学生信息包括：姓名，学号，年纪，专业，注册日期
显示所有学生
搜索学生
删除学生

"""
import json
import os
if os.path.exists("students.json"):#检查在当前目录下，学生信息是否存在，如果存在，则以阅读模式打开
    with open("students.json","r") as f:#命名为f文件
        students = json.load(f)
else:
    students ={} #若不存在，则创建一个字典用于保存学生信息
#  初始化当前用户信息，当前无用户登录
students_user = None

#  创建一个函数，用于保存学生信息，并使用异常处理bug
def save_students():
    try:
        with open("students.json","w") as f:
            json.dump(students,f)
            print("数据保存成功")
    except Exception as e:
        print("数据保存失败，{e}")# 将失败原因输出


#创建函数，用于学生信息注册
def register():
    print("\n======用户注册======")
#  写个循环，防止失误退出
    while True:
        student_name = input("请输入姓名：")
        students_id = input("请输入学号：")
        student_age = input("请输入年龄：")
        student_major = input("请输入你的专业：")
        if students_id in students:
            print("当前学号已存在")
            continue
        else:
            students[students_id] = {  #  将学生的id作为字典的键，并在其中创建一个新字典，储存学生信息
                "student_name":student_name,
                "student_id":students_id,
                "student_age":student_age,
                "student_major":student_major
            }
#  调用save函数，保存信息
            save_students()
            print("信息注册成功")
            return True  #  返回True表示注册成功
# 创建函数，登录
def login():
    global students_user
    while True:
        name = input("请输入姓名：\n")
        student_id = (input("请输入学号(按t退出)：\n"))
        if student_id =="t":
            return
        elif student_id not in students:
            print("该信息不存在")
            continue
        else:
            if student_id == students[student_id]["student_id"]:
                students_user = name
                print("登录成功，欢迎你，{}同学".format(name))

                return True
            else:
                print("姓名或学号错误")
                continue


#创建函数，实现查询学生信息功能
def query_students(query_id):
    while True:
        if query_id == "t":
            break
        elif query_id in students:
            xin = students[query_id]
            print(xin)
        else:
            print("该学号不存在")

# 创建函数，显示所有的学生
def show_students():
    print("\n======显示全部学生======")
    print(students)


# 创建函数，删除学生
def del_student(del_id):
    print("\n======删除信息======")
    while True:
        del_id = input("请输入需要删除的学生学号(按t退出)：")
        again_del_id = input("请再次输入：")
        if del_id == "t":
            break
        elif del_id in students and del_id == again_del_id :
            del students[del_id]
            print("成功删除")
        else:
            print("该学号不存在")
# 创建主菜单
def main_menu():
    print("\n======欢迎来到三七的学生管理系统======\n")
    print(
            "1.登录\n"
            "2.注册\n"
            "3.退出\n")
    return input("请选择你的操作\n")


# 创建功能菜单
def func_menu():
    print("\n======操作选择======\n")
    print("1.查询学生信息\n"
          "2.显示所有学生信息\n"
          "3.删除学生信息\n"
          "4.退出\n")
    return input("请选择你的操作：\n")

# 创建主系统
def main_system():
    global students_user
    while True:
        if not students_user :
            choose = main_menu()
            if choose == "1":
                login()
            elif choose == "2":
                register()
            elif choose == "3":
                break
            else:
                print("没有该功能")
                continue
        try:
            choose = func_menu()
            if choose == "1":
                query_id = input("请输入学号：")
                query_students(query_id)
            elif choose == "2":
                show_students()
            elif choose == "3":
                del_id = input("请输入需要删除的学生学号(按t退出)：")
                del_student(del_id)
            elif choose == "4":
                break
            else:
                print("没有该功能")
                continue
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main_system()
    print("感谢使用三七的学生管理系统")


