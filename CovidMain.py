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

    if message.content == "-covid help":
        coms = {"-infections": "Show the global number of Covid-19 Infections",
                "-deaths": "Show the global number of Covid-19 Deaths",
                "-recovered": "Show the global number of Covid-19 Recoveries",
                "-country infections": "Search for a specific countries Covid-19 metrics"}

        msg = discord.Embed(title="CovidBot",
                            description="Covid-19 Statistics",
                            color=0x0000ff)
        for command, description in coms.items():
            msg.add_field(name=command, value=description, inline=False)
        msg.add_field(name="Covid-Bot", value="Welcome", inline=False)
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
        if msg.content == "South Korea":
            msg.content = "S. Korea"

        covid_country = Covid(Configs.COVID_COUNTRY, msg.content)

        country_information = covid_country.grabCountryInfectionCount()
        print(country_information)

        def nanChecker(a_dict, lookup, content):
            if str(a_dict[lookup][content]) == "nan":
                return str(a_dict[lookup][content]).replace("nan", "0")
            else:
                return '{:,d}'.format(int(a_dict[lookup][content]))

        cases = nanChecker(country_information, "TotalCases", msg.content)
        deaths = nanChecker(country_information, "TotalDeaths", msg.content)
        recovered = nanChecker(country_information, "TotalRecovered", msg.content)

        output = f"{msg.content} has {cases} total cases," + \
                 f"{deaths} dead," + \
                 f" and {recovered} recovered."

        await message.channel.send(output)


client.run(Configs.DISCORD_BOT_ID)
