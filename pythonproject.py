#Library Management System
#Library data
class Library():
    def __init__(self):
        self.books=[]
        self.member=[]
        self.issuebook=[]
    def add_books(self):
        n=int(input("Enter how many books you want"))#adding of books
        for i in range(1,n+1):
            a=input("Enter book {}:".format(i))
            self.books.append(a)
#Display data
    def display_books(self):
        print(".....Books.....")
        for i in range(len(self.books)):
            print(i + 1, ".", self.books[i])
#Search data
    def search_book(self):
        search=input("Enter the the Book name to search")
        if search in self.books:
            print("Book found")
        else:
            print("Book not found")
#Adding members
    def add_member(self):
        m=int(input("Enter how many members do u need to add"))
        for i in range(1,m+1):
            name=input("Enter member {} name:".format(i))
            id=input("Enter member {} ID:".format(i))
            mem={"id":id,
                    "name": name}
            self.member.append(mem)
#Issue Books
    def issue_book(self):
        memberid=input("enter the id")
        found=False
        for mem in self.member:
            if mem["id"]== memberid:
                found=True
                print("Member found")
                bookname=input("enter the name of the book")
                if bookname in self.books:
                    print("Book found")
                    alreadyissued=False
                    for issue in self.issuebook:
                        if issue["book"]==bookname:
                            alreadyissued=True
                    if alreadyissued:
                        print("Book already issued")    
                    else:
                        issue={"memberid":memberid,"book":bookname}
                        self.issuebook.append(issue)
                        print("Book issued successfully")
                else:
                    print("Book not found")
        if found==False:
            print('Member not found')
        print("Issued books:",self.issuebook)
#Return Book
    def return_book(self):
        returnid=(input("enter the id"))        
        bn=input("enter the book name")
        returned=False
        for issue in self.issuebook:
            if issue["memberid"]==returnid and issue["book"]==bn:
                self.issuebook.remove(issue)
                returned=True
                print("book returned")
                break
        if returned==False:
            print("book not returned")
        print("Issued books:",self.issuebook)
#Show Details
    def show_details(self):
        print("..... LIBRARY DETAILS .....")
        print("Total Books:", len(self.books))
        print("Books:")
        if len(self.books) == 0:
            print("No books available")
        else:
            for i in range(len(self.books)):
                print(i + 1, ".", self.books[i])
        print("Total Members:", len(self.member))
        print("Members:")
        if len(self.member) == 0:
            print("No members available")
        else:
            for mem in self.member:
                print("ID:", mem["id"], "| Name:", mem["name"])
        print("Issued Books:")
        if len(self.issuebook) == 0:
            print("No books are currently issued")
        else:
            for issue in self.issuebook:
                print(
                    "Member ID:", issue["memberid"],
                    "| Book:", issue["book"]
                )
lib=Library()
while True:
    print("..... LIBRARY MANAGEMENT SYSTEM .....")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Show Details")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        lib.add_books()
    elif choice == "2":
        lib.display_books()
    elif choice == "3":
        lib.search_book()
    elif choice == "4":
        lib.add_member()
    elif choice == "5":
        lib.issue_book()
    elif choice == "6":
        lib.return_book()
    elif choice == "7":
        lib.show_details()
    elif choice == "8":
        print("Thank you for using Library Management System.Have a great day!")
    else:
        print("Invalid choice")











    
