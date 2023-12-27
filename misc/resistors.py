#Resistor Colour Code calculator
while True:
    print("Resistor Colour Code Calculator")
    colour=["black","brown","red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    n=colour.index((input("Enter the 1st Colour : ")))
    m=colour.index((input("Enter the 2nd Colour : ")))
    p=colour.index((input("Enter the 3rd Colour : ")))
    print("if there is a 4th colour, ignore it for this, it refers to the tolerance")

    q=int(((n*10)+(m))*(10**(p)))
    z=q/1000

    print(f"\nThe {colour[n]} {colour[m]} {colour[p]} Resistors resistance is : ")
    print(f"{q} ohms or {z} kiloohms")

    # Prompt the user to continue or quit
    print('Enter q to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'q':
        break
