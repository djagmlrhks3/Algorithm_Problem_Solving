"""
find('찾을문자열', 'FROM_IDX(생략가능)', 'TO_IDX(생략가능)')
- 존재하면 해당 위치의 인덱스
- 존재하지 않으면 -1
"""
result = input().rstrip()
idx1 = result.find('12')
idx2 = result.find('21')
if idx1 == -1 or idx2 == -1:
	print("No")
else:
	if idx1 < idx2:
		if result.find('21', idx1+2) == -1:
			print("No")
		else:
			print("Yes")
	else:
		if result.find('12', idx2+2) == -1:
			print("No")
		else:
			print("Yes")