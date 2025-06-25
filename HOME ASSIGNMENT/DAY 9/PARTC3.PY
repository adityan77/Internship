# •	Create a dictionary marks with subjects as keys and marks out of 100 as values.
# •	Calculate total marks and average.
# •	Print a message based on average:
# o	>90: Excellent
# o	70–90: Good
# o	<70: Needs Improvement

marks={"Maths":75,"English":90,"Marathi":85,"Science":89,"Social Science":80}
total=0
count=0
for values in marks.values():
    total+= values
    count+=1

print(f"Total Marks:-{total}")
avg=total/count
print(f"Average Of Student Is:-{avg}")

if avg>=90:
    print("Excellent")
elif avg>=70 and avg<90:
    print("Good")
elif avg<70:
    print("Needs Improvement")
