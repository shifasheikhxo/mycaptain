

import csv

def write_csv(info_l):
    with open('student.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0 :
          writer.writerow(["Name","Age","Contact_number","Email_ID"])

        writer.writerow(info_l)
 
 
if __name__  == '__main__':
 condition= True  
 student_num=1

 while(condition): #loop function to repeat
    student_info = input("Enter student details for roll num {} in the following format(Name Age Contact_number Email_ID):".format(student_num))
    student_list = student_info.split(' ')  #split

    print("\nEntered information:\nName: {}\nAge: {}\nContact_number: {}\nEmail_ID: {}"
     .format(student_list[0],student_list[1],student_list[2],student_list[3]))

    check=input("Is the Entered Information correct?(y/n):")

    if check =="y":
      write_csv(student_list)

      condition_check = input("enter y/n(yes/no) if you want to enter information for another student: ")
      if condition_check== "y":
        condition= True
        student_num=student_num+1
      elif condition_check=="n":
        condition= False
   
    else: 
        print("\nPlease Re-enter The Values!")
    