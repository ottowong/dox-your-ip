from requests import get

import discord

client = discord.Client()
@client.event
# whenever a message is sent this will run
async def on_message(message):
    # if the sender of the message is the bot, don't do anything
    if (message.author == client.user):
        return

    if(str.lower(message.content) == "!ip"):
        try:
            ip = get('https://api.ipify.org').text
            print (ip)
            await message.channel.send("http://"+str(ip))
        except Exception as e:
            print(str(e))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# your bot token will be roughly this length with some .s in it:
# aaaaaaaaaaaaaaaaaaaaaaaa.aaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaa
# token should be on this page:
# discordapp.com/developers/applications/[your bot]/bots

client.run('TOKEN')

