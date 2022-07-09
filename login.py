password = 'a123456'
i = 3 #剩餘機會
while True:
	pwd = input('Please enter password : ')
	if pwd == password:
		print('Correct and Logining ...')
		break
	else:
		i = i - 1
		print('wrong! you have', i , 'times chance') 
		if i == 0:
			break
print('lock')
