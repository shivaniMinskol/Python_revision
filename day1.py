str="Python Programming"
newstr=[]
for i in str:
    if str.count(i)>1:
        if i not in newstr:
            newstr.append(i)
print(newstr)

# ------------------------------

str = "My name is shivani"
word=str.split()
rev=[]

for i in word:
    rev.append(i[::-1])
rev2=" ".join(rev)
print(rev2)

str2="My name is shivani"
rev_str=str2[::-1]
print(rev_str)
# --------------------------------------
# palindrome
p ="madam"
rev_p=p[::-1]
if rev_p==p:
    print("string is palindrome")
else:
    print("given string is not palindrome")