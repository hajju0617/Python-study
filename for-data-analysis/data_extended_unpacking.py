monthly_sales = [1200, 1350, 1420, 1500, 1300, 1580, 1620, 1700, 1800, 1850, 1900, 2000]

first, *middle, last = monthly_sales
print(f'첫 달(1월) 판매액 : {first}')
print(f'마지막 달(12월) 판매액 : {last}')
print(f'중간 달(2~11월) 판매액 : {middle}\n')

first, second, *remaining = monthly_sales
print(f'1월 판매액 : {first}')
print(f'2월 판매액 : {second}')
print(f'나머지 월 판매액 : {remaining}')