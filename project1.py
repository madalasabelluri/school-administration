import csv
def write_info_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((["name","Age","contact number","Email id"])
        writer.writerow(info_list)
if __name__=='__main__':
    condition = true
    student_num=1
    while(condition):
        student_info=input("enter student information for student #{} in the following format{Name Age Contact_number Email_id}:".format(student_info))
        student_info_list= student_info.split(' ')
        print("\n the entered information is -\nName:{}\nAge:{}\nContact_number:{}\nEmail_id:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is entered information correct?(yes/no):")
        if choice_check =="yes":
            write_into_csv(student_info_list)
            condition_check =input("enter(yes/no) if u want to enter information of another student:")
            if condition_check =="yes":
                condition = true
                student_num = student_num+1
            elif condition_check =="no":
                condition = false
        elif choice_check =="no":
            print("\nplease re-enter the values!")
    

                
                    
                        
                        
