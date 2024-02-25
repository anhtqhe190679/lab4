def phan1(file_name):
    with open(file_name, 'r') as file:
        file.seek(0)  
        print("File handle at:", file.tell())

def phan2(file_name):
    with open(file_name, 'r') as file:
        file.seek(0, 2)  
        print("File handle at:", file.tell())

def phan3(file_name, offset):
    with open(file_name, 'r') as file:
        file.seek(offset, 0)  
        print("File handle at {}: {}".format(offset, file.tell()))

def phan4(file_name, offset):
    with open(file_name, 'r') as file:
        file.seek(offset, 0)  
        print("File handle at {}: {}".format(offset, file.tell()))

def phan5(file_name):
    with open(file_name, 'r') as file:
        print("Current position of file handle:", file.tell())

file_name = input('Nhập tên file muốn mở: ')
text = input('Nhập nội dung muốn ghi: ')
with open(file_name, 'w') as file:
    file.write(text)

phan1(file_name)
phan2(file_name)
phan3(file_name, 5)
phan4(file_name, 5)
phan5(file_name)
