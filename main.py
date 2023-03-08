import discord
import random
from discord.ext import commands

TOKEN = "MTA4MDk2MDY1NTc0NzcxOTE3OQ.GWvIBp.G-WQ5f50btdE5w73c2_T6PnSHOB9MIm2tpUg3Y"

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

''''
client.run(TOKEN)
