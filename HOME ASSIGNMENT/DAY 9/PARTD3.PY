# 14.	Nested Dictionary
# # •	Create a nested dictionary:
# # student = {
# #     	"name": "Ravi",
# #     	"marks": {
# #         	"math": 88,
# #         	"science": 92
# #     	}
# # }
# # •	Access "science" marks from the nested dictionary.
student = {
     	"name": "Ravi",
     	"marks": {
         	"math": 88,
         	"science": 92
     	}
 }
sci=student["marks"]["science"]
print(f"Acessing Science Marks:-{sci}")
