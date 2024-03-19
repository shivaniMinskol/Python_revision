# $x("//")

# palindrome:-

str="madam"
rev_str=str[::-1]
print(rev_str)

if rev_str == str:
    print("given string is palindrome")
else:
    print("not palindrome")
# ------------------------------------------
# python learning am i
str2= "i am learning python"

s=str2.split()
print(s)

s2= s[::-1]
print(s2)

output= ' '.join(s2)
print(output)
# ---------------------------------------

str3= "i am learning python"
l = str3.split()
print(l)

l2= []

for i in l:
    # print(i)
    l2.append(i[::-1])

print(l2)
output2= " ".join(l2)
print(output2)

# -------------------------------------------------

str4 = "Prograamming"
duplicate=[]

for i in str4:
    if str4.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)

print(duplicate)
# ----------------------------------------

li=[80,70,90,50,60,40,30,20,10,100]
# lis.sort()
# print(lis)
for i in range(0,len(li)):
    for j in range(0,len(li)-i-1):
        if li[j]>li[j+1]:
            temp=li[j]
            li[j] = li[j + 1]
            li[j+1] = temp
print(li)
# -------------------------------------

str="shivanii is good"












