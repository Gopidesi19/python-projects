import datetime

user_input = input("enter your goal with deadline\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
#calculate how many days from now till deadline
today_date = datetime.datetime.today()
time_till = deadline_date-today_date
print(f"Dear user time remaining for your learning {goal} is {time_till.days} days")
