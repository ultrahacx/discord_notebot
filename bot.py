import discord
from discord.ext import commands
import os
from os import path
client = commands.Bot(command_prefix='!')
notename = 'name.txt'
notedetail = 'list.txt'
client.remove_command('help')



@client.event
async def on_ready():
    print("Bot is ready!!!")

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def shownote(ctx, args1):
    if path.exists(notename) == True and path.exists(notedetail) == True:
        print("Both files present....")
        notfound = None
        fh = open(notename)
        for index, line in enumerate(fh):
            line = line.strip()
            if args1 in line:
                print("yes")
                print("index: ", index)
                ff = open(notedetail)
                lines = ff.readlines()
                await ctx.send("{} ".format(ctx.message.author.mention) + " " + lines[index])
                notfound = 1
        if notfound != 1:
           await ctx.send("No such note found")
        else:
            print()
    else:
        print("One of either file not found")
        await ctx.send("Notes database is either corrupted or the files are missing")

@client.command(pass_context=True)
async def showlist(ctx):
    if path.exists(notename) == True:
        fh = open(notename)
        embed = discord.Embed(
            color=discord.Color.green(),
            description="These are the following notes present in my DB :books:"
        )
        author = ctx.message.author
        embed.set_author(name="Notes List")
        for index, line in enumerate(fh):
            line = line.strip()
            embed.add_field(name = "\u200b", value="- {}".format(line), inline=False)
        await ctx.send(author.mention, embed=embed)
    else:
       await ctx.send("No notes database found :books:")





@client.command(pass_context=True)
@commands.has_any_role('Admin', 'Moderator', 'Super Admin')
async def addnote(ctx, args1, *,message):
    if path.exists(notename) == True and path.exists(notedetail) == True:
        print("DB Present... Adding note")
        name = open(notename, "a")
        name.write(args1 +  "\n")
        name.close()
        detail = open(notedetail, "a")
        detail.write(message + "\n")
        detail.close()
        print("Added note to the database")
        await ctx.send("Note added successfully :white_check_mark:")
    else:
        await ctx.send("No notes database found... Making new database")
        open('name.txt', 'a').close()
        open('list.txt', 'a').close()
        print("DB Present... Adding note")
        name = open(notename, "a")
        name.write(args1 +  "\n")
        name.close()
        detail = open(notedetail, "a")
        detail.write(message + "\n")
        detail.close()
        print("Added note to the database")
        await ctx.send("Note added successfully :white_check_mark:")


@client.command(pass_context=True)
@commands.has_any_role('Admin', 'Moderator', 'Super Admin')
async def deletenote(ctx, args1):
    if path.exists(notename) == True and path.exists(notedetail) == True:
        is_skipped = False
        dummy_file = notename + '.bak'
        c = 0
        # Open original file in read only mode and dummy file in write mode
        with open(notename, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            # Line by line copy data from original file to dummy file
            for line in read_obj:
                line_to_match = line
                if line[-1] == '\n':
                    line_to_match = line[:-1]
                # if current line matches with the given line then skip that line
                if line_to_match != args1:
                    write_obj.write(line)
                    c = c + 1
                else:
                    is_skipped = True

        # If any line is skipped then rename dummy file as original file
        if is_skipped:
            os.remove(notename)
            os.rename(dummy_file, notename)
            print("New file renamed")
            print("Line no deleted is: ", c)

        else:
            os.remove(dummy_file)
            print("File not renamed")

        is_skipped_det = False
        current_index = 0
        dummy_file = notedetail + '.bak'
        # Open original file in read only mode and dummy file in write mode
        with open(notedetail, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            # Line by line copy data from original file to dummy file
            for line in read_obj:
                # If current line number matches the given line number then skip copying
                if current_index != (c - 1):
                    write_obj.write(line)
                else:
                    is_skipped_det = True
                current_index += 1

            # If any line is skipped then rename dummy file as original file
        if is_skipped_det:
            os.remove(notedetail)
            os.rename(dummy_file, notedetail)
            print("DEleted detail line: ", (current_index - 1))
            await ctx.send("Note deleted successfully")
        else:
            os.remove(dummy_file)
            print("Not DEleted detial")
            await ctx.send("Unable to deleted note")



@client.command(pass_context=True)
@commands.has_any_role('Admin', 'Moderator', 'Super Admin')
async def deletedb(ctx):
    if path.exists(notename) == True and path.exists(notedetail) == True:
        os.remove(notedetail)
        os.remove(notename)
        print("DB Deleted Successfully")
        await ctx.send("Database deleted successfully :books: :white_check_mark:")
    else:
        print("DB not found...")
        await ctx.send("Database not found :red_circle: :books:")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        color= discord.Color.green(),
        description= "Hello there! I am AndroNix NoteBot. I was made my AndroNix developer. I am only here to keep note of things"
    )
    embed.set_author(name="HELP ")
    embed.add_field(name="!help", value="Gives list of what I can do",
                    inline=False)
    embed.add_field(name="!showlist", value="Shows the list of available notes in my database :books:", inline=False)
    embed.add_field(name="!shownote {notename} ", value="Use this command and replace ***{notename}*** with any name given in the notes list", inline=False)
    embed.add_field(name="!addnote {note title} {note details}", value="Use this command to add note in database (Can only be used by higher authorities)", inline=False)
    embed.add_field(name="!deletenote {notename}", value="Use this to delete any single note (Can only be used by higher authorities)", inline=False)
    embed.add_field(name="!deletedb", value="Use this to delete full database (Can only be used by higher authorities)", inline=False)
    await ctx.send(embed=embed)

client.run('NjgyNjQxMzM3MjUzNjI2MDAw.Xlf9Ww.jjzvchkYbstWHXkN3lH8Fc6OiR8')