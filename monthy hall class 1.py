import numpy as nm

# gift_door = nm.random.randint(1,4)
# user_guess = nm.random.randint(1,4)

# print("gift_door", gift_door)
# print("user_guess", user_guess)

#not-switch
# if user_guess == gift_door:
#     print("---------Hooraa!You Win-------")
# if user_guess != gift_door:
#     print("---------Loseeeeeeeee-------")

i = 0
total_wins = 0
total_lost = 0
total_attempt = 10000
while i < total_attempt+1:
    i = i + 1

    gift_door = nm.random.randint(1, 4)
    user_guess = nm.random.randint(1, 4)

    if user_guess == gift_door:
        total_wins = total_wins + 1
        # print("---------Hooraa!You Win-------")
    if user_guess != gift_door:
        total_lost = total_lost + 1
        # print("---------Loseeeeeeeee-------")

print('total_attempt',total_attempt)
print("total_wins", total_wins)
print("total_lost", total_lost)
print("nesbat_bord" , total_wins/total_attempt)