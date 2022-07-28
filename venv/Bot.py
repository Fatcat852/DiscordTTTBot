import discord
from discord.ext import commands

client = commands.Bot(command_prefix='&')
token = 'Nzk4NzYzMzY3NTg5NDc4NDAw.X_5wWw.8gIn1UQV7dTmKmWN0Qn-GhATgm0'
emoji_yes = ':white_check_mark:'
emoji_no = ':x:'
react_emoji_yes_no = [emoji_yes, emoji_no]


#Board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
one = ":one:"
two = ":two:"
three = ":three:"
four = ":four:"
five = ":five:"
six = ":six:"
seven = ":seven:"
eight = ":eight:"
nine = ":nine:"
game_board = discord.Embed(title="Tic Tac Toe", color=0x00f00)
game_board.add_field(name="  " + board[0] + "  ", value="__")
game_board.add_field(name="  " + board[1] + "  ", value="__")
game_board.add_field(name="  " + board[2] + "  ", value="__")
game_board.add_field(name="  " + board[3] + "  ", value="__")
game_board.add_field(name="  " + board[4] + "  ", value="__")
game_board.add_field(name="  " + board[5] + "  ", value="__")
game_board.add_field(name="  " + board[6] + "  ", value="__")
game_board.add_field(name="  " + board[7] + "  ", value="__")
game_board.add_field(name="  " + board[8] + "  ", value="__")

# players
#player_1 = yes_play.author
#player_2 = play_react.author
#current_player = player_1
#symbol = "X"

# Bot is online
@client.event
async def on_ready():
    print("TTT Bot is ready.")
    print("We have logged on as {0.user}".format(client))

    bot_channel = client.get_channel(798776632722456586)
    await bot_channel.send('Hello! Type &start to start game')

# Introductions of the bot
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command(name='start')
async def start(message):
    response = await message.channel.send('Would you like to play Tic Tac Toe?')
    channel = message.channel
    await response.add_reaction(emoji_yes)
    await response.add_reaction(emoji_no)

    def check(reaction, user):
            return user == message.author and str(reaction.emoji) == emoji_yes

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await channel.send(':thumbdown:')
    else:
        await channel.send(':thumbup:')


@client.command(name='TTT')
async def play_game():
    await context.channel.send(embed = game_board)
    statement = await context.channel.send("Choose a position from 1-9.")
    await statement.add_reaction(one)
    await statement.add_reaction(two)
    await statement.add_reaction(three)
    await statement.add_reaction(four)
    await statement.add_reaction(five)
    await statement.add_reaction(six)
    await statement.add_reaction(seven)
    await statement.add_reaction(eight)
    await statement.add_reaction(nine)

@client.event
async def on_raw_reaction_add(payload):
    await client.channel.send(payload)
    message = client.get_user(payload.message_id)
    channel = client.get_channel(payload.channel_id)
    position = str(payload.emoji)
    player_1 = payload.user_id
    await client.channel.send('you are' + player_1)
    await client.channel.send('selected position is' + position)


client.run(token)
