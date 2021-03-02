import sys



noxUser_id = 183478921864413184
celeryUser_id = 171178377976348674
willingToHelp_id = 813923775548489809

mechanics = [
    'nox#4756',
    'celery#9490'
]

async def receive_message(client, message):
    """
    Handles all our logic when we receive a message.

    :param client: Our discord client (discord.client)
    :param message: discord.message class
    """

    if message.author == client.user:  # check if it is me( bot ) messaging
            return
        # await message.channel.send(message.channel)   #   good for getting var values of datatypes

    if str(message.author) in mechanics:  # make testingUser
        if message.content == "state":
            await message.channel.send("functional")

        if message.content == "stop":
            await client.get_channel(bot_channel_id).send(
                """__***BOT SHUTTING DOWN***__""")
            sys.exit()
        
        if message.content == "!help":
            # Fetch server members with role 'helper'
            helpers = message.guild.get_role(willingToHelp_id).members
            #   Print users (to console)
            
            # If status == online or idle
            goodHelpers = []
            for helper in helpers:
                if helper.raw_status == "online" or helper.raw_status == "idle":
                    print(helper.display_name + "\n")
                    goodHelpers.append(helper)

            await message.channel.send(f'{len(goodHelpers)} people have been pinged')
            

            
                
                
                

    

    

