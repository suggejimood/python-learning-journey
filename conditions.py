x = 10
if x < 0:
    print("Negatif sayı")
elif x == 0:
    print("sıfır")
else:
    print("Negatif")

command = "start"

match command:
        case "start":
          print("Starting...")
        case "stop":
            print("Stoping...")
        case _:
            print("Unknown")

