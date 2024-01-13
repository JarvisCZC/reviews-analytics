data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 
		if count % 1000 == 0: #count 跟1000求餘數，代表1000的倍數才會運作
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)
	print(sum_len)
print('每一筆留言的平均長度為', sum_len / len(data))