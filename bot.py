# version 0.0.7 of RapakkoBot 17/11/21

import asyncio
import random
import io
import aiohttp
import os
import json
import re
import dotenv
from dotenv import load_dotenv
import requests

import discord
from discord.ext import commands
from discord.ext.commands import Bot


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = Bot('!')
client.remove_command('help')


embedColour = discord.Colour.from_rgb(0, 247, 255)
embedFooterText = 'This is a placeholder'
embedFooterIcon = ''


def __init__(self):
    self.bot = discord.Client()


@client.event
async def on_messages(message):
    if message.author == client.user:
        return


# features without user input

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!help'))
    

# bot join message

@client.event
async def on_guild_join(guild):
    
    channel = discord.utils.get(guild.text_channels, name='general')

    embed = discord.Embed( 
    description = 'Hello there! My name is RapakkoBot. Use !help to see how you can utilize my features!\n',
    colour = embedColour)

    await channel.send(embed=embed)
    

# welcome message

@client.event
async def on_member_join(member: discord.member):
    channel = discord.utils.get(member.guild.text_channels, name='welcome')
    #rules_channel = discord.utils.get(member.guild.text_channels, name='rules')

    await channel.send(f'Welcome to **{member.guild.name}** {member.mention}! Enjoy your time here!')


# reaction roles

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id


# add matchmaking role

    if message_id == 758669436705046529:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'crewmate_red':
            role = discord.utils.get(guild.roles, name='Matchmaking')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print('Done')
            else: print('Member not found')
        else:
            print('Role not found')


# add color roles

    if message_id == 759049512483946508:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        
        if payload.emoji.name == 'crewmate_pink':
            role = discord.utils.get(guild.roles, name='Pink')

        elif payload.emoji.name == 'crewmate_red':
            role = discord.utils.get(guild.roles, name='Red')

        if payload.emoji.name == 'crewmate_orange':
            role = discord.utils.get(guild.roles, name='Orange')

        elif payload.emoji.name == 'crewmate_yellow':
            role = discord.utils.get(guild.roles, name='Yellow')

        if payload.emoji.name == 'crewmate_lime':
            role = discord.utils.get(guild.roles, name='Lime')

        elif payload.emoji.name == 'crewmate_green':
            role = discord.utils.get(guild.roles, name='Green')

        if payload.emoji.name == 'crewmate_cyan':
            role = discord.utils.get(guild.roles, name='Cyan')

        elif payload.emoji.name == 'crewmate_blue':
            role = discord.utils.get(guild.roles, name='Blue')

        if payload.emoji.name == 'crewmate_purple':
            role = discord.utils.get(guild.roles, name='Purple')

        elif payload.emoji.name == 'crewmate_white':
            role = discord.utils.get(guild.roles, name='White')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print('Done')
            else: print('Member not found')
        else:
            print('Role not found')


# add matchmaking ping role

    if message_id == 761304013421281350:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'ping':
            role = discord.utils.get(guild.roles, name='MM Ping')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print('Done')
            else: print('Member not found')
        else:
            print('Role not found')


# remove member role 

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 758638294472458262:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'checkmark':
            role = discord.utils.get(guild.roles, name='Member')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print('Done')
            else: print('Member not found')
        else:
            print('Role not found') 




# remove matchmaking role 

    message_id = payload.message_id
    if message_id == 758669436705046529:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'crewmate_red':
            role = discord.utils.get(guild.roles, name='Matchmaking')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print('Done')
            else: print('Member not found')
        else:
            print('Role not found')         


# remove color roles 

    message_id = payload.message_id
    if message_id == 759049512483946508:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'crewmate_pink':
            role = discord.utils.get(guild.roles, name='Pink')

        elif payload.emoji.name == 'crewmate_red':
            role = discord.utils.get(guild.roles, name='Red')

        if payload.emoji.name == 'crewmate_orange':
            role = discord.utils.get(guild.roles, name='Orange')

        elif payload.emoji.name == 'crewmate_yellow':
            role = discord.utils.get(guild.roles, name='Yellow')

        if payload.emoji.name == 'crewmate_lime':
            role = discord.utils.get(guild.roles, name='Lime')

        elif payload.emoji.name == 'crewmate_green':
            role = discord.utils.get(guild.roles, name='Green')
 
        if payload.emoji.name == 'crewmate_cyan':
            role = discord.utils.get(guild.roles, name='Cyan')

        elif payload.emoji.name == 'crewmate_blue':
            role = discord.utils.get(guild.roles, name='Blue')

        if payload.emoji.name == 'crewmate_purple':
            role = discord.utils.get(guild.roles, name='Purple')

        if payload.emoji.name == 'crewmate_white':
            role = discord.utils.get(guild.roles, name='White')
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print('Done')
            else: print('Member not found')
        else:
            print('Role not found')     


# remove matchmaking ping role 


    message_id = payload.message_id
    if message_id == 761304013421281350:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'ping':
            role = discord.utils.get(guild.roles, name='MM Ping')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print('Done')
            else: print('Member not found')
        else:
            print('Role not found') 


# text commands

# random emoji command

@client.command()
async def emoji(ctx):

    emojis = ['<:SleepySulo:888035815714861088>', '<:SleepySulo2:888035816117526548>']

    await ctx.send(random.choice(emojis))


# deleted message log

@client.event
async def on_message_delete(message):

    channel = discord.utils.get(message.guild.text_channels, name='bot-log')    
    
    if not message.author.has_permissions(manage_messages):

        await channel.send(f'**Deleted message** \nMessage: {message.content} \nSent by: **{message.author}** in **#{message.channel.name}** \n')
        return

@client.event
async def on_message(message):
    if '<@745237775028060232>' in message.content or '<@!745939861017722921>' in message.content: #tänne botin ID. Molemmissa muodoissa, koska mobiililla ja pyötäkoneella eri muoto
        await message.channel.send(f'Hello {message.author.mention}! Do you need help with something? Try using !help to learn more about me!')
    await client.process_commands(message) #ilman tätä muut komennot ei toimi


@client.event
async def on_message(message):
    if client.mentioned_in(message):
        await message.channel.send(f'Hello {message.author.mention}! Do you need help with something? Try using !help to learn more about me!')


# help command

@client.command()
async def help(ctx):

    embed = discord.Embed(title = 'Go check out the RapakkoBot GitHub page for the full documentation!',
    url = 'https://github.com/Rapakko/RapakkoBot',
    colour = embedColour)
    

    await ctx.send(f'''**Here are all the available commands:**\n ```
!help   -  Shows this help message\n
!join   -  I join the voice channel you are on\n
!leave  -  I leave the voice channel I am on\n
!clear  -  Removes specified number of messages  Usage: !clear 5\n
!purge  -  Removes all messages from the channel the command is used on\n
!kick   -  Kicks mentioned member, you can specify a reason but it isn't mandatory   Usage: !kick @member reason\n
!ban    -  Gives "Banned" role to mentioned member forcing them to a specific "Banned" channel with
no permission to send messages, you can specify a reason but it isn't mandatory  Usage:  !ban @member reason\n
!pban   -  Permanently bans mentioned member, you can specify a reason but it isn't mandatory  Usage:  !pban @member reason\n
!role   -  Gives mentioned member specified role, cannot be used for roles higher than the bot's own role(s)   Usage: !role @member role\n
!rrole  -  Removes specified role from mentioned member, cannot be used for roles higher than the bot's own role(s)  Usage: !rrole @member role\n
!emoji  -  Sends a randomized emoji from a set list of emojis 
```''')
    await ctx.send(embed=embed)


# clear command

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
    
    #if limit != int:
    #    print('discord sucks ass')
    #    await ctx.send('Please enter a number to specify the amount of messages you wish to remove!')
    #    return

    await ctx.channel.purge(limit=limit + 1)
    #await ctx.message.delete()
    await ctx.channel.send(f'Removed {limit} messages. Requested by {ctx.author.mention}.')
       



@clear.error
async def clear_error(ctx, error):
    #embed = discord.Embed( 
    #description = f'You don\'t have permission to do that!\n',
    #colour = embedColour)

    #embed.set_footer(text=embedFooterText)

    if isinstance(error, commands.MissingPermissions):
        #await ctx.send(embed=embed)
        await ctx.send(f'You don\'t have permission to do that!')


# purge command

@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx):
    await ctx.send(f'Are you 100% sure you want to remove all messages from this channel? You have 30 seconds to choose. (Yes/No)')
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
        message.content() in ['Yes', 'No']
    try:
        message = await client.wait_for('message', check=check, timeout=30)
    
        if message.content.lower() == 'yes':

            channel_position = ctx.channel.position
            channel_topic = ctx.channel.topic
            channel_permissions = ctx.channel.overwrites
            slowmode = ctx.channel.slowmode_delay

            category_name = ctx.channel.category.name
            category = discord.utils.get(ctx.guild.categories, name=category_name)
            channel_name = ctx.channel.name
            await ctx.guild.create_text_channel(f'{channel_name}', category=category, position=channel_position, topic=channel_topic, overwrites=channel_permissions, slowmode_delay=slowmode)
                
            await ctx.channel.delete()
                
            new_channel = discord.utils.get(ctx.guild.text_channels, name=f'{channel_name}')
            await new_channel.send(f'All messages have been removed from this channel. Requested by {message.author.mention}')
        else:
            await ctx.send('Purge canceled. No messages removed.')   
    
    except asyncio.TimeoutError:
        await ctx.send('Purge canceled (confirmation timer ran out). No messages removed.')
        

@purge.error
async def purge_error(ctx, error):
    embed = discord.Embed(
    description = f'You don\'t have permission to do that!\n',
    colour = embedColour)

    embed.set_footer(text=embedFooterText)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embed)


# voice channel/music commands

@client.command()
async def join(ctx):
    bot_connection = ctx.guild.voice_client
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        if bot_connection:
            await ctx.voice_client.disconnect()
            await channel.connect()
            await ctx.send(f'Connected to **{channel}**')
            print ('Connected to Voice Chat')
        else:
            await channel.connect()
            await ctx.send(f'Connected to **{channel}**')
            print ('Connected to Voice Chat')
    else:
        await ctx.send('You\'re not connected to a Voice Channel.')
    

@client.command()
async def leave(ctx):
    bot_connection = ctx.guild.voice_client
    if bot_connection:
        await ctx.voice_client.disconnect()
        await ctx.send('Disconnected from Voice Chat')
        print ('Disconnected from Voice Chat')


# moderation commands

# bad word blocker

with open('badwords.txt', 'r') as f:
    bad_words = '|'.join(s for l in f for s in l.split(', '))
    bad_word_check = re.compile(bad_words).search


@client.event
async def on_message(message):
    if bad_word_check(message.content.lower()):
        await message.delete()
        await message.channel.send(f'{message.author.mention} your message was removed because it was inappropriate')
    else:
        await client.process_commands(message)


# kick command

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *args):
    
    if member == ctx.author:
        await ctx.send(f'You can\'t kick yourself!')
        return
    
    if member.guild_permissions.kick_members:
        await ctx.send(f'You can\'t kick that person!')
        return

    reason = ''
    if args != ():
        reason = 'Reason: **'
        for i in args:
            reason = reason+' '+i
        reason = reason+'**'

    channel = await member.create_dm()
    await channel.send(f'You were kicked from **{ctx.guild.name}**. {reason}. Please consider changing your behaviour if you decide to join the server again.')

    await ctx.send(f'{member.mention} has been kicked. {reason} \n \nKicked by {ctx.author.mention}')
    
    #embed = discord.Embed( 
    #description = f'{member.mention} has been kicked. Reason: {reason} \n \n Kicked by {ctx.author.mention} \n',
    #colour = embedColour)

    #embed.set_footer(text=embedFooterText, )
    
    #await ctx.send(embed=embed)
    await member.kick(reason=reason)
    await ctx.message.delete()
    

@kick.error
async def kick_error(ctx, error):
    
    #embed = discord.Embed( 
    #description = f'You don\'t have permission to do that!\n',
    #colour = embedColour)

    #embed.set_footer(text=embedFooterText)

    if isinstance(error, commands.MissingPermissions):
        #await ctx.send(embed=embed)
        await ctx.send(f'You don\'t have permission to do that!')


# soft ban

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *args):
    
    banned_role = discord.utils.get(ctx.guild.roles, name='Banned')
    
    member_role = discord.utils.get(ctx.guild.roles, name='Member')

    if member == ctx.author:
        await ctx.send(f'You can\'t ban yourself!')
        return 

    if member.guild_permissions.ban_members:
        await ctx.send(f'You can\'t ban that person!')
        return

    reason = ''
    if args != ():
        reason = 'Reason: **'
        for i in args:
            reason = reason+' '+i
        reason = reason+'**'

    channel = await member.create_dm()
    await channel.send(f'You were banned from **{ctx.guild.name}**. {reason}. Please consider changing your behaviour to avoid this happening on other servers.')

    await ctx.send(f'{member.mention} has been banned. {reason} \n \nBanned by {ctx.author.mention}')
    
    if member_role in member.roles:
        await member.remove_roles(member_role)

    await member.add_roles(banned_role)
    await ctx.message.delete()

@ban.error
async def ban_error(ctx, error):
    
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'You don\'t have permission to do that!')


# unban for soft ban

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member):

    banned_role = discord.utils.get(ctx.guild.roles, name='Banned')

    member_role = discord.utils.get(ctx.guild.roles, name='Member')

    if member == ctx.author:
        await ctx.send(f'You can\'t unban yourself!')
        return 

    if member.guild_permissions.ban_members:
        await ctx.send(f'You can\'t unban that person!')
        return

    channel = await member.create_dm()
    await channel.send(f'You were unbanned from **{ctx.guild.name}**.')

    await ctx.send(f'{member.mention} has been unbanned. \n \n Unbanned by {ctx.author.mention}')
    
    await member.remove_roles(banned_role)
    await member.add_roles(member_role)
    await ctx.message.delete()




# permaban command

@client.command()
@commands.has_permissions(ban_members=True)
async def pban(ctx, member: discord.Member, *args, reason=None):

    if member == ctx.author:
        await ctx.send(f'You can\'t ban yourself!')
        return
    
    if member.guild_permissions.ban_members:
        await ctx.send(f'You can\'t ban that person!')
        return

    reason = ''
    if args != ():
        reason = 'Reason: **'
        for i in args:
            reason = reason+' '+i
        reason = reason+'**'

    channel = await member.create_dm()
    await channel.send(f'You were banned permanently from **{ctx.guild.name}**. {reason}. Please consider changing your behaviour to avoid this happening on other servers.')

    await ctx.send(f'{member.mention} has been permanently banned. {reason} \n \nBanned by {ctx.author.mention}')
    
    #embed = discord.Embed( 
    #description = f'{member.mention} has been banned. Reason: {reason} \n \n Banned by {ctx.author.mention} \n',
    #colour = embedColour)

    #embed.set_footer(text=embedFooterText)

    #await ctx.send(embed=embed)
    await member.ban(reason=reason)
    await ctx.message.delete()


@pban.error
async def pban_error(ctx, error):
    
    #embed = discord.Embed( 
    #description = f'You don\'t have permission to do that!\n',
    #colour = embedColour)

    #embed.set_footer(text=embedFooterText)
    
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'You don\'t have permission to do that!')
        
         #await ctx.send(embed=embed)


# role command

@client.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role):
    role = discord.utils.get(ctx.guild.roles, name=f'{role}')
    
    print(ctx.guild.me.roles)

    bot_role = discord.utils.get(ctx.guild.me.roles, name='RapakkoBot')
    print(bot_role)

    if role == None:
        await ctx.send(f'That role doesn\'t exist!')
        return

    if ctx.guild.me.top_role <= role: #or bot_role:
        await ctx.send(f'That role is above or the same as my highest role, I can\'t give that role to {member.mention}!')
        return
    
    if role in member.roles:
        await ctx.send(f'{member.mention} already has that role!')
        return

    await ctx.send(f'{ctx.author.mention} added **{role}** role to {member.mention}')
    await member.add_roles(role)
    
    
        

#@role.error
#async def role_error(ctx, error):
#    embed = discord.Embed( 
#    description = f'You don\'t have permission to do that!\n',
#    colour = embedColour)

#    embed.set_footer(text=embedFooterText)
    
#    if isinstance(error, commands.has_permissions):
#        await ctx.send(embed=embed)


# remove role command

@client.command()
@commands.has_permissions(manage_roles=True)
async def rrole(ctx, member: discord.Member, role):
    role = discord.utils.get(ctx.guild.roles, name=f'{role}')

    embed = discord.Embed( 
    description = f'{ctx.author.mention} removed {role} role from {member.mention}.\n',
    colour = embedColour)

    embed.set_footer(text=embedFooterText)

    if role == None:
        await ctx.send(f'That role doesn\'t exist!')
        return

    if ctx.guild.me.top_role <= role: #or bot_role:
        await ctx.send(f'That role is above or the same as my highest role, I can\'t give that role to {member.mention}!')
        return
    
    if not role in member.roles:
        await ctx.send(f'{member.mention} doesn\'t have that role!')
        return

    await ctx.send(f'{ctx.author.mention} removed **{role}** from {member.mention}')
    await member.remove_roles(role)


@rrole.error
async def rrole_error(ctx, error):
    embed = discord.Embed( 
    description = f'You don\'t have permission to do that!\n',
    colour = embedColour)

    embed.set_footer(text=embedFooterText)
    
    if isinstance(error, commands.has_permissions):
        await ctx.send(embed=embed)




client.run(TOKEN)
