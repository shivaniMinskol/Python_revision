# str="shivanii is good"
# duplicate=[]
# for i in str:
#     if str.count(i)>1:
#         # continue
#         print(i,":-",str.count(i))
#     if i not in duplicate:
#             duplicate.append(i)
#
# print(duplicate)

# str="shivani is good"
# str2=[]
# duplicate=[]
# for i in str:
#     if str.count(i)<=1:
#         str2.append(i)
#     else:
#         duplicate.append(i)
# print(str2)
# print(duplicate)

# ---------------------------------------------

add= lambda x,y:x+y
add(10,20)


def add(*args):
    return args

add(1,2,3,80,70,50,70,89)
print