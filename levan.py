class BankAccount:



    def __init__(self,account_number, account_holder  ,balance):
        self.balance = balance
        self.account_number = account_number
        self.account_holder = account_holder


    def deposit(self, amount):
        self.balance+= amount
        print(self.balance)

    def withdraw(self, amount):
        self.balance-= amount
        print(self.balance)



bankEmployer = BankAccount(00000, "levan kavtaradze", 1000)

bankEmployer.deposit(1000)
bankEmployer.withdraw(2000)


class Student:

    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses


    def showName(self):
        print(self.name)

    def showCourse(self):
        print(self.courses)

    def showStudentID(self):
        print(self.student_id)


student1 = Student("levan kavtaradze", 231, ["computer science", "Architechture"])
student2 = Student("vaja fshavela", 542, ["bussiness", "engineering"])
student3 = Student("galaktion tabidze", 623, ["phylosophy", "engineering", "marketing"])


student1.showName()
student2.showStudentID()
student3.showCourse()
