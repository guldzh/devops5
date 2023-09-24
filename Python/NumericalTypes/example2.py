# We are asked to create a program to calculate 
# average score for a student with the exam scores following:
# 1 -> 70
# 2 -> 95
# 3 -> 50 
# 4 -> 45
# Calculate the average score for the student 
# and print the average in following format. 
# Average score for given student grades is `avgScore`. 

studentScore1=70
studentScore2=95
studentScore3=50
studentScore4=45

totalNumberOfStudents=4

avgScore=(studentScore1+studentScore2+studentScore3+studentScore4)/totalNumberOfStudents

print("1 - Average score for given student grades is  -> ", avgScore)

# type() function - we can use this finction to know what data type is suing the 
# particular variable: print(type(avgScore)) - output: <class 'float'>
print(type(avgScore))

studentScore1, studentScore2, studentScore3, studentScore4=40,90,22,21

totalNumberOfStudents=4

avgScore=(studentScore1+studentScore2+studentScore3+studentScore4)/ totalNumberOfStudents

print("2 - Average score for given student grades is  -> ", avgScore)

a=b=c=d=5
b=2

sum=a+b+c+d
print(b)
# Python always looks for the last assignment to the same variable