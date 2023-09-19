def read_file(file_names):
    dict_data = {}
    for name in file_names:
       with open(f'{name}', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            dict_data[len(lines)] = { 'name_file' : name, 'len_file' : len(lines), 'data_file' : lines}
    return dict_data

def write_file(dict_data):
    sort_len_list = sorted(list(dict_data.keys()))
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

write_file(read_file(['1.txt', '2.txt','3.txt']))

print('Ok')




