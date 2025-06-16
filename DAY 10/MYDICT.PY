my_dict={"a":1,"b":2,"c":1}
list1=list(my_dict)
new={v:k for k,v in my_dict.items()}
print(new)
