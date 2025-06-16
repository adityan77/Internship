list3=[4,5,6,22,2,50]
# list4=[55,66,77,88,99]
# list5=list3 + list4


# # list3.extend(list4)
# print(list5)
# list5.remove(2)
# print(list5)
# p=list5.pop(3)
# print(p)
# del list5[6]
# print(list5)
# a=list3.__add__
# print(a)
def add(list3):
    total=0
    for i in list3:
        total=total+i
    print(total)
print(list3)
add(list3)