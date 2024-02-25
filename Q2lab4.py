def phan1():
    a = input('Nhập tên file bạn muốn mở: ')
    with open(a,'w') as file:
        new_content = input('Nhập content mới: ')
        text = input('Nhập nội dung: ')
        file.write(new_content)
        file.write(text)
        print('Done writting')
    while True:
        if new_content not in a:
            print('This is new content')
            break
        else:
            return False

def phan2():    
    b = input('Nhập file đã có sẵn: ')
    print('Opening file again....')
    with open(b,'w') as file:
        noi_dung = input('Nhập nội dung mới: ')
        file.write(noi_dung)
        print('Nội dung mới đã được nhập')

def phan3():
    b = input('Nhập file đã có sẵn: ')
    print('Opening file again....')
    with open(b,'w') as file:
        text = input('Nhập chuỗi của bạn: ')
        text_list = text.split()
        for element in text_list:
            file.write(element + '\n')
        print(f'Các từ {text_list} đã được ghi vào file')
phan1()
phan2()
phan3()
   