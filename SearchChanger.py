import os

print("FYI, this is case sensitive!")
ask = (input("Anyways, Enter the Searchbox type (1 - 6) or Reset: "))

if ask == "1":
    os.system('cmd /k vivetool /enable /id:39072097 /variant:1')
if ask == "2":
    os.system('cmd /k vivetool /enable /id:39072097 /variant:2')
if ask == "3":
    os.system('cmd /k vivetool /enable /id:39072097 /variant:3')
if ask == "4":
    os.system('cmd /k vivetool /enable /id:39072097 /variant:4')
if ask == "5":
    os.system('cmd /k vivetool /enable /id:39072097 /variant:5')
if ask == "6":
    os.system('cmd /k vivetool /enable /id:39072097 /variant:6')
if ask == "Reset":
    os.system('cmd /k vivetool /enable /id:39072097 /variant:x')
else:
    print("\nPlease enter a valid number!")