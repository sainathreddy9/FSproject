import json

with open("colors.json") as f:
    data = json.load(f)

## print(data)
print('Rama', '_____________________________________________', 'Jalla')
count=0
for color in data['colors']:
    print(color['color'], color)

    print(count)
    if color['color'] == 'white':
        del data['colors'][count]
    '''del color['category']'''
    count = count + 1
    print(count)

print(color)
'''item_dict = json.loads(data)
print len(item_dict['result'][0]['run'])'''
print(len(data['colors']))
del color
print(len(data['colors']))
with open("colors.json", 'w') as f1:
    json.dump(data, f1, indent=2)