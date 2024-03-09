import random

def get_numbers_ticket(min, max, quantity):
   
        if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
            return [] 
        numbers = random.sample(range(min, max + 1), quantity)
        return sorted(numbers)
   

while True:
   
    try:
        print(get_numbers_ticket(int(input('min:')),int(input('max:')), int(input('quantity:'))))
        break
    except ValueError:
        print ('Ви ввели некоректні дані')
   



    

