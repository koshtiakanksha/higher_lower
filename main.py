from random import randint
from art import logo, vs
from game_data import data

print(logo)
def celebs():
    A = data[randint(0, len(data) - 1)]
    game_over = False
    final_score = 0
    while not game_over:
        B = data[randint(0, len(data) - 1)]
        while B == A:
            B = data[randint(0, len(data) - 1)]
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} ")
        print(vs)
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']} ")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if A['follower_count']> B['follower_count'] and guess=='a':
            game_over = False
            final_score +=1
            print(f"You're right. Your current score: {final_score}")
        elif A['follower_count']< B['follower_count'] and guess=='b':
            game_over = False
            final_score += 1
            print(f"You're right. Your current score: {final_score}")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {final_score}")
        A = B
celebs()