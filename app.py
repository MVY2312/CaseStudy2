# Developed by:
# Morgun Vlada - 65%, Gevorgyan Alla - 35%
print('Здравствуйте! Хотите узнать свой годовой налог?(Y/N)')
answer = input()
if answer == 'N':
    print('Всего доброго!')
    exit(0)
def every_month():
    annual_income = 0
    name_month = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре'] 
    for month in range(12):
        print('Введите ваш доход в', name_month[month], end='')
        income = int(input(': '))
        annual_income += income
        return annual_income
def per_month():
    annual_income = int(input('Укажите ваш ежемесячный доход: '))*12
    return annual_income
print('Ваш месячный доход изменялся в течение года?(Y/N)')
answer_income=input()
if answer_income == 'Y':
    annual_income = every_month()
elif answer_income == 'N':
    annual_income = per_month()
print('Ваш годовой доход составил', annual_income, 'долларов')
print('Укажите ваше семейное положение: 1 - Холост/Не замужем; 2 - Женат/Замужем; 3 - Отец/Мать одиночка')
number_type = int(input())
S1 = 0.1
S2 = 0.15
S3 = 0.25
S4 = 0.28
S5 = 0.33
S6 = 0.35
S7 = 0.396
S = [S1, S2, S3, S4, S5, S6, S7]
def tax_for_unmarried():
    D1 = 0
    D2 = 9075
    D3 = 36900
    D4 = 89350
    D5 = 186350
    D6 = 405100
    D7 = 406750
    D = [D1, D2, D3, D4, D5, D6, D7, annual_income]
    D.sort()
    tax=0
    for element in range(1,len(S)+1):
        tax += S[element-1] * (D[element] - D[element - 1])
        if D[element] == annual_income:
            break
    return tax
def tax_for_married():
    D1 = 0
    D2 = 18150
    D3 = 73800
    D4 = 148850
    D5 = 226850
    D6 = 405100
    D7 = 457600
    D = [D1, D2, D3, D4, D5, D6, D7, annual_income]
    D.sort()
    tax = 0
    for element in range(1, len(S)+1):
        tax += S[element - 1] * (D[element] - D[element - 1])
        if D[element] == annual_income:
            break
    return tax
def tax_for_lonely_parents():
    D1 = 0
    D2 = 12950
    D3 = 49400
    D4 = 127550
    D5 = 206600
    D6 = 405100
    D7 = 432200
    D = [D1, D2, D3, D4, D5, D6, D7, annual_income]
    D.sort()
    tax = 0
    for element in range(1, len(S)+1):
        tax += S[element - 1] * (D[element] - D[element - 1])
        if D[element] == annual_income:
            break
    return tax
type_of_tax = [tax_for_unmarried(), tax_for_married(), tax_for_lonely_parents()]
tax_income = type_of_tax[number_type - 1]
print('Все готово!')
print('Ваш налог составил', tax_income, 'долларов')
