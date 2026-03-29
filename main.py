def show_menu():
    # 显示菜单
    print("---学生成绩管理系统---")
    print("1.添加学生")
    print("2.查看所有学生")
    print("3.删除学生")
    print("4.修改学生")
    print("5.查找学生")
    print("0.退出")

def add_student(students):
# 添加学生
    print("---添加学生---")
    stu_id = input("学号：")
#检查学号是否重复
    for s in students:
        if s['id'] == stu_id:
            print("学号已经存在，添加失败")
            return
        else:
            name = input("姓名：")
#输入成绩，并处理非法输入
    try:
        math = float(input("数学成绩:"))
        chinese = float(input("语文成绩"))
        english = float(input("英语成绩"))
    except  ValueError:
        print("成绩必须是数字，添加失败")
        return
    student = {
        'id': stu_id,
        'name': name,
        'math': math,
        'chinese':chinese,
        'english':english
    }
    students.append(student)
    print("添加成功")
