#PGM TO CHECK WHETHER THE STRING IS PALINDROME OR NOT :
    #WITHOUT USING FUNCTION
Str = input("ENTER YOUR NAME:")
print('ENTER STRING IS:',Str)
Revstr = Str[::-1]
print('REVERSED STRING IS:',Revstr)
if Revstr == Str:
    print('THE STRING IS PALINDROME')
else:
    print('THE STRING IS NOT A PALINDROME')
    #WITH USING FUNCTION
def reverse(Str):
    print('ENTER STRING IS:', Str)
    Revstr = Str[::-1]
    print('REVERSED STRING IS:', Revstr)
    if Revstr == Str:
        print('THE STRING IS PALINDROME')
    else:
        print('THE STRING IS NOT A PALINDROME')
reverse('madam')




#PGM TO SORT NAMES IN ALPHABETICAL ORDER :
names = ['ramya', 'rak', 'indial', 'vhi', 'aby']
sortednames = sorted(names)
print("Sorted names are  :", sortednames)




#PGM TO FIND LARGETST OF 3 NUMBERS :
    #WITHOUT USING FUNCTION
a=70
b=40
c=30
if a>b and a>c :
    print('a is greater')
elif b>a and b>c :
    print ('b is greater')
else:
    print('c is greater')

    #WITH USING FUNCTION

def greatest(a,b,c) :
    if a > b and a > c:
        print('a is greater')
    elif b > a and b > c:
        print('b is greater')
    else:
        print('c is greater')
greatest(45,78,90)




#PGM TO PRINT MAXIMUM , 2nd and 4th LARGET , 3rd and 5th SMALLEST no. IN GIVEN LIST :
lis = [1, 88, 40, 70, 99, 55, 10, 20, 56, 98, 100, 98760]
lis2 = sorted(lis)
print(lis2)
print('LARGEST VALUE', max(lis2))
print('THE SECOND LARGEST NO. IS', lis2[-2])
print('THE FOURTH LARGEST NO. IS', lis2[-4])
print('THE THIRD SMALLEST NO. IS', lis2[2])
print('THE FIFTH SMALLEST NO. IS', lis2[4])




#PGMS ON  PRIME NUMBERS :

    # PRIME OR NOT WITHOUT USING FUNCTION

num = int(input("Enter a number: "))
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f = 1
        break
    i = i + 1
if f == 0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")

    #PRIME OR NOT WITH USING FUNCTION

def primein(num):
    f = 0
    i = 2
    while i <= num / 2:
        if num % i == 0:
            f = 1
            break
        i = i + 1
    if f == 0:
        print(num,"is a PRIME number")
    else:
        print(num,"is not a PRIME number")
primein(18)

    #PRIME NO'S IN RANGE USING WHILE WITHOUT USING FUNCTION

x = int(input(" Please Enter the Minimum Value: "))
y = int(input(" Please Enter the Maximum Value: "))
Num= x
while (Num <= y):
    count = 0
    i = 2
    while (i <= Num / 2):
        if (Num % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and Num != 0):
        print(Num)
    Num = Num + 1

    #PRIME NO'S IN RANGE USING WHILE WITH USING FUNCTION

def primewhile(x,y):
    Num = x

    while (Num <= y):
        count = 0
        i = 2

        while (i <= Num / 2):
            if (Num % i == 0):
                count = count + 1
                break
            i = i + 1

        if (count == 0 and Num != 0):
            print(Num)
        Num = Num + 1
primewhile(5,15)

    #PRIME NO'S IN RANGE USING FOR WITHOUT USING FUNCTION

x= int(input(" Please Enter the Minimum Value: "))
y= int(input(" Please Enter the Maximum Value: "))
for Num in range (x, y + 1):
    count = 0
    for i in range(2, (Num // 2 + 1)):
        if(Num % i == 0):
            count = count + 11
            break
    if (count == 0 and Num != 0):
        print(Num)




#PGM TO PRINT PYRAMID USING NO. :
    def contnum(n):
        num = 1
        for i in range(0, n):
            for j in range(0, i + 1):
                print(num, end=" ")
                num = num + 1
            print("\r")
    contnum(6)




#PGM TO PRINT TRIANGLE USING 01 :
    def triangle(n):
        k = 2 * n - 2
        for i in range(0, n):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i + 1):
                # printing stars
                print("01 ", end="")
            print("\r")
    triangle(8)




#MENU DRIVEN PROGRAM AIRTHEMATIC OPERATIONS:
    def switch():
        num1 = int(input("\nENTER FIRST NUMBER : "))
        num2 = int(input("ENTER SECOND NUMBER : "))
        print("1. ADDITION \n2. SUBTRACTION \n3. MULTIPLICATION \n4. DIVISION \n")
        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            result = (num1 + num2)
            print("ADDITION OF 2 NO. IS = ", result)
            ysno = (input("do you want to continue(YES/NO) :"))
            if ysno == 'YES' or ysno == 'yes':
                switch()
            elif ysno == 'NO' or ysno == 'no':
                print(" END OF PROCESS")
            else:
                print(" INVALID INPUT ")
        elif choice == 2:
            result = (num1 - num2)
            print("SUBTRACTION OF 2 NO. IS = ", result)
            ysno = (input("do you want to continue(YES/NO) :"))
            if ysno == 'YES' or ysno == 'yes':
                switch()
            elif ysno == 'NO' or ysno == 'no':
                print(" END OF PROCESS")
            else:
                print(" INVALID INPUT ")
        elif choice == 3:
            result = (num1 * num2)
            print("MULTIPLICATION OF 2 NO. IS = ", result)
            ysno = (input("do you want to continue(YES/NO) :"))
            if ysno == 'YES' or ysno == 'yes':
                switch()
            elif ysno == 'NO' or ysno == 'no':
                print(" END OF PROCESS")
            else:
                print(" INVALID INPUT ")
        elif choice == 4:
            result = (num1 / num2)
            print("DIVISION OF 2 NO. IS = ", result)
            ysno = (input("do you want to continue(YES/NO) :"))
            if ysno == 'YES' or ysno == 'yes':
                switch()
            elif ysno == 'NO' or ysno == 'no':
                print(" END OF PROCESS")
            else:
                print(" INVALID INPUT ")
        else:
            print("Incorrect option")
    switch()





