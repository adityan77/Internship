tup = ('tuple','is','awesome')
# length = tuple(len(i) for i in tup)
my_list = []
for i in tup:
    my_list.append(len(i))

length = tuple(my_list)
print(length)