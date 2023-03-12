import discord
import random
from discord.ext import commands

TOKEN = "MTA4MDk2MDY1NTc0NzcxOTE3OQ.GUrcZq.V7ej6fn2cLayxwly316fQJpZHyl57oqUGTz4CY"

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
    self.guess = ['-' for letter in self.random_word]

  def user_guess(self, ctx, letter):
    count = 0
    if letter in self.random_word:
      for i in range(len(self.random_word)):
        if self.random_word[i] == letter:
          self.guess[i] = letter
          count += 1
    return count


@client.command("test")
async def test(ctx):
  await ctx.channel.send(guess.guess)
  await ctx.channel.send(guess.random_word)


@client.command("guess")
async def try_letter(ctx, letter):
  results = guess.user_guess(ctx, letter)
  if results > 0:
    await ctx.channel.send("correct!")
    await ctx.channel.send(guess.guess)
  else:
    await ctx.channel.send("guess again")


guess = Guess()

client.run(TOKEN)
