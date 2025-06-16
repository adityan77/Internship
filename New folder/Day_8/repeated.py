my_tuple = (1,89,100,22,45,67,89,100)

my_list = []
for i in range(len(my_tuple)):
    count = my_tuple.count(my_tuple[i])
    if count > 1 and my_tuple[i] not in my_list:
        my_list.append(my_tuple[i])


print("Repeated Value",my_list)

