# Replace Words with Frequencies
# Input: "cat dog cat rat dog cat"
# # Output: "3 2 3 1 2 3"
li="cat dog cat rat dog cat"
sp=li.split()
print(sp)
my_list=[str(sp.count(word)) for word in sp]
str=" ".join(my_list) 
print(str)
c_count=li.count("cat")
d_count=li.count("dog")
r_count=li.count("rat")
# print(c_count)