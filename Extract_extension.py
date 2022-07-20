#extract the extension


a= input("Enter Filename: ")

l1 = a.split(".")
#print ("Extension of the file is : '" +l1[1]+"'")

#considering extension is the last part of the list
print ("Extension of the file is : '" +l1[-1]+"'")
#print ("Extension of the file is :  " + l1[-1])


