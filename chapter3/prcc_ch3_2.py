#to replce name and date in given letter format
letter='''Dear <name>,
                    You have passed the Exam.
                    Huge Congratulation!!!
                    <date>'''
name=input("Enter name of passed candidate: ")
date=input("Enter date of passed: ")
print(letter.replace("<name>",name).replace("<date>",date)) 