import emoji
import random
from colorama import Fore,Back,Style
from playsound import playsound

print(Fore.RED + "\n\n                                WELCOME TO THE PASSWORD GENERATOR!\n")
print(Style.RESET_ALL)

playsound('C:\\Users\\STARK\\OneDrive\\Desktop\\python\\projects\\soundtop.wav')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many Letters do you want in your Password?"))
num_symbols = int(input("How many Symbols do you want in your Password?"))
num_numbers = int(input("How many Numbers do you want in your Password?"))

# num_letters_list = len(letters)
# num_numbers_list = len(numbers)
# num_symbols_list = len(symbols)

print("Your Password is:")

for i in range(0,num_letters):
    print(Fore.GREEN + random.choice(letters),end="")

for i in range(0,num_symbols):
    print(Fore.GREEN + random.choice(symbols),end="")

for i in range(0,num_numbers):
    print(Fore.GREEN + random.choice(numbers),end="")

print(Fore.RED + "\n\nAs Per The Guidelines Provided By The Carnegie Mellon University:")

if(num_numbers==0 and num_symbols==0):
    print(Fore.BLUE + "Your Password should contain at least a number and a special character!!",end="")
    print("\U0001F61E")
    playsound('C:\\Users\\STARK\\OneDrive\\Desktop\\python\\projects\\sound1.wav')

elif (num_symbols+num_letters+num_numbers<8):
    print(Fore.RED + "You dont have a STRONG password!! Try again.",end="")
    print("\U0001F61E")
    playsound('C:\\Users\\STARK\\OneDrive\\Desktop\\python\\projects\\sound1.wav')

else:
    print(Fore.YELLOW + "You have a HARD NUT password!!",end="")
    print("\U0001f600")
    playsound('C:\\Users\\STARK\\OneDrive\\Desktop\\python\\projects\\sound2.wav')
    




    

