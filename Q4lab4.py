import datetime
import os
files = ['file1.txt file2.txt file3.txt']
file = files.split()
for file in files:
    with open(file,'w') as file:
        file.write('')

def phan1():
    a = input('Nhập tên file muốn đổi tên: ')
    if os.path.exists(a):
        new_name = input('Nhập tên mới: ')
        os.rename(a, new_name)
        print(f"File đã được đổi tên từ {a} thành {new_name}")
    else:
        print(f'File {a} không tồn tại')


def phan2():
    a = input('Nhập tên file: ')
    new_name = input('Nhập tên mới: ')
    for filename in os.listdir():
        if filename.endswith('.txt'):
            old_path = os.path.join('path\to\folder',a)
            new_filename = filename.replace(a,new_name)
            new_path = os.path.join('path\to\folder')
            os.rename(a,new_name)
            print(f"{a} has been renamed to {new_name}")       


def phan3():
    for file_name in files:
        old_path = os.path.join('path\to\folder', file_name)
        new_file_name = file_name + '_new'
        new_path = os.path.join('path\to\folder', new_file_name)
        print(f"{old_path} has been renamed to {new_path}")


def phan4():
    file = input('Nhập tên file muốn đổi: ')
    with open(file,'w') as file:
        file.write('')
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = input('Nhập tên mới cho file: ')
    new_name = f"{name}_{time}"
    print(f"File has been renamed to {new_name}")


def phan5():
    file_name = input('Nhập file bạn muốn đổi tên: ')
    name, _ = os.path.splitext(file_name)
    new_extention = '.csv'
    new_name = f"{name}{new_extention}"
    os.rename(file_name, new_name)
    print(f"{file_name} has been renamed to {new_name}")


def phan6():
    a = input('Nhập file: ')
    old_path = '/old/path/{a}'
    file_name = os.path.basename(old_path)
    new_path = os.path.join("/new/path", file_name)
    print(f"{old_path} has been moved to {new_path}")

phan1()
phan2()
phan3()
phan4()
phan5()
phan6()
    
    