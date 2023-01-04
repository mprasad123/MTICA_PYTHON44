defdef printMonth(dn):
    mn=' '
    if(dn==1):
        mn= "January"
    elif(dn==2):
        mn= "February"
    elif(dn==3):
         mn= "March"
    elif(dn==4):
        mn= "April"
    elif(dn==5):
        mn= "May"
    elif (dn==6):
        mn= "June"
    elif(dn==7):
        mn= "July"
    elif(dn==5):
        mn= "Aug"
    elif(dn==6):
        mn= "Sep"
    else:
        mn= "Invalid"
        
    return mn
for i in range(7):
    inpNum=int(input())
     print(printMonth(inpNum))

     

