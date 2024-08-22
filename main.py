import os
import discord


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#@client.event
#async def on_message(message):
    #if message.author == client.user:
        #return
    #if message.content.startswith('Hello') or message.content.startswith('hello') :
        #await message.channel.send('Hello!')
 

#@client.event
#async def on_member_join(member):
    #print(member)  # This will print the member information in the console
    #channel = client.get_channel(1276010237882662925)
    #if channel:  # Check if channel is found
        #await channel.send(f'Welcome {member.mention} to the server')
    #else:
        #print("Channel not found")

@client.event
async def on_member_join(member):
    channel = client.get_channel(1276010237882662925)  # Replace with your channel ID
    if channel:
        embed = discord.Embed(color=discord.Color.blue(), description=f"Welcome {member.mention}!")
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        embed.set_author(name=member.name, icon_url=avatar_url)
        embed.set_thumbnail(url=avatar_url)
        embed.add_field(name="Welcome to the server!", value=f"Glad to have you, {member.name}!")
        await channel.send(embed=embed)
    else:
        print("Channel not found") 


client.run('Token')