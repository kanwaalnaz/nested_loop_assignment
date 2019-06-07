print ("Choose the given option number to print pattern")
print (" ")

print ("Option # 01")
print (" ")
print ("*")
print ("**")
print ("***")
print ("****")
print ("*****")
print ("******")
print (" ")

print ("Option # 02")
print (" ")
print ("1")
print ("22")
print ("333")
print ("4444")
print ("55555")
print ("666666")
print ("7777777")
print (" ")

print ("Option # 03")
print (" ")
print ("1")
print ("12")
print ("123")
print ("1234")
print ("12345")
print ("123456")
print (" ")

print ("Option # 04")
print (" ")
print ("            *")
print ("           * *")
print ("          * * *")
print ("         * * * *")
print ("        * * * * *")
print ("       * * * * * *")
print ("      * * * * * * *")
print ("       * * * * * *")
print ("         * * * *")
print ("          * * *")
print ("           * *")
print ("            *")



option = int (input("Please enter the option number = "))

if option == 1:

    for i in range(0,6):
        for j in range (0,i+1):
            print ("*", end ='')
        print ("\r")
    print("\n")

elif option == 2:
    for i in range (1,8):
        for j in range (1,i+1):
            print (i, end ='')
        print ("")
    print("\n")

elif option == 3:
    for i in range (1,7):
        for j in range (1,i+1):
            print (j, end ='')
        print ("")
    print("\n")

elif option == 4:
    size =7
    m = (2* size) - 2
    for i in range (0,size):
        for j in range (0,m):
            print(end= " ")
        m=m-1
        for j in range (0, i+1):
            print ("*",end= ' ')
        print ("")
    m=m+2
    for i in range(size,0,-1):
        for j in range(m,0,-1):
            print(end= ' ')
        m=m+1
        for j in range (i-1,0,-1):
            print ("*",end =' ')
        print(" ")