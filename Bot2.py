import discord
from discord.ext import commands

# Initial Variables
client = commands.Bot(command_prefix='&')
token = 'Nzk4NzYzMzY3NTg5NDc4NDAw.X_5wWw.8gIn1UQV7dTmKmWN0Qn-GhATgm0'
bot_channel = client.get_channel(798776632722456586)

# Game board data
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

# Initializing the client bot
@client.event
async def on_ready():
    print("TTT Bot is ready.")
    print("We have logged on as {0.user}".format(client))

    bot_channel = client.get_channel(798776632722456586)
    await bot_channel.send('Hello! Send &start to start game')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command(name='start')
async def start(message):
    channel = message.channel
    response = await channel.send('Would you like to play Tic Tac Toe?')
    emoji_yes = ':white_check_mark:859795400528625675'
    emoji_no = ':x:859795356287107125'
    await response.add_reaction(emoji_yes)
    await response.add_reaction(emoji_no)

    def check_reaction(reaction, user):
        return user == message.author and str(reaction.emoji) == emoji_yes

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0,
                                                check=check_reaction)
    except asyncio.TimeoutError:
        await channel.send("It looks like you don't want to play :(")
    else:
        await channel.send('Who would you like to play with?')
        # find someone to play

        client.play_game(user, user)

#shortcut to playing the game
@client.command(name='TTT')
async def start_game(message):
    client.play_game(user, user)

@client.event
async def on_raw_reaction_add(payload):
    await client.channel.send(payload)
    message = client.get_user(payload.message_id)
    channel = client.get_channel(payload.channel_id)
    position = str(payload.emoji)
    player_1 = payload.user_id
    await client.channel.send('you are' + player_1)
    await client.channel.send('selected position is' + position)

@client.command()
async def play_game(player1, player2, channel=bot_channel):
    await channel.send(embed = game_board)
    statement = await channel.send("Choose a position from 1-9.")
    await statement.add_reaction(one)
    await statement.add_reaction(two)
    await statement.add_reaction(three)
    await statement.add_reaction(four)
    await statement.add_reaction(five)
    await statement.add_reaction(six)
    await statement.add_reaction(seven)
    await statement.add_reaction(eight)
    await statement.add_reaction(nine)


client.run(token)
