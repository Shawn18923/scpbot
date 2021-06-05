from operator import add
from re import S
import discord
import random
from discord import activity, Member
from discord.embeds import Embed
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions, BucketType
from itertools import cycle
from asyncio import sleep
import traceback


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='scp!', intents=intents)
client.remove_command("help")
client.sniped_messages = {}
version = "1.2.1"
footer = f"Owner of the bot: something23#5495 | TCLS SCP Bot v{version}"
version_description = "+ New Command: `scp!github` | View the bot code!\n+ Fixed a issue with Changelog\n+ Misc. Changes/Fixes (Find out for what they are!)"
prev_version = "1.2.0.1"
prev_version_description="New Error Message Again | Updated another Error Message"
scp_version = "2.10.0-Beta"


async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'The Cat Lord Server', url='https://www.twitch.tv/shawncsgo2'))
        await sleep(45)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'scp! commands', url='https://www.twitch.tv/shawncsgo2'))
        await sleep(45)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'{len(client.users) - 17} users', url='https://www.twitch.tv/shawncsgo2'))
        await sleep(45)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'TCLS SCP Bot v{version}', url='https://www.twitch.tv/shawncsgo2'))
        await sleep(45)

@client.event
async def on_ready():
    print(f"TCLS SCP Bot {version} has loaded!")
client.loop.create_task(status())
    

@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)


@client.event
async def on_member_join(member):
    guild = client.get_guild(719372883889225749)
    channel = guild.get_channel(724635823227535379)
    await channel.send(f'Welcome to the Cat Lord Server! {member.mention} :partying_face:') # Welcome the member on the server
    await member.send(f'Heyo! Welcome to the Cat Lord Server {member.mention}, go to <#726605728076267651> to make sure you do not get yeeted from a game or the server, anyways have fun :D')

@client.command(aliases=['scpsc'])
async def scpversion(message):

    if message.author.id == 522888094454644737:

        server_channel = client.get_channel(828382251825496144)
        
        embed = discord.Embed(title="Current Version of SCP:SL Server", description="v10.2.2 SCP | v2.10.0 EXILED", color=0x00ff00)
        embed.add_field(name="Release Date of the Server (Revised)", value="May 27th, 2021", inline=False)
        embed.add_field(name="Changes", value='Moved to EXILED Hosting ($10/mnth)')
        embed.set_footer(text=f"{footer}")

        await server_channel.send(embed=embed)

    elif message.author.id != 522888094454644737:
        await message.channel.send(f'<#828382251825496144> | You cannot use this command {message.author.mention}!')



##Important Stuff



@client.command(aliases=['bv', 'botv'])
@commands.cooldown(1,15,commands.BucketType.user)
async def botversion(ctx):

    embed = discord.Embed(title=f"Version {version} of the TCLS SCP Bot", color=0x00ff00)
    embed.add_field(name='Changes', value=f"{version_description}", inline=False)
    embed.add_field(name='Time of Release', value='June 5th, 2021')
    embed.add_field(name='Any more?', value='Use `scp!pv` for the previous version or `scp!cl`')
    embed.set_footer(text=f"{footer}")

    await ctx.author.send(embed=embed)
    await ctx.send(f'Sent to your DMs {ctx.author.mention}! | A ***15 Second*** Cooldown has been applied to this Command')

@client.command(aliases=['git'])
@commands.cooldown(1,10,commands.BucketType.user)
async def github(ctx):

    embed = discord.Embed(title=f'Github Resporitory!', color=0x00ff00)
    embed.add_field(name='Link to', value='https://github.com/Shawn18923/scpbot')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@client.group(invoke_without_command=True, aliases=['changelog'])
async def cl(ctx):

    embed = discord.Embed(title=f"Changelog of the TCLS SCP Bot | `scp!changelog <version>`", color=0x00ff00)

    embed.add_field(name='Pastebin', value='https://pastebin.com/af71umcc (Use this to view the changelog in itself on a file)', inline=False)
    embed.add_field(name='Versions to view!', value='`1.2.1`\n`1.2.0.1`\n`1.2`\n`1.1.6.1`\n`1.1.6`\n***VERSIONS BELOW THIS TEXT ARE NOT ABLE TO GIVE A RELEASE DATE***\n`1.1.5`\n`1.1.4`\n`1.1.3`\n`1.1.2`', inline=False)
    embed.add_field(name='Time of Release?', value=f'Only Available from v1.1.6 to v{version}')

    await ctx.send(embed=embed)

@client.command(aliases=['pbv', 'pbotversion'])
@commands.cooldown(1,15,commands.BucketType.user)
async def pv(ctx):

    embed = discord.Embed(title=f"Previous Version ({prev_version}) of the TCLS SCP Bot", color=0x00ff00)
    embed.add_field(name='Changes', value=f'{prev_version_description}', inline=False)
    embed.add_field(name='Time of Release', value='June 5th, 2021')
    embed.set_footer(text=f"{footer}")

    await ctx.author.send(embed=embed)
    await ctx.send(f'Sent to your DMs {ctx.author.mention}! A ***15 Second*** Cooldown has been applied to this Command')


@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def server(ctx):

    embed = discord.Embed(title='Server for SCP:SL and Discord', color=0x00ff00)
    embed.add_field(name='Discord Server', value='https://discord.gg/ZMhjkBS is a permanent invite link to the server :smile:', inline=False)
    embed.add_field(name='SCP Server', value='The Cat Lord Server', inline=False)
    embed.add_field(name='SCP:SL EXILED Version', value=f'{scp_version}')
    embed.set_footer(text=f"{footer}")

    await ctx.author.send(embed=embed)
    await ctx.send(f'Sent to your DMs {ctx.author.mention}! | A ***15 Second*** Cooldown has been applied to this Command')

@client.command(aliases=['rp', 'rperms', 'rolepermissions'])
@commands.cooldown(1,15,commands.BucketType.user)
async def roleperms(ctx):
    embed = discord.Embed(title='Permissions for basic actions based on roles (and above roles)', color=0x00ff00)
    embed.add_field(name='Administrator, Manage Server, Manage Roles, Mention Everyone', value=f'<@&724633627463254128>', inline=False)
    embed.add_field(name='Priority Speaker', value=f'<@&724633223086211122> and <@&724633627463254128>', inline=False)
    embed.add_field(name='Ban Members', value=f'<@&734257831594688583> and above', inline=False)
    embed.add_field(name='Manage Webhooks, Manage Channels', value=f'<@&734259465137946675> and above', inline=False)
    embed.add_field(name='Kick Members', value=f'<@&744619191436574760> and above', inline=False)
    embed.add_field(name='Manage Emojis', value=f'<@&744618701587873912> and above', inline=False)
    embed.add_field(name='Speaking Perms (Text, Voice)', value=f'<@&719372883889225749> except <@&726589070750384198>', inline=False)
    embed.add_field(name='Able to see, no speak', value='<@&726589070750384198>')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@client.command(aliases=['rule'])
@commands.cooldown(1,15,commands.BucketType.user)
async def rules(ctx):
    embed = discord.Embed(title='Information on the rules in Discord and SCP:SL Server(s)', color=0x00ff00)
    embed.add_field(name='Discord-SCP:SL Rules', value=f'<#726605728076267651>', inline=False)
    embed.add_field(name='Discord TOS', value='https://discord.com/terms')
    embed.add_field(name='Punishments | Discord-SCP:SL ***SERVER*** Rules', value='They are given in the rules themselves, read them lol', inline=False)
    embed.add_field(name='Punishments | Discord TOS', value='Ban from all servers (If applicable for SCP:SL) and a report to the Discord T&S Team')
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

#Moderation Commands

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason != None:

        await member.kick(reason=reason)

        embed = discord.Embed(title='Member has been Kicked!', color=0x00ff00)
        embed.add_field(name='Member Kicked', value=f'{member.name}')
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        embed.add_field(name='The Yeeter', value=f'{ctx.author.mention}')
        embed.set_footer(text=f"{footer}")
    else:
        await member.kick(reason=reason)

        embed = discord.Embed(title='Member has been Kicked!', color=0x00ff00)
        embed.add_field(name='Member Kicked', value=f'{member.name}')
        embed.add_field(name='Reason', value=f'No Reason', inline=False)
        embed.add_field(name='The Yeeter', value=f'{ctx.author.mention}')
        embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason != None:

        await member.ban(reason=reason)

        embed = discord.Embed(title='Member has been Banned!', color=0x00ff00)
        embed.add_field(name='Member Banned', value=f'{member.name}')
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        embed.add_field(name='The Banisher', value=f'{ctx.author.mention}')
        embed.set_footer(text=f"{footer}")
    else:
        await member.ban(reason=reason)

        embed = discord.Embed(title='Member has been Banned!', color=0x00ff00)
        embed.add_field(name='Member Banned', value=f'{member.name}')
        embed.add_field(name='Reason', value=f'No Reason', inline=False)
        embed.add_field(name='The Banisher', value=f'{ctx.author.mention}')
        embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

##Fun Commands

@client.command(pass_context = True, aliases=['rn', 'RN'])
@commands.cooldown(1,12,commands.BucketType.user)
async def randomnumber(ctx):

    embed = discord.Embed(title = "Random Number", description = (random.randint(1, 1000)), color = (0x00ff00))
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1,30,commands.BucketType.user)
async def shawn(ctx):


    embed = discord.Embed(title = "Shawn", description = "The mother fucker that created the SCP:SL part of the server", color = 0x00ff00)
    embed.add_field(name='`Discord`', value=f'something23#5495 | <@522888094454644737>', inline=False)
    embed.add_field(name='`Social Medias`', value='@dank1892 (Snapchat)', inline=False)
    embed.add_field(name='`IRL Info`', value=f"9th Grader | 13 Year Old | `7/23/2007` Birthday", inline=False)
    embed.set_footer(text=f"{footer}")

    await ctx.author.send(embed=embed)
    await ctx.send(f'Sent to your DMs {ctx.author.mention}! | A ***30 Second*** Cooldown has been applied to this Command')

@client.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.channel.send('Sorry but I could not find a message to snipe LOL')
        return

    embed = discord.Embed(description=contents, color=0x00ff00, timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name} | TCLS SCP Bot v{version}")

    await ctx.channel.send(embed=embed)

@client.command(aliases=['8ball', '8b'])
async def eightball(ctx, *, question):
    responses = [
        'Hell no. :x:',
        'Prolly not. :x:',
        'Idk bro. :thinking:',
        'Prolly. :man_shrugging:',
        'Hell yeah my dude. :white_check_mark:',
        'It is certain. :white_check_mark:',
        'It is decidedly so. :white_check_mark:',
        'Without a Doubt. :white_check_mark:',
        'Yes - Definitaly. :white_check_mark:',
        'You may rely on it. :white_check_mark:',
        'As i see it, Yes. :white_check_mark:',
        'Most Likely. :white_check_mark:',
        'Outlook Good. :white_check_mark:',
        'Yes! :white_check_mark:',
        'No! :x:',
        'Signs a point to Yes! :white_check_mark:',
        'Reply Hazy, Try again. :man_shrugging:',
        'Better not tell you know. :thinking:',
        'Cannot predict now. :thinking',
        'Concentrate and ask again. :man_shrugging:',
        "Don't Count on it. :x:",
        'My reply is No. :x:',
        'My sources say No. :x:',
        'Outlook not so good. :x:',
        'Very Doubtful :x:']
    embed = discord.Embed(title="8ball!", description=f'Question: "{question}"', color=0x00ff00)
    embed.add_field(name="Answer", value=f'{random.choice(responses)}')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)


## Help Section

@client.group(invoke_without_command=True)
@commands.cooldown(1,5,commands.BucketType.user)
async def help(ctx):

    server = discord.Embed(title="Help | Serious/Server Commands", description="Command Names/Info | `scp!help <command>`", color=0x00ff00)
    server.add_field(name='`botversion`', value=f'Gives the Version of the Bot without having to go the relevant channel', inline=False)
    server.add_field(name='`pv`', value=f'Gives information on the version BEFORE v{version}', inline=False)
    server.add_field(name='`server`', value='Shows Info about and for the Discord and SCP:SL Servers', inline=False)
    server.add_field(name='`kick`', value=f'Yeet a motherfucker! | Only available with the <@&744619191436574760> and above')
    server.add_field(name='`ban`', value=f'Banish a motherfucker! | Only available with the <@&734257831594688583> role and above', inline=False)
    server.add_field(name='`changelog`', value=f'View the bot changelog between v1.1.2 - v{version}', inline=False)
    server.add_field(name='`roleperms`', value=f'Shows Permissions (or a broader range of permissions) for specific roles', inline=False)
    server.add_field(name='`rules`', value=f'Shows Information on the rules of both Discord itself, and the Discord and SCP:SL __Servers__', inline=False)
    server.add_field(name='`github`', value=f'Gives the Github Resporitory on where it is also changed along with the bot!')

    fun = discord.Embed(title="Help | Random Commands", description="Commands that are not helpful but slightly fun for the bot!", color=0x00ff00)
    fun.add_field(name='`randomnumber`', value=f'Random Number Generator without Google!', inline=False)
    fun.add_field(name='`snipe`', value='Snipes the most recent message that was deleted in the server', inline=False)
    fun.add_field(name='`shawn`', value=f'Shows info about <@522888094454644737>', inline=False)
    fun.add_field(name='`8ball`', value='Ask Questions, get Answers!')
    fun.set_footer(text=f"{footer}")

    await ctx.send(embed=server)
    await ctx.send(embed=fun)

@help.command(aliases=['botv', 'bv'])
async def botversion(ctx):

    embed = discord.Embed(title='Command: `botversion`', description="Shows the Version of the Bot!", color=0x00ff00)

    embed.add_field(name='Use', value='`scp!botversion`', inline=False)
    embed.add_field(name='Aliases', value='`botv`, `bv`', inline=False)
    embed.add_field(name='Cooldown', value='15 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command(aliases=['git'])
async def github(ctx):

    embed = discord.Embed(title='Command `github`', description='Gives the Github Resporitory on where it is also changed along with the bot!', color=0x00ff00)
    
    embed.add_field(name='Use', value='`scp!github`', inline=False)
    embed.add_field(name='Aliases', value='`git`', inline=False)
    embed.add_field(name='Cooldown', value='10 Seconds')
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@help.command(aliases=['cl'])
async def changelog(ctx):

    embed = discord.Embed(title='Command: `changelog`', description=f'Shows the Changelog between v{version} - v1.1.2', color=0x00ff00)
    
    embed.add_field(name='Use', value='`scp!changelog`', inline=False)
    embed.add_field(name='Aliases', value='`cl`', inline=False)
    embed.add_field(name='Cooldown', value='15 Seconds')
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@help.command(aliases=['pbv', 'pbotversion'])
async def pv(ctx):
    
    embed = discord.Embed(title='Command: `pv`', description=f"Shows the Previous Version Changelog before v{version}", color=0x00ff00)
    
    embed.add_field(name='Use', value='`scp!pv`', inline=False)
    embed.add_field(name='Aliases', value='`pbv`, `pbotversion`', inline=False)
    embed.add_field(name='Cooldown', value='15 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command()
async def server(ctx):

    embed = discord.Embed(title='Command: `server`', description='Shows information of both the SCP and Discord Servers!', color=0x00ff00)

    embed.add_field(name='Use', value='`scp!server`', inline=False)
    embed.add_field(name='Cooldown', value='15 Seconds', inline=False)
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@help.command(aliases=['rp', 'rperms', 'rolepermissions'])
async def roleperms(ctx):

    embed = discord.Embed(title='Command: `roleperms`', description='Shows Permissions for specific (or broader ranges of) roles', color=0x00ff00)
    
    embed.add_field(name='Use', value='`scp!roleperms`', inline=False)
    embed.add_field(name='Aliases', value='`rp`, `rperms`, `rolepermissions`', inline=False)
    embed.add_field(name='Cooldown', value='15 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command(aliases=['rule'])
async def rules(ctx):

    embed = discord.Embed(title='Command: `rules`', description='Shows Information on both the Servers of Discord and SCP:SL, and the Discord TOS itself', color=0x00ff00)
    
    embed.add_field(name='Use', value='`scp!rules`', inline=False)
    embed.add_field(name='Aliases', value='`rule`', inline=False)
    embed.add_field(name='Cooldown', value='15 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command(aliases=['rn', 'RN'])
async def randomnumber(ctx):
    
    embed = discord.Embed(title='Command: `randomnumber`', description='Gives a literal random number from a range of 1-101', color=0x00ff00)
    
    embed.add_field(name='Use', value='`scp!randomnumber`', inline=False)
    embed.add_field(name='Aliases', value='`rn`, `RN`', inline=False)
    embed.add_field(name='Cooldown', value='Cooldown: 12 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command()
async def shawn(ctx):

    embed = discord.Embed(title='Command: `shawn`', description='Gives information on Shawn, the creator of the bot', color=0x00ff00)

    embed.add_field(name='Use', value='`scp!shawn`', inline=False)
    embed.add_field(name='Cooldown', value='30 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command()
async def snipe(ctx):

    embed = discord.Embed(title='Command: `snipe`', description='Snipes the most recently deleted message', color=0x00ff00)
    
    embed.add_field(name='Use', value='`scp!snipe`', inline=False)
    embed.add_field(name='Cooldown', value='10 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command()
async def kick(ctx):

    embed = discord.Embed(title='Command: `kick`', description='Yeet a motherfucker!', color=0x00ff00)

    embed.add_field(name='Use', value='`scp!kick @[user] [reason]` (Reason is not required)')
    embed.add_field(name='Role/Perms Needed', value='Role: <@&744619191436574760> | Perms: Kick Members')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command()
async def ban(ctx):

    embed = discord.Embed(title='Command: `ban`', description='Banish a motherfucker!', color=0x00ff00)

    embed.add_field(name='Use', value='`scp!ban @[user] [reason]` (Reason is not required)')
    embed.add_field(name='Role/Perms Needed', value='Role: <@&734257831594688583> | Perms: Ban Members')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

@help.command(aliases=['8ball', '8b'])
async def eightball(ctx):

    embed = discord.Embed(title='Command: `8ball`', description='Ask a Question, get an Answer!', color=0x00ff00)

    embed.add_field(name='Use', value='`scp!8ball [text]`', inline=False)
    embed.add_field(name='Aliases', value='`8b`, `eightball`, `eightball``', inline=False)
    embed.add_field(name='Cooldown', value='10 Seconds')
    embed.set_footer(text=f"{footer}")

    await ctx.send(embed=embed)

## Changelog

@cl.command(aliases=['1.2.1'])
async def _121(ctx):

    embed = discord.Embed(title='Version `1.2.1` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='June 5th, 2021', inline=False)
    embed.add_field(name='Changes', value='+ New Command: `scp!github` | View the bot code!\n+ Fixed a issue with Changelog\n+ Misc. Changes/Fixes (Find out for what they are!)')
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@cl.command(aliases=['1.2.0.1'])
async def _1201(ctx):

    embed = discord.Embed(title='Version `1.2.0.1` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='June 5th, 2021', inline=False)
    embed.add_field(name='Changes', value='New Error Message Again | Updated another Error Message')
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@cl.command(aliases=['1.2'])
async def _12(ctx):

    embed = discord.Embed(title='Version `1.2` Changelog', color=0x00ff00)

    embed.add_field(name='Time of Release/ToR', value='June 4th, 2021', inline=False)
    embed.add_field(name='Changes', value='+ New Command: `scp!rules`\n+ Updated the Help Command with more relevant info | Also added `scp!rules` to it\n+ Updated Changelog with a serious overhaul to it!\n+ Updated `scp!shawn` with more information!\n+ New Error Message | Updated the `Missing Permissions` Error')
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@cl.command(aliases=['1.1.6.1'])
async def _1161(ctx):

    embed = discord.Embed(title='Version `1.1.6.1` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='June 1st, 2021', inline=False)
    embed.add_field(name='Changes', value='Cooldown for the Help Command, and the subcommands have went to 5 seconds, up from 2 (This is to not overload the bot, nor spam)')
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@cl.command(aliases=['1.1.6'])
async def _116(ctx):

    embed = discord.Embed(title='Version `1.1.6` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='June 1st, 2021', inline=False)
    embed.add_field(name='Changes', value=f"+ New Command: `scp!changelog` | Gives the changelog of the bot from v1.1.2 to {version} (Ironic considering you're using it!)")
    embed.set_footer(text=f'{footer}')

    await ctx.send(embed=embed)

@cl.command(aliases=['1.1.5'])
async def _115(ctx):

    embed = discord.Embed(title='Version `1.1.5` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='N/A | Unknown', inline=False)
    embed.add_field(name='Changes', value='+ The Help Command is now sent in the channel the command was invoked from')
    embed.set_footer(text=f'{footer}')
    
    await ctx.send(embed=embed)

@cl.command(aliases=['1.1.4'])
async def _114(ctx):

    embed = discord.Embed(title='Version `1.1.4` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='N/A | Unknown', inline=False)
    embed.add_field(name='Changes', value='+ Updated 8ball responses with emojis of what it indicates')
    embed.set_footer(text=f'{footer}')
    
    await ctx.send(embed=embed)

@cl.command(aliases=['1.1.3'])
async def _113(ctx):

    embed = discord.Embed(title='Version `1.1.3` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='N/A | Unknown', inline=False)
    embed.add_field(name='Changes', value='+ New command: `scp!pv` | Gives the previous version of the bot!')
    embed.set_footer(text=f'{footer}')
    
    await ctx.send(embed=embed)

@cl.command(aliases=['1.1.2'])
async def _112(ctx):

    embed = discord.Embed(title='Version `1.1.2` Changelog', color=0x00ff00)
    
    embed.add_field(name='Time of Release/ToR', value='N/A | Unknown', inline=False)
    embed.add_field(name='Changes', value='+ New command: `scp!8ball`\n+ `scp!botversion` has been changed for use from everyone!\n+ `scp!server` has been updated slightly')
    embed.set_footer(text=f'{footer}')
    
    await ctx.send(embed=embed)


##Errors

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): #checks if on cooldown

        embed = discord.Embed(title='Error: Cooldown', color=0xff0000)
        embed.add_field(name="Oops! Seems you weren't patient!", value='The command **{}** is still on cooldown for {:.2f} seconds lol'.format(ctx.command.name, error.retry_after))
        embed.set_footer(text=f"{footer}")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):

        embed = discord.Embed(title='Error: Missing Required Argument(s)', color=0xff0000)
        embed.add_field(name='Oops!', value='It seems you did not pass the required amount of arguments for the command: "**{}**". Try again'.format(ctx.command.name))
        embed.set_footer(text=f"{footer}")

        await ctx.send(embed=embed)
    
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(title='Error: Invalid Argument(s)', color=0xff0000)
        embed.add_field(name='Oops!', value='You fucked up! The arguments given are bad/invalid for the command "**{}**". Try again'.format(ctx.command.name))
        embed.set_footer(text=f"{footer}")

    elif isinstance(error, commands.CommandNotFound):

        embed = discord.Embed(title='Error: No Command Exists!', color=0xff0000)
        embed.add_field(name='Oops!', value="It seems you tried to use a command that didn't exist! Refer to the `scp!help` command for what does exist!")
        embed.set_footer(text=f'{footer}')

        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):

        embed = discord.Embed(title='Error: Permissions', color=0xff0000)
        embed.add_field(name=f"Oops! Seems you aren't powerful enough! ({ctx.author})", value='You do not have the permissions to use the **{}** command!'.format(ctx.command.name), inline=False)
        embed.add_field(name=f"What Permissions do I need?", value='Do `scp!help {}` to see! | Also you can do `scp!roleperms`'.format(ctx.command.name))
        embed.set_footer(text=f"{footer}")
        await ctx.send(embed=embed)

client.run('[PUT YOUR TOKEN HERE]')
