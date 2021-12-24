# Check first character is repeated or not if repeated return 1 else return 0
def check(a):
    mark = 1
    k = a[0]
    for j in range(0, len(a), 2):
        if(k != a[j]):
            mark = 0
    return(mark)


n = int(input())
for i in range(n):
    a = input()
    print(check(a))
