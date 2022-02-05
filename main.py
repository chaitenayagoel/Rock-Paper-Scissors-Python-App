rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

b = [rock,paper,scissors]
length = len(b)

c = random.randint(0,length-1)
print(f'You chose:\n{b[a]}')
print("Computer chose: ")
if c==0:
  print(rock)
elif c ==1:
  print(paper)
else:
  print(scissors)




if a == 0:
  if c == 1:
    print("You Lose")
  elif c == 2:
    print("You Win")
  else:
    print("Drawn")

elif a == 1:
  if c == 0:
    print("You Win")
  elif c == 2:
    print("You Lose")
  else:
    print("Drawn")

else:
  if c == 0:
    print("You Lose")
  elif c == 1:
    print("You Win")
  else:
    print("Drawn")




