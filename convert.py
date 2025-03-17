# assignment: programming assignment 3
# author: Shreya Hiremath
# date: July 26, 2022
# file: convert.py is a program that emulates a simple SI unit conversion calculator.
# input: strings and numbers (integers and float)
# output: interactive messages (strings and numbers)

def format(num, precision = 2):
    
    newnum = '{0:.3g}'.format(num)
    return newnum

    

def isfloat(token) :
    try:
        float(token)
        return True
    except ValueError:
        return False
    

def fahrenheit_celsius(fahrenheit):

    
    fahrenheit = float(fahrenheit)
    celsius = round ((float(fahrenheit - 32) * 5 / 9), 2)
    return celsius
    


def miles_km(miles):

    miles = float(miles)
    km = round ((float(miles * 1.609344)),2)
    return km
    

def pounds_kg(pounds):

    pounds = float(pounds)
    kg = round ((float(pounds * 0.45359237)),2)
    return kg



if __name__ == '__main__':

    print("Welcome to the SI Unit Converter!")

    flag = "y" 
    while flag == "Y" or flag == "y":

        choice = input ( """Please choose one of the following conversions:\nFahrenheit to Celsius - F\nPounds to kg - P\nMiles to km - M \n""" ).upper()


            
        if choice == 'F':

            while True:
                
                fahrenheit = input("Please enter a temperature in Fahrenheit: \n")

                if isfloat(fahrenheit)!= True:
                    
                    print("You did not enter a number.")
                

                else:

                    fahrenheit = float(fahrenheit)

                    break
                    
                
            c = fahrenheit_celsius(fahrenheit)

            print (format(fahrenheit) , "Fahrenheit corresponds to" , format(c) , "Celsius.")

            flag = input( "Do you want to continue? [Y/N]: \n")
                    

                

        elif choice == 'M':

            while True:

                miles = input("Please enter miles: \n")

                if isfloat(miles)!= True:
                    
                    print("You did not enter a number.")

                else:

                    miles = float(miles)

                    break
                

            n = miles_km(miles)

            print(format(miles), "miles corresponds to" , format(n) , "km.")

            flag = input("Do you want to continue? [Y/N]: \n")



        elif choice == 'P':

            while True:

                pounds = input("Please enter pounds: \n")

                if isfloat(pounds)!= True:

                    print("You did not enter a number.")

                else:

                    pounds = float(pounds)

                    break


            k = pounds_kg(pounds)

            print (format(pounds) , "pounds corresponds to" , format(k) , "kg.")

            flag = input( "Do you want to continue? [Y/N]: \n")



        else:
            
            print("You did not choose correctly.")

            continue
            
print("Goodbye!")


    
    # 1. print the welcome message
    
    # 2. make a while loop
    
    # 3. write the menu and get the user input used in the elif statement
    
    # 4. write an elif statement and make function calls

    # 5. get the user input used to control the while loop
