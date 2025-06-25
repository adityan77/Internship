# 8.	Contact Book
# o	Create a dictionary contacts with 3 people’s names as keys and their phone numbers as values.
# o	Add a new contact.
# o	Update one contact’s number.
# o	Delete one contact.
contact={"Aditya":9420320699,"Jayesh":8652458820,"Piyush":7020456320}
contact["Prasad"]=9404789834
print(f"Dictionary After Adding One Contact:-{contact}")
contact["Aditya"]=9021639713
print(f"Dictionary After Updating One Number:-{contact}")
del(contact["Jayesh"])
print(f"Dictionary After Deleting One Contact:-{contact}")
