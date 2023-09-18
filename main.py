# with open('3.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(len(lines))
#     print(lines)
#     for line in lines:
#         print(line)
# n = 1
# while n < 4:
#     with open(f'{n}.txt', 'r', encoding='utf-8') as f:
#         data = f.read()
#         print(len(data))
#         print(type(data))
#         print(data)
#     n +=1

# n = 1
# while n < 4:
#     with open(f'{n}.txt', 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         print(len(lines))
#         print(type(lines))
#         for line in lines:
#             print(line)
#     n +=1

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
            print(dict_data[key])
            a = dict_data[key]

            print(a['name_file'])


