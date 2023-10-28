from dotenv import load_dotenv
load_dotenv()

import discord
from discord.ext import commands

import os

token = os.getenv("TOKEN")

client = commands.Bot(command_prefix = "k!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("[INFO] Luh Kranky has booted!")

@client.command()
async def hello(ctx):
    await ctx.send("Yuh wsg twizz")

client.run(token)