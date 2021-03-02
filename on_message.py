import sys

async def receive_message(message):
    """
    Handles all our logic when we receive a message.

    :param message: discord.message class
    """

        if message.author == client.user:  # check if it is me( bot ) messaging
            return
        # await message.channel.send(message.channel)   #   good for getting var values of datatypes

        if str(message.author.id) == testingUser_id:  # make testingUser
            if message.content == "state":
                await message.channel.send("functional")

            if message.content == "stop":
                await client.get_channel(bot_channel_id).send(
                    """__***BOT SHUTTING DOWN***__""")
                sys.exit()
            
        if message.content == "!help":
                
                
                

    

    

