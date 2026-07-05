import time 

correct_pin = "6767"
attempts = 0
max_attempts = 4

print("Pin Lock")

while attempts < max_attempts:
    pin = input("Enter pin")

    if pin == correct_pin:
        print("Access granted")
        break

    else:
        attempts+=1
        print("Incorrect Pin")

        if attempts < max_attempts:
            print("Wait 6 seconds")
            time.sleep(6)


        if attempts == max_attempts:
          print("Too many attempts")
          print("LOCKED FOREVER💀")
          while True:
              pass