string = input().upper()
answer = []
for i in set(string) :
    if answer == [] or answer[1] < string.count(i) :
        answer = [i, string.count(i)]
    elif answer[1] == string.count(i) :
        answer[0] = "?"
print(answer[0])
