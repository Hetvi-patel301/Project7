from module import * 
def main():
    print("-----------------------------------\n-----------------------------------")
    print("Welcome to Multi-Utility Toolkit")
    print("-----------------------------------\n-----------------------------------")
    while True:
        print("Choose an option:")
        print("1.Date and Time Operation")
        print("2.Mathematical operations")
        print("3.Random Data Generation")
        print("4.Generate Unique Identifiers(UUID)")
        print("5.File Operaton (Custom Module)")
        print("6.Explore Module Attributes (dir())")
        print("7.Exit")
        print("-----------------------------------\n-----------------------------------")
        choice = int(input("Enter your choice:"))
        match choice:
            case 1:
                while True:
                    print("Datetime and Time Operations:")
                    print("1.Display current date and time")
                    print("2.Calculate difference between two dates")
                    print("3.Formate date into custom format")
                    print("4.Stopwatch")
                    print("5.Countdown Timer")
                    print("6.Back to Main Menu")
                    choice1 = int(input("Enter Your choice:"))
                    match choice1:
                        case 1:
                            date_time_module.current_datetime()
                            print("-----------------------------------\n-----------------------------------")
                        case 2:
                            date_time_module.datetime_difference()
                            print("-----------------------------------\n-----------------------------------")
                        case 3:
                            date_time_module.custom_date()
                            print("-----------------------------------\n-----------------------------------")
                        case 4:
                            date_time_module.stopwatch()
                            print("-----------------------------------\n-----------------------------------")
                        case 5:
                            date_time_module.countdown()
                            print("-----------------------------------\n-----------------------------------")
                        case 6:
                            break
                        case _:
                            print("Invalid choice")
            case 2:
                while True:
                    print("Mathematical Operations:")
                    print("1.Calculate Factorial")
                    print("2.slove Compound Interest")
                    print("3.Trigonometric Calculations")
                    print("4.Area of Geometric Shapes")
                    print("5.Back to Main Menu")
                    choice2 = int(input("Enter Your choice:"))
                    match choice2:
                        case 1:
                            n = int(input("Enter number for factorial:"))
                            Math_module.fact(n)
                            print("-----------------------------------\n-----------------------------------")
                        case 2:
                            p_amount = int(input("Enter principal amount:"))
                            rate_of_interest = int(input("Enter rate of interest (in %):"))
                            time = int(input("Enter time (in years):")) 
                            Math_module.interest(p_amount,rate_of_interest,time)
                            print("-----------------------------------\n-----------------------------------")
                        case 3:
                            degrees = float(input("Enter Degrees:"))
                            Math_module.trigo(degrees)
                            print("-----------------------------------\n-----------------------------------")
                        case 4:
                            Math_module.area_of_shape()
                            print("-----------------------------------\n-----------------------------------")
                        case 5:
                            break
            case 3:
                while True:
                    print("Random Data Generation:")
                    print("1.Generate Random Number")
                    print("2.Generate Random List")
                    print("3.Create Random Password")
                    print("4.Generate Random OTP")
                    print("5.Back to Main Menu")
                    choice3 = int(input("Enter your choice:"))
                    match choice3:
                        case 1:
                            random_module.random_num()
                            print("-----------------------------------\n-----------------------------------")
                        case 2:
                            random_module.random_list()
                            print("-----------------------------------\n-----------------------------------")
                        case 3:
                            random_module.password()
                            print("-----------------------------------\n-----------------------------------")
                        case 4:
                            random_module.otp()
                            print("-----------------------------------\n-----------------------------------")
                        case 5:
                            break
            case 4:
                while True:
                    print("Generate Unique Identifiers:")
                    print("1.Generate Unique Identifier 1")
                    print("2.Generate Unique Identifier 3")
                    print("3.Generate Unique Identifier 4")
                    print("4.Generate Unique Identifier 5")
                    print("5.Back to Main Menu")
                    choice4 = int(input("Enter your choice:"))
                    match choice4:
                        case 1:
                            uuid_module.unique_identifiers1()
                            print("-----------------------------------\n-----------------------------------")
                        case 2:
                            uuid_module.unique_identifiers3()
                            print("-----------------------------------\n-----------------------------------")
                        case 3:
                            uuid_module.unique_identifiers4()
                            print("-----------------------------------\n-----------------------------------")
                        case 4:
                            uuid_module.unique_identifiers5()
                            print("-----------------------------------\n-----------------------------------")
                        case 5:
                            break
            case 5:
                while True:
                    print("File Operations:")
                    print("1.Create a new file")
                    print("2.Write to a file")
                    print("3.Read from a file")
                    print("4.Append to a file")
                    print("5.Back to Main Menu")
                    choice5 = int(input("Enter your choice:"))
                    match choice5:
                        case 1:
                            file_module.new_file()
                            print("-----------------------------------\n-----------------------------------")
                        case 2:
                            file_module.write_file()
                            print("-----------------------------------\n-----------------------------------")
                        case 3:
                            file_module.read_file()
                            print("-----------------------------------\n-----------------------------------")
                        case 4:
                            file_module.append_file()
                            print("-----------------------------------\n-----------------------------------")
                        case 5:
                            break
            case 6:
                print("Explore Module Attributes:")
                name = input("Enter module name to explore:")
                dir_module.explore_module_attributes(name)
                print("-----------------------------------\n-----------------------------------")
            case 7:
                print("-----------------------------------\n-----------------------------------")
                print("Thank you for using the Multi-Utility Toolkit!")
                print("-----------------------------------\n-----------------------------------")
                break
            case _:
                print("Invalid choice")
if __name__ == "__main__":
    main()


                    
