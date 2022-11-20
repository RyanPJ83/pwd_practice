password = 'a12345'
cnt = 3
while cnt > 0:
	guess_1 = input('plz input password: ')
	if guess_1 == password:
		print('Congratuation!')
		break
	else:
		cnt = cnt - 1
		print('還有', cnt, '次機會')