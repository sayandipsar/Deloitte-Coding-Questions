# Print index of each digit in the string
s = input()
r = ""
for i in range(len(s)):
    if s[i].isdigit():
        r = r+str(i)
print(r)
