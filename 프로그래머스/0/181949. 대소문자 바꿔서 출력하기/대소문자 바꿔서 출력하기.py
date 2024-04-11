str = input()
result = ''
for i in str :
    if i.islower() :
        result += i.upper()
    else :
        result += i.lower()
print(result)