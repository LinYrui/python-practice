"""
用简单的函数式编程来实现学生信息管理系统的基本功能
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


#学生的数据
data = [
    {'name': 'Tom',
     'age': 18,
     'address': '上海',
     'id': '0001'
    },
    {'name': 'Amy',
     'age': 19,
     'address': '广州',
     'id': '0002'
      },
    {'name': 'Jack',
     'age': 20,
     'address': '深圳',
     'id': '0003'
    },
    {'name': 'Geoge',
     'age': 21,
     'address': '兰州',
     'id': '0004'
    }
       ]

def beauty_print(data_list):
    for index, student in enumerate(data_list):
        print(f'序号：{index}',end= ' \t')
        print(f'姓名：{student["name"]}', end=' \t')
        print(f'年龄：{student["age"]}', end=' \t')
        print(f'地址：{student["address"]}', end=' \t')
        print(f'学号：{student["id"]}')


def input_name():
    while True:
        name = input('请输入学生姓名：').strip()
        if name:
            return name
        else:
            continue

# 1.显示所有学生信息
def show_all_student():
        beauty_print(data)


#2.新建学生信息
def add_student():
    name = input_name()
    id = input('请输入学生学号：')
    address = input('请输入学生住址：')
    age = input('请输入学生年龄：')
    student = {'name': name,
               'age': age,
               'address': address,
               'id': id

               }
    data.append(student)


#3.查询学生信息
def find_imformation():
    n = input('请输入查询学生姓名:')
    for student in data:
        if student['name'] == n:
            print(student)
            break
    else:
        print('学生系统中没有该学生信息')


#4.修改学生信息
def change_student():
    n = input('请输入需要修改的学生姓名:')
    for student in data:
        if student['name'] == n:
            print(student)
            student['name'] = input('请输入修改后的学生姓名：')
            student['id'] = input('请输入修改后的学生学号：')
            student['address'] = input('请输入修改后的学生住址：')
            student['age'] = input('请输入修改后的学生年龄：')
            break
    else:
        print('学生系统中没有该学生信息')


#5.删除学生信息
def remove_student():
    n = input('请输入需要修改的学生姓名:')
    for student in data:
        if student['name'] == n:
            print(student)
            data.remove(student)
            print('已将该学生从系统中删除')
            break
    else:
        print('学生系统中没有该学生信息')


#0.退出系统
while True:
    print("""
     ————————————————————————————————————————
        欢迎使用【学生信息管理系统】，请按提示操作
        1. 显示所有学生信息
        2. 新建学生信息
        3. 查询学生信息
        4. 修改学生信息
        5. 删除学生信息
        0. 退出系统
     ————————————————————————————————————————
    """)
    op = input('请输入操作序号： ')
    if op == '1':
        show_all_student()
    elif op == '2':
        add_student()
    elif op == '3':
        find_imformation()
    elif op == '4':
        change_student()
    elif op == '5':
        remove_student()
    elif op == '0':
        print('已退出系统')
        break