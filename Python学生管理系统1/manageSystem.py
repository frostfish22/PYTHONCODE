
from student import *
class StudentMange(object):
    def __init__(self):
        #列表方式存储学生信息
        self.Student_list=[]
    # TODO  程序的入口函数
    def run(self):
        # 1、加载文件里面的学员数据
        self.load_student()
        while True:
            #2、显示功能菜单
            self.show_menu()
            # 3、输入目标功能序号
            menu_num=int(input("请输入需要的功能需序号："))
            #4、根据用户输入的需要执行不同的功能
            if menu_num==1:
                # 添加学员
                self.add_Student()
            elif menu_num==2:
                self.del_Student()
            elif menu_num==3:
                self.modify_student()
            elif menu_num==4:
                self.search_student()
            elif menu_num==5:
                self.show_student()
            elif menu_num==6:
                self.save_student()
            elif menu_num==7:
                break
    #  系统菜单功能
    @staticmethod    #类、对象都可以调用
    # 2.1、显示功能菜单-------打印序号的功能对应的关系
    def show_menu():
        print("请选择如下功能")
        print("1、添加学员")
        print("2、删除学员")
        print("3、修改学员信息")
        print("4、查询学员信息")
        print("5、显示所有的学院信息")
        print("6、保存学员信息")
        print("7、退出系统")

    # 2.2、添加学员
    def add_Student(self):
        # 1、学员输入对应的姓名、性别、手机号
        name=input("请输入您的姓名：")
        gender=input("请输入您的性别：")
        tell=input("请输入您的手机号：")

        # 2、创建学员的对象------类  Student   在Studnet 文件里面，先导入Student模块再创建对象
        students=Student(name,gender,tell)

        # 3、对象添加到学员列表中
        self.Student_list.append(students)
        print(self.Student_list)
        print(students)

    # 2.3、删除新学员信息
    def del_Student(self):
        #1、用户输入目标学员姓名
        del_name=input("亲输入需要删除的学员姓名：")
        #2、遍历学员的列表，用户输入的学员存在则删除学员对象，否则提示不存在
        for i in self.Student_list:
            if del_name==i.name:
                self.Student_list.remove(i)
                break
            else:
                #循环正常结束，循环结束没有删除任何一个人，说明用户输入的目标学员不存在
                print("查无此人")
        print(self.Student_list)
    # 2.4、修改学员信息
    def modify_student(self):
        # 1、输入目标学员姓名
        modify_name=input("请输入要修改的学员性别：")
        #2、遍历列表数据，如果学员存在修改姓名、性别、手机号，否则提示学员不存在
        for i in self.Student_list:
            if modify_name==i.name:
                i.name=input("姓名：")
                i.gender=input("性别：")
                i.tell=input("号码：")
                print(f"修改学员的信息成功，姓名{i.name},性别{i.gender},号码{i.tell}")
                break
        else:
            print("查无此人")
    #2.5、查询学员信息
    def search_student(self):
        # 1、用户输入目标学员姓名
        search_name=input("要搜索的学员姓名")
        # 2、遍历列表，有就打印学员信息，否则提示学员不存在
        for i in self.Student_list:
            if search_name==i.name:
                print("姓名是{i.name},性别是{i.gender},号码是{i.tell}")
                print(f"姓名是{i.name},性别是{i.gender},号码是{i.tell}")
                break
        else:
            print("查无此人")

    # 2.6 、显示所有的学员信息
    def show_student(self):
        # 1、打印我们的表头
        print("姓名：\t性别：\t手机号；")
        # 2、打印学员数据
        for i in self.Student_list:
            print(f"{i.name}\t{i.gender}\t{i.tell}")
    # 2.7 、保存学员信息
    def save_student(self):
        # 1、打开文件
        f=open("student.data","w")
        # 2.1、文件写入数据   学员对象转换为字典
        new_list=[i.__dict__ for i in self.Student_list]
        # 2.2、文件写入字符串数据
        f.write(str(new_list))
        # 3、关闭文件
        f.close()
    # 2.8 加载学员信息
    def load_student(self):
        # 1、打开文件，尝试r打开  有异常就用w
        try:
            f=open("student.data","r")
        except:
            f=open("student.data","w")
        else:
            # 2、读取数据   读取的数据是字符串还原列表类型[{}],转换成学员对象[]
            data=f.read()  #必然是个字符串
            new_list=eval(data)  #转换成字典数据
            self.Student_list=[Student(i["name"],i["gender"],i["tell"]) for i in new_list]
        finally:
            # 3、关闭文件
            f.close()




if __name__ == "__main__":
    Student_manage=StudentMange()
    StudentMange().run()


