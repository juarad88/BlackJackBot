import discord, os
import random
from PIL import Image,ImageDraw
from discord.ext import commands

TOKEN = os.environ['token']

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)
'''

@client.command("play")
while player_hand
async def deal(ctx):
    # Deal two cards to the player
    player_hand = [random.randint(1, 10) for i in range(2)]
    dealer_hand = [random.randint(1, 10) for i in range(2)]

    # Send the cards to the chat channel
    await ctx.channel.send(f"Player's hand: {player_hand}\nDealer's hand: {dealer_hand[0]}")
    return player_hand 

@client.command("hit")
async def hit(ctx):
    # Deal one additional card to the player
    player_hand.append(random.randint(1, 10))

    # Send the new card to the chat channel
    await ctx.channel.send(f"Player's hand: {player_hand}")
    

#Creates a list of cards 
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#Defines a set value for each card from the list
card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


def user_hand():
  hand = []
  hand.append(random.choice(cards))
  
  return hand
  
hand_value = 0
for card in hand:
  card_value = card_values[card]
  hand_value += card_value
  
if "A" in hand and hand_value + 10 <= 21:
  hand_value += 10

while hand_value < 21:
  @client.command("play")
  user_hand()

print("Player's hand:", hand)
print("Hand value:", hand_value)

'''
words = ["jazz", "zinc", "cycle", "lymph", "onyx"]


class Guess:

  def __init__(self):
    self.random_word = list(random.choice(words))
    self.guess = ['?' for letter in self.random_word]
    self.misses = 0
    self.guessed_letters = []

  def user_guess(self, ctx, letter):
    count = 0
    if letter in self.random_word:
      for i in range(len(self.random_word)):
        if self.random_word[i] == letter:
          self.guess[i] = letter
          count += 1
    else:
      self.misses+=1
      if letter not in self.guessed_letters:
        self.guessed_letters.append(letter)
    return count


@client.command("test")
async def test(ctx):
  await ctx.channel.send(guess.guess)
  await ctx.channel.send(guess.random_word)

def prepare_image():
  img = Image.open("stage-"+str(guess.misses)+".png")
  EditedImage = ImageDraw.Draw(img)
  EditedImage.text((10,10),"".join(guess.guess),fill = (255,0,0))
  img.save("to_send.png")
  


@client.command("guess")
async def try_letter(ctx, letter):
  results = guess.user_guess(ctx, letter)
  prepare_image()
  if results > 0:
    await ctx.channel.send("correct!")
    await ctx.channel.send(guess.guess)
  else:
    await ctx.channel.send("Incorrect")
  
  await ctx.channel.send("guess again",file=discord.File("to_send.png"))
 
      


      
    


guess = Guess()

client.run(TOKEN)
