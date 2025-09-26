employees = [
    {'name': '김지원', 'salary': 3700000},
    {'name': '박민준', 'salary': 7000000},
    {'name': '이서연', 'salary': 4400000},
    {'name': '정현우', 'salary': 3500000}
]
updated_employee = list(map(lambda emp: {'name': emp['name'], 'salary': emp['salary'] * 1.1}, employees))
print('-- 급여 인상 후 --')
for emp in updated_employee:
    print(f'{emp["name"]}: {int(emp["salary"]):,}원')