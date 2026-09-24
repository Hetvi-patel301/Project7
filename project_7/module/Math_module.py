import math
def fact(n):
    result = math.factorial(n)
    print("Factorial:",result)
def interest(p_amount,rate_of_interest,time):
    total_amount = p_amount*((1+rate_of_interest/100)**time)
    print("Compound Interest:",total_amount)
def trigo(degrees):
    print("--- Trigonometric Calculations ---")
    radian = math.radians(degrees)
    sin_val = math.sin(radian)
    print("sin =",sin_val)
    cos_val = math.cos(radian)
    print("cos =",cos_val)
    if radian == 180:
        print("undefined")
    else:
        tan_val = math.tan(radian)
        print("tan =",tan_val)
def area_of_shape():
    while True:
        print("\n1.Circle\n2.Rectangle\n3.Triangle\n4.Square\n5.Exit")
        choice = int(input("Enter your choice:"))
        match choice:
            case 1:
                r = float(input("Enter Radius:"))
                ans = math.pi*r*r
                print("Area of Circle = ",ans)
                print("-----------------------------------\n-----------------------------------")
            case 2:
                l = float(input("Enter length:"))
                w = float(input("Enter width:"))
                ans = l*w
                print("Area of Rectangle = ",ans)
                print("-----------------------------------\n-----------------------------------")
            case 3:
                base = float(input("Enter base:"))
                h = float(input("Enter Height:"))
                ans = 0.5*base*h
                print("Area of Triangle =",ans)
                print("-----------------------------------\n-----------------------------------")
            case 4:
                l = float(input("Enter length:"))
                ans = l*l
                print("Area of Square = ",ans)
                print("-----------------------------------\n-----------------------------------")
            case 5:
                break
            case _:
                print("Invalid choice")