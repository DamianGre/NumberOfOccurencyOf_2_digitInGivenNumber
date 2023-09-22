#how many digits "2" are in the sequence of numbers from 0 to the given number and enters the number of occurrencestry
try:
    def user_input():
        user_in = ""
        user_in = input("Podaj liczbę całkowitą: ")
        while user_in.isdigit() == False or int(user_in) < 0:
            print("Podano złą wartość")
            user_in = input("Podaj liczbę całkowitą: ")
        return int(user_in)


    def counter_of_2_in_input():
        user_in = user_input()
        count = 0
        for number in range(user_in + 1):
            count += str(number).count('2')
        print(f'W ciągu liczb od 0 do {user_in} cyfra 2 została użyta {count} razy!')

    counter_of_2_in_input()
except:
  print("An exception occurred")