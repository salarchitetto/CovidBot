# CovidBot

During this quarantine I thought to myself, what should I do with my spare time? Well I figured I would learn how to make a Discord bot since all my buddies decided to migrate over to the platform. 

The idea started from constantly checking the [Johns Hopkins website](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) . Being the lazy person that I am I didn't want to constantly refresh it and watch the staggering numbers unfold, which led to this beautifully unnecessary bot. 

The bot pulls data from this website [here](https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%20) , shout out to them. As of right now the bot does a few things which I'll list below: 
##

| The Bot Command | What It Returns  |
|--|--|
|-infections  |Pulls the global number of Covid-19 infections  |
|-deaths|Pulls the global number of deaths|
|-recovered|Pulls the global number of recoveries|
|-country infections|Maps the country which the user inputs and returns # of cases/deaths/recoveries of that given country. |
|-covid help|General help embedded message to help you traverse this bot|

## How to Install the bot on your Discord Server
First you need someone with admin access to your discord server in order to have it join. Once you've got that ready follow this link [here](https://discordapp.com/api/oauth2/authorize?client_id=701418790654836746&permissions=0&scope=bot), from there you should be able to just choose the specific server you want the bot to join and that's it. 