password = 'a123456'
pwd = input('Please enter password : ')
while pwd == password:
	print('Correct and Logining ...')
	break
i = 3
while i > 0:
	i = i - 1
	print('wrong! you have', i , 'times chance') 
	pwd = input('Please enter password : ')
print('Lock') 