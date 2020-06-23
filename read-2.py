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
for d in data: #data=清單 清單才能算字串長度 d=每一筆留言
	sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100: #留言長度是算字母
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])