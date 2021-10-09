#input of dict_list can be taken from user also

dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

output = []
for dict in dict_list:
    f=0
    for o in output:
        if dict['name'] == o['name'] and dict['confidence'] == o['confidence']:
            f=1
            break
    if f==0:   
        output.append(dict)

print(output)
