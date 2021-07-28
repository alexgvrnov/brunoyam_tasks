dic = {1: 10, 2: 20, 3: 30, 4: 10, 'abc': 10, 99: 10, 777: 20}
dic_reversed = {}

for k, v in dic.items():
    if dic_reversed.get(v):
        temp_list = []

        if type(dic_reversed[v]) == list:
            temp_list.extend(dic_reversed[v])
            temp_list.append(k)
        else:
            temp_list.append(dic_reversed[v])
            temp_list.append(k)

        dic_reversed[v] = temp_list
        print(temp_list)
    else:
        dic_reversed[v] = k

print(dic)

print(dic_reversed)
