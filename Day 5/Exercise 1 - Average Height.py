# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#fast way
# sum_heights = sum(student_heights)
# number_students = len(student_heights)
# print(round(sum_heights/number_students))


#using loops
sum_heights = 0
number_students = 0
for height in student_heights:
  sum_heights += height
  number_students += 1

print(round(sum_heights/number_students))

