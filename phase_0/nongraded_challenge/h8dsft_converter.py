def kelvin_celcius ():
    temp_check = ["kelvin", "celcius"]
    temperature = input("Please input the temperature: ")

    while temperature != float:
        print ("wrong temperature!")
        temperature = input("Please input the temperature: ")

    print ("Thank you")
    print ("Is this temperature in kelvin or celcius?")
    temp_type = input("Please input 'kelvin' for kelvin and 'celcius' for celcius: ")
    temp_type.lower()
    
    while temp_type not in temp_check:
        print ("wrong temperature type!")
        print ("Is this temperature in kelvin or celcius?")
        temp_type = input("Please input 'kelvin' for kelvin and 'celcius' for celcius: ").lower()

    if temp_type in temp_check:
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")

kelvin_celcius()
