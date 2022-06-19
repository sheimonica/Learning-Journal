w = float(input("Masukan berat badan (kg): "))
h = float(input("Masukan tinggi badan (cm): "))
h *= 0.01

def bmi(w, h):
    calc = round((w/(h**2)), 1)
    if calc < 18.5:
        print(f"BMI anda adalah {calc}, anda underweight!")
    elif 18.5 <= calc <= 24.9:
        print(f"BMI anda adalah {calc}, anda normal!")
    elif 25 <= calc <= 29.9:
        print(f"BMI anda adalah {calc}, anda overweight!")
    else:
        print(f"BMI anda adalah {calc}, anda very overweight!")

bmi(w,h)