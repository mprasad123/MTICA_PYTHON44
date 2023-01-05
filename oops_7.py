class Employee:
    empCount = 0
    def __init__(self,name,salary):
          self.name = name
          self.salary = salary
          Employee.empCount +=1
    def displayCount(self):
           print("Total Employee {0} ".format( Employee.empCount))
    def displayEmployee(self):
           print("Name :",self.name, ",  Salary:  ", self.salary)
emp1=Employee("prabha",100000)
emp1.displayEmployee()
print ("is salary an attribute:",hasattr(emp1,  'salary'))
print( getattr(emp1, 'salary') )
setattr(emp1, 'salary', 50000)
print ("Modified salary", getattr(emp1,'salary'))
print ( hasattr(emp1, 'desig') )
setattr(emp1, 'desig', 'manager')
print( hasattr(emp1, 'desig') )
print ("Added Attribute", getattr(emp1, 'desig') )
delattr(emp1, 'salary')
print  (" is salary an attribute:",hasattr(emp1, 'salary'))






