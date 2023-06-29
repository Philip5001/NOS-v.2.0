#Neon Operating System v.2.0

import time
import faker
from faker import Faker
import colorama
from colorama import Fore, Back, Style
import pickledb
import rich
from rich.progress import track
import sys
import os

fake = Faker()
db = pickledb.load('NOS_2.db', True)
name_user = db.get('login')
name_user2 = db.get('login')
count_users = 1
users = [db.get('login'), db.get('login2')]
ram = '150'
install_root = False

if not db.exists('login'):
	db.set('login', input("Введите имя пользователя:"))
	db.set('password', input("Придумайте пароль:"))
	
else:
	if input('Введите пароль: ') != db.get('password'):
		print('Неверный пароль!')
		sys.exit()

def start_os():
	print(Fore.YELLOW + 'Загрузка ' + Fore.GREEN + 'ОС')
	time.sleep(2)
	print(Fore.YELLOW + 'Добро пожаловать в NOS!')
	
def off_os():
	print(Fore.GREEN + 'Завершение работы')
	time.sleep(2)
	
def no_system():
	while True:
		ns = input(Fore.RED + 'НЕТ СИСТЕМЫ!')
	
def addition_calc(a, b):
	c = a + b
	print("Результат: " + str(c))
	
def decrease_calc(a, b):
	c = a - b
	print("Результат: " + str(c))
	
def multiplication_calc(a, b):
	c = a * b
	print("Результат: " + str(c))
	
def division_calc(a, b):
	c = a / b
	print("Результат: " + str(c))
	
def multiplication2_calc(a, b):
	c = a ** b
	print("Результат: " + str(c))
	
def division2_calc(a, b):
	c = a // b
	print("Результат: " + str(c))
	
def division3_calc(a, b):
	c = a % b
	print("Результат: " + str(c))
	
start_os()
while True:
	com = input(Fore.YELLOW + 'Введите команду: ')
	
	if com == 'информация':
		print('NOS -- Neon Operating System -- была создана в 2023 году на языке программирования Python.')
		
	if com == 'перезагрузить':
		print(Fore.GREEN + '------------------------------------------------------------')
		start_os()
		
	if com == 'выключить':
		off_os()
		break
		
	if com == 'запустить $Калькулятор':
		what = input('Выберите действие: ')
		num1 = float(input('Введите первое число:'))
		num2 = float(input('Введите второе число:'))
		
		if what == '+':
			addition_calc(num1, num2)
			
		elif what == '-':
			decrease_calc(num1, num2)
			
		elif what == '*':
			multiplication_calc(num1, num2)
			
		elif what == '/':
			division_calc(num1, num2)
			
		elif what == '//':
			division2_calc(num1, num2)
			
		elif what == '**':
			multiplication2_calc(num1, num2)
			
		elif what == '%':
			division3_calc(num1, num2)
			
	if com == 'cd: Аккаунты-Новый':
		new_user = input('Введите имя нового пользователя: ')
		db.set('login2', new_user)
		print('Вы создали нового пользователя, ' + db.get('login2'))
		
	if com == 'cd: Аккаунты-Удалить':
		print(users)
#Neon Operating System v.2.0

import time
import faker
from faker import Faker
import colorama
from colorama import Fore, Back, Style
import pickledb
import rich
from rich.progress import track
import sys
import os

fake = Faker()
db = pickledb.load('NOS_2.db', True)
name_user = db.get('login')
name_user2 = db.get('login')
count_users = 1
users = [db.get('login'), db.get('login2')]
ram = '150'
install_root = False

if not db.exists('login'):
	db.set('login', input("Введите имя пользователя:"))
	db.set('password', input("Придумайте пароль:"))
	
else:
	if input('Введите пароль: ') != db.get('password'):
		print('Неверный пароль!')
		sys.exit()

def start_os():
	print(Fore.YELLOW + 'Загрузка ' + Fore.GREEN + 'ОС')
	time.sleep(2)
	print(Fore.YELLOW + 'Добро пожаловать в NOS!')
	
def off_os():
	print(Fore.GREEN + 'Завершение работы')
	time.sleep(2)
	
def no_system():
	while True:
		ns = input(Fore.RED + 'НЕТ СИСТЕМЫ!')
	
def addition_calc(a, b):
	c = a + b
	print("Результат: " + str(c))
	
def decrease_calc(a, b):
	c = a - b
	print("Результат: " + str(c))
	
def multiplication_calc(a, b):
	c = a * b
	print("Результат: " + str(c))
	
def division_calc(a, b):
	c = a / b
	print("Результат: " + str(c))
	
def multiplication2_calc(a, b):
	c = a ** b
	print("Результат: " + str(c))
	
def division2_calc(a, b):
	c = a // b
	print("Результат: " + str(c))
	
def division3_calc(a, b):
	c = a % b
	print("Результат: " + str(c))
	
start_os()
while True:
	com = input(Fore.YELLOW + 'Введите команду: ')
	
	if com == 'информация':
		print('NOS -- Neon Operating System -- была создана в 2023 году на языке программирования Python.')
		
	if com == 'перезагрузить':
		print(Fore.GREEN + '------------------------------------------------------------')
		start_os()
		
	if com == 'выключить':
		off_os()
		break
		
	if com == 'запустить $Калькулятор':
		what = input('Выберите действие: ')
		num1 = float(input('Введите первое число:'))
		num2 = float(input('Введите второе число:'))
		
		if what == '+':
			addition_calc(num1, num2)
			
		elif what == '-':
			decrease_calc(num1, num2)
			
		elif what == '*':
			multiplication_calc(num1, num2)
			
		elif what == '/':
			division_calc(num1, num2)
			
		elif what == '//':
			division2_calc(num1, num2)
			
		elif what == '**':
			multiplication2_calc(num1, num2)
			
		elif what == '%':
			division3_calc(num1, num2)
			
	if com == 'cd: Аккаунты-Новый':
		new_user = input('Введите имя нового пользователя: ')
		db.set('login2', new_user)
		print('Вы создали нового пользователя, ' + db.get('login2'))
		
	if com == 'cd: Аккаунты-Удалить':
		print(users)
		choice_delete = input('Напишите имя пользователя из списка, которого вы хотите удалить: ')
		
		if choice_delete == db.get('login'):
			print(Fore.RED + 'НЕЛЬЗЯ УДАЛИТЬ ОСНОВНОЙ АККАУНТ!')
		if choice_delete == db.get('login2'):
			db.rem('login2')
			
	if com == 'cd: Аккаунты-Тестовый':
		choice_test = input('Вы точно хотите переключиться на тестовый аккаунт?[y/n]: ')
		if choice_test == 'y':
			name_user2 = 'Alvin Diklin'
			print('Добро пожаловать, Alvin Diklin!')
		
	if com == 'cd: Аккаунты-Сменить':
		print(users)
		choice_user = input('Напишите имя пользователя из списка, на которого вы хотите смениться: ')
		
		if choice_user == db.get('login'):
			name_user2 = db.get('login')
			print('Добро пожаловать, ' + name_user2 + '!')
			
		if choice_user == db.get('login2'):
			name_user2 = db.get('login2')
			print('Добро пожаловать, ' + name_user2 + '!')
			
	if com == "системная информация":
		print('Имя пользователя: ' + name_user2)
		print('RAM: ' +str(ram) + 'mb')
		print('NOS v.2.0')
		
	if com == "запустить $AIBot":
		print(Fore.CYAN + 'Здравствуйте, чем могу быть полезен?')
		while True:
			vopAI = input('Введите сообщение: ')
			
			if vopAI == 'Как тебя зовут?':
				print('Меня зовут YooAIBot)')
				
			if vopAI == 'Сколько тебе лет?':
				print('Мне -1 год))')
				
			if vopAI == 'Где ты живешь?':
				print('Я живу на земле)))')
				
			if vopAI == 'Срегенерируй имя':
				count1 = int(input('Сколько вы хотите срегенерировать имен?: '))
				for names in range(count1):
					print(fake.name())
					
			if vopAI == 'Срегенерируй адрес':
				count2 = int(input('Сколько вы хотите срегегерировать адресов?: '))
				for addres in range(count2):
					print(fake.address())
					
	if com == 'установить $ROOT':
		  	print(Fore.GREEN + 'Установка. . .')
		  	time.sleep(12)
		  	install_root = True
		  	while True:
		  		root_inp = input('C:/sys48: ')
		  		
		  	
		  		if root_inp == 'выйти':
		  			break
		  		
		  		if root_inp == 'установить #RAM':
		  			ram_count = int(input('Сколько вы хотите установить ОЗУ?: '))
		  			if ram_count == 0:
		  				print('ОШИБКА 3')
		  			else:
		  				ram = ram_count
		  				print('Успешно!')
		  			
	if com == "удалить $ОС":
		vop = input("ВНИМАНИЕ! Если вы подтвердите операцию, то вы потеряете доступ к ОС? [y/n]: ")
		
		if vop == 'y':
			db.set('OSdelete', true)
			no_system()￼Enter		choice_delete = input('Напишите имя пользователя из списка, которого вы хотите удалить: ')
		
		if choice_delete == db.get('login'):
			print(Fore.RED + 'НЕЛЬЗЯ УДАЛИТЬ ОСНОВНОЙ АККАУНТ!')
		if choice_delete == db.get('login2'):
			db.rem('login2')
			
	if com == 'cd: Аккаунты-Тестовый':
		choice_test = input('Вы точно хотите переключиться на тестовый аккаунт?[y/n]: ')
		if choice_test == 'y':
			name_user2 = 'Alvin Diklin'
			print('Добро пожаловать, Alvin Diklin!')
		
	if com == 'cd: Аккаунты-Сменить':
		print(users)
		choice_user = input('Напишите имя пользователя из списка, на которого вы хотите смениться: ')
		
		if choice_user == db.get('login'):
			name_user2 = db.get('login')
			print('Добро пожаловать, ' + name_user2 + '!')
			
		if choice_user == db.get('login2'):
			name_user2 = db.get('login2')
			print('Добро пожаловать, ' + name_user2 + '!')
			
	if com == "системная информация":
t('Имя пользователя: ' + name_user2)
		print('RAM: ' +str(ram) + 'mb')
		print('NOS v.2.0')
		
	if com == "запустить $AIBot":
		print(Fore.CYAN + 'Здравствуйте, чем могу быть полезен?')
		while True:
			vopAI = input('Введите сообщение: ')
			
			if vopAI == 'Как тебя зовут?':
				print('Меня зовут YooAIBot)')
				
			if vopAI == 'Сколько тебе лет?':
				print('Мне -1 год))')
				
			if vopAI == 'Где ты живешь?':
				print('Я живу на земле)))')
				
			if vopAI == 'Срегенерируй имя':
				count1 = int(input('Сколько вы хотите срегенерировать имен?: '))
				for names in range(count1):
					print(fake.name())
					
			if vopAI == 'Срегенерируй адрес':
				count2 = int(input('Сколько вы хотите срегегерировать адресов?: '))
				for addres in range(count2):
