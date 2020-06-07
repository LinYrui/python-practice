"""
用简面向对象编程来实现学生信息管理系统的基本功能
显示界面如下：
————————————————————————————————————————
欢迎使用【学生信息管理系统】，请按提示操作
  1. 显示所有学生信息
  2. 新建学生信息
  3. 查询学生信息
  4. 修改学生信息
  5. 删除学生信息
  0. 退出系统
————————————————————————————————————————
"""

from datetime import datetime

# 模拟的学生数据
data = [
    {'name': 'Tom',
     'address': '上海',
     'id': '0001',
     'birthday':'20020101'
    },
    {'name': 'Amy',
     'address': '广州',
     'id': '0002',
     'birthday':'20010101'
      },
    {'name': 'Jack',
     'address': '深圳',
     'id': '0003',
     'birthday':'20000101'
    },
    {'name': 'Geoge',
     'address': '兰州',
     'id': '0004',
     'birthday':'19990101'
    }
       ]


# 学生类
class Student:
    # 学生初始化
    def __init__(self, name, birthday, address, id):
        self.name = name
        self.address = address
        self.id = id
        self.birthday = birthday


    def get_age(self):
        this_year = datetime.now().year
        age = this_year - int(self.birthday[:4])
        return age


# 学生管理系统类
class System:
    def __init__(self, name):
        self.name = name
        self.data = []


    # 加载数据
    def load_data(self):
        for item in data:
            student = Student(item['name'], item['birthday'], item['address'], item['id'])
            self.data.append(student)


    # 启动学生管理系统
    def start(self):
        # 在系统启动时加载数据
        self.load_data()
        while True:
            self.show_menu()
            op = input('请输入操作序号： ')
            if op == '1':
                self.show_all_student(self.data)
            elif op == '2':
                self.create_student()
            elif op == '3':
                self.find_student()
            elif op == '4':
                self.change_student()
            elif op == '5':
                self.delet_student()
            elif op == '0':
                print('已退出系统')
                break
            else:
                print('请输入正确的操做序号')
                continue



    # 显示菜单
    def show_menu(self):
        print(f"""
                    ————————————————————————————————————————
                        欢迎使用【{self.name}】，请按提示操作
                          1. 显示所有学生信息
                          2. 新建学生信息
                          3. 查询学生信息
                          4. 修改学生信息
                          5. 删除学生信息
                          0. 退出系统
                    ————————————————————————————————————————
               """)


    # 1.显示所有学生信息
    def show_all_student(self, data_list):
        for index, student in enumerate(data_list):
            print(f'{index}  名字：{student.name:6}', end='\t')
            print(f'年龄：{student.get_age()}', end='\t')
            print(f'住址：{student.address}', end='\t')
            print(f'学号：{student.id}', end='\n')


    def input_name(self):
        while True:
            name = input('输入学生姓名：').strip()
            if name:
                return name
            else:
                continue


    # 2.新建学生信息
    def create_student(self):
        name = self.input_name()
        birthday = input('输入学生生日，如19990101：')
        address = input('输入学生家庭住址：')
        id = input('输入学生学号：')
        new_student = Student(name, birthday, address, id)
        self.data.append(new_student)


    # 3.查询学生信息
    def find_student(self):
        name = self.input_name()
        for student in self.data:
            if student.name == name:
                print(f'名字：{student.name:5}', end='\t')
                print(f'年龄：{student.get_age():3}', end='\t')
                print(f'住址：{student.address:5}', end='\t')
                print(f'学号：{student.id:5}', end='\n')
                break
        else:
                print('查无此人')


    # 4.修改学生信息
    def change_student(self):
        name = self.input_name()
        for student in self.data:
            if student.name == name:
                student.name = input('修改后的学生名字:')
                student.birthday = input('修改后的学生生日:')
                student.address = input('修改后的学生住址:')
                student.id = input('修改后的学生学号:')
                break
        else:
            print('查无此人')


    # 5.删除学生信息
    def delet_student(self):
        name = self.input_name()
        for student in self.data:
            if student.name == name:
                self.data.remove(student)
                print('已删除')
                break
        else:
            print('查无此人')




if __name__ == '__main__':
    student_sys = System('23333管理系统')
    student_sys.start()

