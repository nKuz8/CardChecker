CRADS = {2: 'MUP', 4: 'VISA', 5: 'MASTERCARD', 6: 'CUP'}

class InvalidCardException(Exception):
	pass


def main():
	while 1:
		card_input = input("Введите номер карты: ").rstrip('\n')
		card = list(map(int, list(card_input)))

		try:
			check_card(card)
			break
		except InvalidCardException as e:
			print(e)	


def check_card(card_number):
	if len(card_number) != 16:
		raise InvalidCardException("Неверное количество символов (" + 
			str(len(card_number)) + ")")
	try:	
		paying_system = CRADS[card_number[0]]
	except KeyError:
		raise InvalidCardException("Неизвестная платежная система")

	if luhn(card_number) != True:
		raise InvalidCardException("Неверный номер карты")
	else:
		print('Валидная карта')	


def luhn(card_number):
	control_sum = 0

	for i in range(0, len(card_number) - 1, 2):
		double = card_number[i]*2
		if double > 9:
			double -= 9
		control_sum += double	

	for i in range(1, len(card_number), 2):
		control_sum += card_number[i]	

	if control_sum % 10 == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	main()