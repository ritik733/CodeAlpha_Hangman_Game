import random

f= open("word.txt","r")
data = f.readline()
words = data.split(",")

word = random.choice(words)
word = word.lower()

total_chances = 7
guessed_word = '-' * len(word)

while total_chances != 0:

  print(guessed_word)
  
  letter = input("Gusse a letter: ").lower()
  
  if letter in word:
    print ("Good")
    for index in range(len(word)):
      if word[index] == letter:
        guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
        print(guessed_word)
    
    if guessed_word == word:
      print ("Congratulations! You gussed the word correctly.")
      break
      
  else:
    total_chances -= 1
    print("Incorect guess. You have", total_chances, "chances left.")
else:
  print ("Game Over : You Lose")
  print ("All Chances are over")
  print ("The word was", word)
        
