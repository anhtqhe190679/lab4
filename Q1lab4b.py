def phan1():
    file = 'poem.txt'
    with open(file, 'w') as file:
        for line in file:
            print(line.strip())
        
            
def phan2():
    try:
        story = 'story.txt'
        count = 0
        with open(story, 'w') as file:
            for line in file:
                if not line.strip().startswith('T'):
                    count += 1
        return count
    except :
        print("Không tìm thấy file 'story.txt'")

print("Nội dung file 'poem.txt':")
phan1()

print(f"Số dòng không có chữ 'T' đầu tiên trong file 'story.txt': {phan2()}")
