def printSunday():
    print("sunday")
def printMonday():
    print("monday")
def printTuesday():
    print("tuesday")
def printWednesday():
    print("wednesday")
def printThursday():
    print("thursday")
def printFriday():
    print("friday")
def printSaturday():
    print("saturday")


def choose():
    print("Enter day number between 1-7 ")
dayDict={ 1:printSunday ,2:printMonday, 3: printTuesday, 4: printWednesday,
          5:printThursday, 6:printFriday, 7:printSaturday }
choose()
dayNo=int(input())
if dayNo>=1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("INVALID")
