data = []
count = 0 #count=計數(此用來計算清單長度)
with open('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count=count+1
		if count % 1000 == 0: #%=餘數
			print(len(data))
print(len(data))

print(data[0])
print('------------')
print(data[1])