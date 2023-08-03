# Temperature task

temperature = int(input("Enter the current temperature: "))

if temperature >= 35:
    print("Stay inside with the blinds shut, it's not worth it!")
elif temperature >=22:
    print("it's taps aff weather! Get the cans and the disposable BBQ oot!")
elif temperature >= 15:
    print("Decent weather for a wee jaunt.")
elif temperature >= 8:
    print("Make sure you have a light jacket with you.")
elif temperature >= 2:
    print("Unseasonably mild today!")
elif temperature >= -3:
    print("Ooh it's a wee bit nippy!")
else:
    print("It's pure baltic the day man!")
