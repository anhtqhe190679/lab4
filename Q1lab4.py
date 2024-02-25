import datetime

def phan_1(name_file):
    with open(name_file,'w') as file:
        print(f'Tạo file {name_file} thành công')

def phan_2():
    name = input("Nhập tên cho file mới: ")
    with open(name,'w') as file:
        print(f"Tạo file {name} thành công")
        current_time = datetime.datetime.now()
        file.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"tạo file {name} có ngày tháng năm thành công")

def phan_3():
    name = input('Nhập tên file bảo mật: ')
    with open(name,'w', encoding='utf-8') as file:
        print('tạo file {name} có bảo mật thành công')
    
phan_1("sales.txt")
phan_2()
phan_3()