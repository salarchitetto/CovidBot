import subprocess

import discord
from discord.ext import commands
from covid import *
from config import Configs

client = discord.Client()
bot = commands.Bot(command_prefix="-")
bot.remove_command("help")


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"{member.name}, you've been Infected!"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '-covid help':
        coms = {'-infections': 'Show the global number of Covid-19 Infections',
                '-deaths': "Show the global number of Covid-19 Deaths",
                '-recovered': "Show the global number of Covid-19 Recoveries"}

        msg = discord.Embed(title='CovidBot',
                            description="Covid-19 Statistics",
                            color=0x0000ff)
        for command, description in coms.items():
            msg.add_field(name=command, value=description, inline=False)
        msg.add_field(name='Covid-Bot', value='Welcome', inline=False)
        await message.channel.send(message.channel, embed=msg)

    covidMain = Covid(Configs.COVID_MAIN)

    if message.content == "-infections":
        confirmedCases = covidMain.grabTotalConfirmed()
        await message.channel.send(f"There are {confirmedCases} of Covid-19 cases in the world right now")

    if message.content == "-deaths":
        confirmedDeaths = covidMain.grabTotalDead()
        await message.channel.send(f"There are {confirmedDeaths} of Covid-19 deaths in the world right now")

    if message.content == "-recovered":
        confirmedRecoveries = covidMain.grabTotalRecovered()
        await message.channel.send(f"There are {confirmedRecoveries} of Covid-19 recoveries in the world right now")

    if message.content.startswith("-country infections"):
        await message.channel.send("Please enter a country: I.E (USA, Spain, Italy)")

        msg = await client.wait_for("message")

        covid_country = Covid(Configs.COVID_COUNTRY, msg)
        user_response = covid_country.decodeHelper()
        print(user_response)
        country_information = covid_country.grabCountryInfectionCount()
        print(country_information)
        output = f"""{user_response} has {'{:,d}'.format(country_information['TotalCases'][user_response])} total cases,
        {'{:,d}'.format(int(country_information['TotalDeaths'][user_response]))} dead, and 
        {'{:,d}'.format(int(country_information['TotalRecovered'][user_response]))} recovered.
        """
        await message.channel.send(output)

client.run(Configs.DISCORD_BOT_ID)
