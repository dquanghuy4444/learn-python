# python -u app.py
import datetime

# 
print("Print")
# 
variable = 10
print(variable)
# 
variable = variable +12
print(variable)

# 
abcd = 'abcdef'
print(abcd[1:3])

# 
str2= 2222
str = f'Huy đẹp trai {str2}'
print(str)


# 
yearx = input("Năm sinh: ")
today = datetime.date.today()
year = today.year
age = year - int(yearx)
print(age)

