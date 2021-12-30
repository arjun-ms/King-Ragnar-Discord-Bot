import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
from db import mydb
import os
from dotenv import load_dotenv

load_dotenv()
mycursor = mydb.cursor()


key = os.environ["KEY"]


intents = discord.Intents.all()             #let us know who is joining the server
intents.members = True                          #let us know who is joining the server
client = commands.Bot(command_prefix='!',intents = intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Sends hello 
# @client.event
# async def on_message(message):
#     if (message.author == client.user):
#         return

#     if(message.content.startswith('$hello')):
#         await message.channel.send('Hello')

# Greetings
@client.event
async def on_member_join(member):
    print(f"{member} joined the server")
    try:
        channel = discord.utils.get(member.guild.text_channels, name="welcome-and-rules")
        await channel.send(f'Welcome to the server {member.mention} !')     #Welcome the member on the server

    except Exception as e:
        raise e

# while adding a reaction to a message, send a message to a channel (<user> gave reaction to <user>)
@client.event
async def on_raw_reaction_add(payload):
    sentmsg_channel = client.get_channel(payload.channel_id)
    msg = await sentmsg_channel.fetch_message(payload.message_id)
    channel=discord.utils.get(msg.author.guild.text_channels, name="reactions")
    print(f"{payload.member}  gave reaction to  {msg.author}  in  #{sentmsg_channel}")
    await channel.send(f"{payload.member}  gave reaction to  {msg.author}  in  #{sentmsg_channel}")



# parameterized command, create a role named the parameter received, and assign it to the user.
@client.command()
async def role(ctx,*args):
    if(len(args)>0):
        member = ctx.author
        role = get(ctx.guild.roles,name=args[0])
        if(role==None):
            role = await ctx.guild.create_role(name=args[0])
        print(f"{member} has created role {role}")
        await member.add_roles(role)




# using a parameterized command(eg - !register <name>) insert the name to the database, if the same name tries to register again send an error message to the channel.
@client.command()
async def register(ctx,*args):
    if(len(args)>0):
        name = args[0]
        mycursor.execute("USE mydb")
        find_sql = "SELECT name FROM users WHERE name=%s"
        insert_sql = "INSERT INTO users (name) VALUES (%s)"
        val = (name,)
        mycursor.execute(find_sql,val)
        data =mycursor.fetchall()
        if(len(data)>0):
            await ctx.send("Name already registered")
            print("Name already registered")
        else:
            mycursor.execute(insert_sql,val)
            mydb.commit()
            await ctx.send("Name Registered Successfully")
            print("Name Registered Successfully")



# with a role restricted command retrieve all names in the database ( eg - !names)

@client.command()
@commands.has_role('arjunms')
async def names(ctx):
    mycursor.execute("USE mydb")
    find_sql = "SELECT name FROM users"
    mycursor.execute(find_sql)
    data = mycursor.fetchall()
    username = ""
    for i in range(len(data)):
        username += data[i][0]+"\n"
    await ctx.send(username)


client.run(key)
