#program to check whether student passed on exam and individually in each subjects
name=input("Enter the name of student:")
n1=int(input("Enter numbers in maths:"))
n2=int(input("Enter numbers in science:"))
n3=int(input("Enter numbers in computer:"))

#check for total preccentage
total_per=((n1+n2+n3)/300)*100
if(total_per>=40 and n1>=33 and n2>=33 and n3>=33):
    print("Congratulation! ",name,", You passed the exam🎊.")
else:
    print("Sorry! You are failed.")