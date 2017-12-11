text = input()

splitted = text.split(' ')
result = ''

for c in splitted:
    result += format(int(c), '08b') + ' '

print(result)