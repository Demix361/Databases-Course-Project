

def update(spent, level):
	if level != 'Алмазный' or spent != 0:
		arr = [[0, 10000, 40000, 70000, 150000, 300000], ['Отсутствует', 'Бронзовый', 'Серебряный', 'Золотой', 'Платиновый', 'Алмазный']]
		n = len(arr[0])

		for i in range(n - 1, -1, -1):
			if spent >= arr[0][i]:
				new_limit = arr[0][i]
				new_level = arr[1][arr[0].index(new_limit)]

				if arr[0][arr[1].index(level)] > arr[0][arr[1].index(new_level)]:
					return level
				else:
					return new_level
	else:
		return level


for i in range(0, 560000, 17439):
	level = 'Алмазный'

	new_level = update(i, level)
	print('-' * 40)
	print(f'spent: {i}')
	print(f'{level} --> {new_level}')



