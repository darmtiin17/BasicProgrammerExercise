def menu():
    print ("""
    1. Calculate the area of a triangle
    2. Calculate the area of a rectanglethree lengths
    3. Specify odd-even number
    4. Exit
    """)
 
menu ()


def triangle():
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the heioght of the triangle: "))\
 
    area = 1/2 *base*height
    print(f"The area of triangle is{area}cm")

def rectangle():
    numbers = int (input("Enter the length of the rectangle: "))

    if numbers % 2 == 0 :
        print (f"{numbers} even numbers : ")
        
    else :
        print(f"{numbers} odd numbers")

while True :
    choice = input (" Select menu: ")

    if choice == "1":
        triangle()
    elif choice == "2":
        rectangle()
    elif choice == "3":
        determine_numbers()
    elif choise == "4":
        os.system("cls")
        exit()

    isBreak = input("do you want to continue ? Y/N :")

    if isBreak == "Y" or isBreak == "y":
        os.system("cls")
        sleep(1)
    else:
        os.system("cls")
        break
    menu()