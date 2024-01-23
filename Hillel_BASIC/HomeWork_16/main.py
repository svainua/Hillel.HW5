from HW5_task_3 import make_odd_list
from Task import do_summ

print("Here is the first function:")
number = int(input("Please choose the number: \n"))
print(f"The result of the first function is: {make_odd_list(number)}")

print()

print("Here is the second function:")
do_summ_here = do_summ()
print(f"The result of the second function is: {do_summ_here}")
