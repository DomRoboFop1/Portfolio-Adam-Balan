import discord
from discord.ext import commands
import random
import requests
import mysql.connector
from discord.ext import tasks

current_number = 0
game_active = False
players = []

api_key = "EoVhBxCDDk+a7EoMLnv1NgUz8F8xrp/o3s0sHpwgnVRMvH/c"
group_id = "32538858"

url = "https://www.roblox.com/groups/32538858/USAR-United-States-Army-Roleplay#!/about"

#response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})

#if response.status_code == 200:
 #   members = response.json()["data"]
  #  for member in members:
   #     print(f"Username: {member['username']}")
    #    print(f"ID: {member['id']}")
#else:
 #   print(f"Error: {response.status_code} - {response.text}")



dbconfig = {
    "host": "127.0.0.1",
    "user": 'root',
    'password': 'DomRoboFop',
    'database': 'Storage'
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "How do you organize a space party? You 'planet'!",
    "Why did the bicycle fall over? Because it was two-tired!",
]

@bot.command()
async def salam(ctx, arg):
    await ctx.send("Malejkum")

@bot.command()
async def help_me(ctx,arg):
    if arg == "Applications":
        await ctx.send("All applications are in Application Announcement channel.")
    elif arg == "Admin Help":
        await ctx.send(" Head to the Admin help channel where you may open your ticket.")
    elif arg == "Report":
        await ctx.send("Everything regarding report you may found in report channels.")
    elif arg == "Information":
        await ctx.send("All information you can find in information channel.")

@bot.command()
async def joke(ctx):
    await ctx.send("What’s the best thing about Switzerland? I don’t know, but the flag is a big plus :)))).")

@bot.command()
async def meet(ctx):
    await ctx.send("If you want to meet with head admin or owner you must send ticket in meeting request and the person who responded you will send you time when you can talk.")

@bot.command()
async def calculate(ctx, operation, num1: float, num2: float):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            await ctx.send("Cannot divide by zero.")
            return
    if result is not None:
        await ctx.send(f'Result: {result}')

bot.run("MTEyMjkyMzY0MjQzOTg2ODQ1Ng.G9oXUK.TJHUapeg2W12OQhNXQwgYC_JVU4giu2_KGQXnU")

