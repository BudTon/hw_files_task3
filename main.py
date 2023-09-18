len_list = []
dict_data = {}
n = 1
while n < 4:
    c = f'{n}.txt'
    n += 1
    with open(f'{c}', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        dict_data[len(lines)] = { 'name_file' : c, 'len_file' : len(lines), 'data_file' : lines}
        len_list.append(len(lines))
sort_len_list = sorted(len_list)
for l in sort_len_list:
    for key in dict_data:
        if l == key:
            result = dict_data[key]
            with open('result.txt', 'a', encoding='utf-8') as f:
                name_file = result['name_file']
                f.write(f'{name_file}\n')
                len_file = result['len_file']
                f.write(f'{len_file}\n')
                for data in result['data_file']:
                    f.write(data)
print('Ok')




