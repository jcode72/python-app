'''import datetime

user_input = input('enter you goal with deadline separated by colon\n')
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, '%d.%m.%Y')
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f'Dear user! Time remaing for your goal: {goal} is {time_till.days} days') # noqa'''

print('hello there')
user_name = input("Enter you name here\n")
print((user_name) + ' thanks for playing with me!')
