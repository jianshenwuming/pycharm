"""
需求:进入系统显示系统功能界面，功能如下:
1、添加学员
2、删除学员
3、修改学员信息
4、查询学员信息
5、显示所有学员信息
6、退出系统
系统共 6 个功能，用户根据自己需求选取。
"""
print('='*30)
print('学生信息管理系统')
print('1.添加学生信息')
print('2.删除学生信息')
print('3.修改学生信息')
print('4.查询学生信息')
print('5.显示所有学员信息')
print('6.退出系统')
print('='*30)

stuInfo = [{'学号': '0010', '姓名': '张三', '手机号码': '123456'}, {'学号': '0001', '姓名': '李四', '手机号码': '123456'}]
def main():
    key = int(input('请输入功能序号：'))
    if key == 1:
        addInfo()  # 添加学员
    elif key == 2:
        delInfo()  # 删除学员
    elif key == 3:
        amendInfo()  # 修改学员信息
    elif key == 4:
        lookoutInfo()  # 查询学员
    elif key == 5:
        showstuInfo()  #显示所有学员
    elif key == 6:
        QuitConfirm = input('真的要退出吗？（y or n）：')
        if QuitConfirm == 'y':
            print("您已成功退出系统！")
        else:
            print('输入有误，请重新输入')
            main()


# 添加学员
def addInfo():
    newnum = input('请输入学号:')
    newname = input('请输入姓名:')
    newphone = input('输入手机号码:')
    newInfo = {}
    newInfo['学号'] = newnum
    newInfo['姓名'] = newname
    newInfo['手机号码'] = newphone
    stuInfo.append(newInfo)
    print(f"信息已成功录入，请检查：{stuInfo[-1]}")
    main()

# 删除学员
def delInfo():
    delName = input('请输入要删除的学员的姓名：')
    for i in stuInfo:
        if delName == i['姓名']:
            stuInfo.remove(i)
            print(f"信息已成功删除，请检查：{i}")
            main()
        else:
             print("该用户不存在")
    main()

#修改学员信息
def amendInfo():
    amendname = input('请输入要修改的学员的姓名：')
    for i in stuInfo:
        if amendname == i['姓名']:
            i['学号'] = input("请输入新的学号：")
            i['手机号码'] = input("请输入新的手机号码：")
            print(f"信息修改完毕，请检查：{i}")
            main()
    else:
        print("该学生不存在")
    main()

#查询学员信息
def lookoutInfo():
    lookname = input('请输入要查询的学员的姓名：')
    for i in stuInfo:
        if lookname == i['姓名']:
            print(f"该学生姓名：{i['姓名']}，学号：{i['学号']}，手机号码：{i['手机号码']}")
            main()
    else:
        print("查无此人，请重试！")

#显示所有学员
def showstuInfo():
    print('姓名\t学号\t\t手机号码')
    for i in stuInfo:
        print(f"{i['姓名']}\t{i['学号']}\t{i['手机号码']}")
    main()
main()

