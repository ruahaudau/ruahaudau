d_1 = {}
d_1['key_1'] = 'first value'
d_1['key_2'] = 2
d_1['key_3'] = 3.14
d_1['key_4'] = True
d_1['key_5'] = [4, 2, 1]
d_1['key_6'] = {'inner_key': 3}

print(d_1.values())

list_1 = list(d_1.values())
list_2 = list(d_1.keys())
#print(list_1)
#print(list_2)
d_2 = dict(zip(list_2, list_1))

for key in d_1:
    a = d_1.get(key)
    print(a)


print('key_7' in d_1)
print('key_6' in d_1)
print(3.14 in d_1)
print('first value' in d_1)
      