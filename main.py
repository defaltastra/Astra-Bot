
import discord, datetime, time, asyncio, os, json, random, requests, aiohttp , io, sys
import colorama
from discord.ext import commands
from datetime import datetime
from discord import Member
from random import choice
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, Back, Style
from discord.ext.commands import has_permissions, CheckFailure
from datetime import datetime
from requests import get
import json
import subprocess





determine_flip = [1, 0]
bot = commands.Bot(command_prefix='.', case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    version = "1.0"
    print(f'''{Fore.RESET}{Fore.CYAN}


·▄▄▄▄•      ·▄▄▄▄  ▪   ▄▄▄· ▄ •▄ 
▪▀·.█▌▪     ██▪ ██ ██ ▐█ ▀█ █▌▄▌▪
▄█▀▀▀• ▄█▀▄ ▐█· ▐█▌▐█·▄█▀▀█ ▐▀▀▄·
█▌▪▄█▀▐█▌.▐▌██. ██ ▐█▌▐█ ▪▐▌▐█.█▌
·▀▀▀ • ▀█▄▀▪▀▀▀▀▀• ▀▀▀ ▀  ▀ ·▀  ▀


{Fore.BLUE}Logged in as | {Fore.CYAN}{bot.user.name}#{bot.user.discriminator}
{Fore.BLUE} Prefix | {Fore.CYAN}{prefix}
{Fore.BLUE}Version| {Fore.CYAN}{version}
{Fore.BLUE}Made by Zodiak
  
    '''+Fore.RESET)


    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep"))


@bot.command()
async def serverpfp(ctx):
    embed = discord.Embed(title=ctx.guild.name)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
        embed = discord.Embed(title=f"Pong {bot.latency}ms latency")
        await ctx.send(embed=embed)


@bot.command()
async def logout(ctx):
  if ctx.author.id == 208650005731475456:
    await ctx.send('Logging out')
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)
    await ctx.message.delete()
    return
  else:
    await ctx.send(f"{ctx.message.author.mention} you are not the owner so you cant logout of the bot")

@bot.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)






@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    mention = []
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Nickname:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def version(ctx):
        version = "1.0"
        embed = discord.Embed(title="Version | Zodiak's Bot :D ", description=f"{ctx.author.mention} Im on version {version}")
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def getpfp(ctx, member: Member = None):
 if not member:
  member = ctx.author
 await ctx.send(member.avatar_url)

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")







@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=True
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.send(embed=help_embed)

@bot.command(pass_context=True)
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip | Zodiak's bot :D ", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip | Zodiak's bot :D ", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
        await ctx.send(embed=embed)

@bot.command()
async def ip(ctx, ip: str=None):
    if ip is None: await ctx.send("Please sepcify an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("Invalid IP address")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(color=0xff4301, title=f"ip info",timestamp=datetime.utcfromtimestamp(time.time()))
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.set_footer(text=f"Requested by {ctx.author} || HONK  ||Zodiak")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")



@bot.command()
async def serverinfo(ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f'{guild} Info', description="Coded by Zodiak",
                          timestamp=ctx.message.created_at, color=discord.Color.red())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Number of channels:", value=len(guild.channels))
        embed.add_field(name="Number of roles:", value=len(guild.roles))
        embed.add_field(name="Number of boosters:", value=guild.premium_subscription_count)
        embed.add_field(name="Number of users:", value=guild.member_count)
        embed.add_field(name="Date created:", value=guild.created_at)
        embed.add_field(name="Server owner:", value=guild.owner)
        embed.set_footer(text=f"{ctx.author} used serverinfo command.", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def bonk(ctx):
    
    await ctx.send("https://tenor.com/view/bonk-meme-dog-doge-gif-14889944")

@bot.command(pass_context=True)
async def niggus(ctx):
    await ctx.send("https://tenor.com/view/miller-grove-meme-lol-black-kid-kid-gif-19310057")
@bot.command(pass_context=True)
async def niggusthink(ctx):
    await ctx.send("https://tenor.com/view/black-kid-focus-thinking-at-work-hmm-gif-16917389")





bot.run(TOKEN)
