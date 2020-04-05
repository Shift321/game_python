from colorama import Fore, Back, Style
from colorama import init
init()
print( Back.RED )

Name = input(" Введите Свое имя")
print( " Привет" + Name +"!")
Name2 =input(" Сколько тебе лет?")
if int(Name2) > 15:
    print(" ого целых" + Name2 +"!")
elif int(Name2) < 15:
    print("пфф всего лишь " + Name2 +"?")
print(" я тут сделал калькулятор вот смотри!")
#калькулятор
print(Back.CYAN)
What = input ( "Что делаем? (+,-): ")
a = float( input ("Введи первое число:") )
b = float( input ("Введи второе число:") )

if What == "+":
    c = a + b
    print(Back.GREEN)
    print("Результат: "+ str(c))
if What == "-":
    c= a - b
    print("Результат: "+ str(c))
