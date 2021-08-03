s= input()
new_s= s.casefold()
x=len(new_s)
new_s=new_s.replace('a', '')
new_s=new_s.replace('e', '')
new_s=new_s.replace('i', '')
new_s=new_s.replace('o', '')
new_s=new_s.replace('u', '')
new_s=new_s.replace('y', '')
new_s2=""
for letter in new_s:
    new_s2+=".%s"%letter
print(new_s2)