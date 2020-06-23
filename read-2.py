data = []
count = 0 #count=計數(此用來計算清單長度)
with open('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count=count+1
		if count % 1000 == 0: #%=餘數
			print(len(data))
print('檔案讀取完了，總共有', len(data) ,'筆資料')
		
sum_len = 0 #總長度
for d in data: #因為已將line存入data清單 清單才能算字串長度
	sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len / len(data))