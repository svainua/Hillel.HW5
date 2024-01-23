"""Напишіть функцію використовуючи обробку винятків, яка запитує введення двох значень.
Якщо хоча б одне з них не є числом, то має виконуватися конкатенація, тобто з'єднання. 
В інших випадках введені числа підсумовуються (сума чисел)."""

def do_summ():
    """The function does the Summing or Concatenation, depending on type of the input"""
    input_1 = input("Please enter 1st number:\n")
    input_2 = input("Please enter 2nd number:\n")

    try:
        result = int(input_1) + int(input_2)
    except ValueError:
        result = str(input_1) + str(input_2)
    finally:
        return result



    

