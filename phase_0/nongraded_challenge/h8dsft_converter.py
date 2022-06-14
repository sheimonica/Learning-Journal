#basic info
temp_type = ""
temp_check = ["kelvin", "celcius", "fahrenheit"]

#convert kelvin-celcius dan sebaliknya
def kelvin_celcius ():
    if temp_type == "celcius":
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        new_temp = temperature + 273.15
        print (f"The new temperature in kelvin is {new_temp}K ")
    
    elif temp_type == "kelvin":
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        new_temp = temperature - 273.15
        print (f"The new temperature in celcius is {new_temp}°C ")
    
    else:
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        print (f"no conversion happened")

#convert ke fahrenheit dari celcius atau kelvin
def convert_fahrenheit():
    if temp_type == "celcius":
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        new_temp = (temperature*(9/5)) + 32
        print (f"The new temperature in celcius is {new_temp}°F ")
    
    elif temp_type == "kelvin":
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        new_temp = (9/5)*(temperature-273) + 32
        print (f"The new temperature in kelvin is {new_temp}°F ")
    
    else:
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        print (f"no conversion happened")

#convert fahrenheit ke celcius atau kelvin
def converting_fahrenheit():
    if desired_temp == "celcius":
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        new_temp = (temperature-32)*(5/9)
        print (f"The new temperature in celcius is {new_temp}°F ")
    
    elif desired_temp == "kelvin":
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        new_temp = (5/9)*(temperature - 32) + 273.15
        print (f"The new temperature in kelvin is {new_temp}°F ")
    
    else:
        print (f"The temperature you entered was {temperature}")
        print (f"The temperature was in {temp_type}")
        print (f"no conversion happened")

#decide which conversion to do
def decision():
    if temp_type == "fahrenheit":
        converting_fahrenheit()
    
    elif desired_temp == "fahrenheit":
        convert_fahrenheit()
    
    else:
        kelvin_celcius()

#input
temperature = float(input("Please input the temperature: "))

print ("Is this temperature in kelvin, celcius, or fahrenheit?")
temp_type = input("Please input 'kelvin' for kelvin, 'celcius' for celcius, and 'fahrenheit' for fahrenheit: ").lower()
    
#correcting temperature
while temp_type not in temp_check:
    print ("wrong temperature type!")
    print ("Is this temperature in kelvin or celcius?")
    temp_type = input("Please input 'kelvin' for kelvin, 'celcius' for celcius, and 'fahrenheit' for fahrenheit: ").lower()

print ("Do you want to convert this into kelvin, celcius, or fahrenheit?")
desired_temp = input("Please input 'kelvin' for kelvin, 'celcius' for celcius, and 'fahrenheit' for fahrenheit: ").lower()

#correcting desired temperature    
while desired_temp not in temp_check:
    print ("wrong temperature type!")
    print ("Do you want to convert this into kelvin, celcius, or fahrenheit?")
    desired_temp = input("Please input 'kelvin' for kelvin, 'celcius' for celcius, and 'fahrenheit' for fahrenheit: ").lower()

#decide conversion    
decision()
