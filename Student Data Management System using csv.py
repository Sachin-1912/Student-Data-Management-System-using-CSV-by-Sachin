import csv
def read_csv_file():
    with open('Student_data.csv','r')as f:
        fobj = csv.reader(f)
        for i in fobj:
            print(i)
def write_csv_file():
    with open('Student_data.csv','w', newline='')as f:
        fobj = csv.writer(f)
        while True:
            Admn_no = int(input('Enter Admission number: '))
            Name = input('Enter Name:')
            Age = int(input('Enter age(Yrs): '))
            Grade = int(input('Enter Grade: '))
            Section = input('Enter section: ')
            City = input('Enter City:')
            State = input('Enter State: ')
            Mother_Toungue = input('Enter your mother toungue: ')
            CGPA_Score = float(input('Enter CGPA score: '))
            data = [Admn_no,Name, Age, Grade, Section, City, State, Mother_Toungue, CGPA_Score]
            fobj.writerow(data)
            choice = int(input('Do you want to add more data? 1.Yes 2.No: '))
            if choice==1:
                continue
            if choice==2:
                break
    print('file created successfully')
def search_csv_file():
    with open('Student_data.csv','r',) as f:
        fobj = csv.reader(f)
        Admn_no = int(input('Enter Admission number to be searched: '))
        next(fobj) 
        flag=0
        for i in fobj:
            if int(i[0])==Admn_no:
                print('Details of given Admission number:')
                print(i)
                flag=1
                break
            if flag==0:
                print('Admission number not found')
def max_csv_file():
    with open('Student_data.csv','r') as f:
        fobj = csv.reader(f)
        next(fobj) 
        maxs = -1
        for i in fobj:
            if int(i[8])>maxs:
                maxs = int(i[8])
                z=i
        print('Student with maximum CGPA score:', z)
        f.seek(0)
        next(fobj)
        for i in fobj:
            if int(i[8])==maxs:
                print(i)
def min_csv_file():
    with open('Student_data.csv','r') as f:
        fobj = csv.reader(f)
        next(fobj) 
        maxs = -1
        for i in fobj:
            if int(i[8])>maxs:
                maxs = int(i[8])
                z=i
        print('Student with minimum CGPA score:', z)
def dispmark():
    with open('Student_data.csv','r') as f:
        fobj = csv.reader(f)
        next(fobj)
        for i in fobj:
            if int(i[8])>=9:
                print(i)
while True:
    choice = int(input('1.Read CSV file\n2.Write CSV file\n3.Search by Admission number\n4.Student with maximum CGPA score\n5.Student with minimum CGPA score\n6.Exit\nEnter your choice: '))
    if choice == 1:
        read_csv_file()
    elif choice == 2:
        write_csv_file()
    elif choice == 3:
        search_csv_file()
    elif choice == 4:
        max_csv_file()
    elif choice == 5:
        min_csv_file()
    elif choice == 6:
        print('Thankyou for using our program system.......\nDo use our program again......\nHave a nice day!!!')
        break

        








        
        