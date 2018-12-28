import re


# 打开文件并读取
name_dict = {}
def func(filename):
    with open(filename, encoding='utf-8') as f:
        # print(f.read())
        for line in f:
            names = line.split('|')
            # print(names)
            for n in names:
                # print(n)
                name_num = find_item(n)
                name_dict[n] = name_num

# 返回人物或者兵器的数量
def find_item(hero):
    with open('sanguo.txt',encoding='utf-8') as f:
        data = f.read().replace('\n','')
        # print(data)
        name_num = re.findall(hero,data)
        print('%s 出现了 %s 次' %(hero,len(name_num)))


    return name_num

func('name.txt')
# func('weapon.txt')
# func('sanguo.txt')