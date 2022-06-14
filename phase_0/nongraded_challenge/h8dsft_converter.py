def kelvin_celcius ():
    temp_check = ["kelvin", "celcius"]
    temperature = input("Please input the temperature: ")
    
    while type(temperature) != int or type(temperature) != float:
        print ("That is not a number!")
        temperature = input("Please input the temperature: ")

    print ("Thank you!")
    print ("Is this temperature in kelvin or celcius?")
    temp_type = input("Please input 'kelvin' for kelvin and 'celcius' for celcius: ")
    temp_type.lower()
    
    while temp_type not in temp_check:
        print ("wrong temperature type!")
        print ("Is this temperature in kelvin or celcius?")
        temp_type = input("Please input 'kelvin' for kelvin and 'celcius' for celcius: ")
        temp_type.lower()

    if temp_type in temp_check:
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")

kelvin_celcius()