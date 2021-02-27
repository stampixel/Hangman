#Codes related to the pictures
from IPython.display import display
from PIL import Image
import requests
from io import BytesIO
import random
url = "https://i.imgur.com/RWgekjY.png" # link to image
response = requests.get(url)
img = Image.open(BytesIO(response.content)) # open the picture from the online link
img_1 = img.crop((100,50,275,275)) # crop the image
img_2 = img.crop((350,50,525,275))
img_3 = img.crop((600,50,800,275))
img_4 = img.crop((100,300,275,550))
img_5 = img.crop((350,300,525,550))
img_6 = img.crop((600,300,800,550))
img_7 = img.crop((300,550,550,800))

# get word lists from google drive
from google_drive_downloader import GoogleDriveDownloader as gdd
# link to google sheets: https://docs.google.com/spreadsheets/d/1boqSxAk-N-kKRuCDvExvGBxMcAO99LDy/edit#gid=332790544
gdd.download_file_from_google_drive(file_id='1boqSxAk-N-kKRuCDvExvGBxMcAO99LDy',
                                    dest_path='./Wordlist.xlsx',
                                    unzip=False, showsize=True)
import pandas as pd
df = pd.read_excel("Wordlist.xlsx", sheet_name=0)
# word lists for different categories
wordlist_sports = df["Sports"].dropna().tolist()
wordlist_nature = df["Nature"].dropna().tolist()
wordlist_food = df["Food"].dropna().tolist()
wordlist_vechicles = df["Vehicles"].dropna().tolist()
wordlist_animals = df["Animals"].dropna().tolist()
wordlist_python = df["Python"].dropna().tolist()




default_word_list = ["linear", "fail", "cucumber", "aisle", "satisfaction", "wander", "canada", "python","concete", "banana", "excess", "giggit", "voodoo", "pullup", "myrrhy"]

# def get_number_input():
#   while True:
#     userInput = input("Enter an integer from 1-6: ")
#     try:
#       userInput = int(userInput)
#       if (userInput > 0 and userInput < 7):
#         break
#     except:
#       pass
#   return userInput

class Hangman():
  def __init__(self, lifeCount=6, word_list=default_word_list):
    self.lifeCount = lifeCount
    self.word_list = word_list

  def run(self):
    randomWord = random.choice(self.word_list).lower()
    randomWord
    n=0
    #print("How many lives do you need? ")
    # self.lifeCount = get_number_input()
    display(img_1)
    guess_history = ""
    while n<self.lifeCount:
      output = ""
      for letter in randomWord:

        if (letter in guess_history):
          output += letter + " "
        else:
          output += "_ "
      print(output)
      if "_" not in output:
        print("Congratulations! You won!")
        return True
        # break
      else: # check if there are _
        userGuess = ""
        while len(userGuess)!=1:
          userGuess = input("Please input a single letter\n").lower()
        guess_history += userGuess
        if userGuess not in randomWord:
          n+=1
        if (6-n==5):
          display(img_2)
        if (6-n==4):
          display(img_3)
        if (6-n==3):
          display(img_4)
        if (6-n==2):
          display(img_5)
        if (6-n==1):
          display(img_6)
        if (6-n==0):
          display(img_7)
        if n==self.lifeCount:
          #print('You have lost! Try again?')
          print(f"Correct answer: {randomWord}")
          return False
      print(f"n={n}")

  def chooseCategory(self):
    while True:
      categoryInput = input("Which category do you want to play? Enter 1 for sports, 2 for nature, 3 for food, 4 for vehicles, 5 for animals, and 6 for python. ")
      try:
        categoryNumber = int(categoryInput)
        if (categoryNumber > 0):
          break
      except:
        pass

    if (categoryNumber == 1):
      print("You picked the sports category.")
      self.word_list = wordlist_sports
    elif (categoryNumber == 2):
      print("You picked the nature category.")
      self.word_list = wordlist_nature
    elif (categoryNumber == 3):
      print("You picked the food category.")
      self.word_list = wordlist_food
    elif (categoryNumber == 4):
      print("You picked the vehichles category.")
      self.word_list = wordlist_vechicles
    elif (categoryNumber == 5):
      print("You picked the animals category.")
      self.word_list = wordlist_animals
    elif (categoryNumber == 6):
      print("You picked the python category.")
      self.word_list = wordlist_python
    else :
      print("You picked the default category")
      self.word_list = default_word_list

while True:
  new_game = Hangman(6, default_word_list)
  new_game.chooseCategory()
  win = new_game.run()
  if (win == True):
    break
  elif (win == False):
    tryAgain = input('You have lost! Try again? Enter yes or no.')
    if (tryAgain == "no"):
      break
    else:
      pass