import re
import random
import discord
apikey = ""
query = ""
options = ""
def add_training_data(pattern, responses, filename='training.txt'):
    with open(filename, 'a') as training_file:
        training_file.write(f"Pattern: {pattern}\n")
        training_file.write(f"Responses: {','.join(responses)}\n\n")

    print("Training data added.")

def splitingtool(data, spliter):
    return data.split(spliter)

def load_training_data(filename='training.txt'):
    with open(filename, 'r') as training_file:
        training_contents = training_file.read()

    training_data = re.findall(r'Pattern:\s*(.*?)\nResponses:\s*(.*?)\n\n', training_contents, re.DOTALL)
    return training_data


def chatbot_response(user_input, training_data):
    for pattern, responses in training_data:
        if re.search(pattern, user_input, re.IGNORECASE):
            response_list = responses.split(',')
            selected_response = random.choice(response_list).strip()
            return selected_response
    
    return "Sorry, I didn't understand that."

# Using Mode
mode = input("Do you want to go into training mode or product mode? \n").lower()
if  mode == "product" or mode == "2":
    print(f"{mode} mode intialised")
    # Initialize the Discord bot
    intents = discord.Intents.default()
    bot = discord.Client(intents=intents)


    # Event to handle incoming DM messages
    @bot.event
    async def on_message(message):
        if message.guild is None and not message.author.bot:  # Check if the message is in a DM
            user_input = message.content
            training_data = load_training_data()
            response = chatbot_response(user_input,training_data)
            if response == "Sorry, I didn't understand that.":
                await message.channel.send(f"{response} Please can you DM Biz#3940 to have this query added to my programming!")
            else:
                await message.channel.send(response)
    # Run the Discord bot
    bot.run(apikey)
else:
    print(f"{mode} mode intialised")
    intents = discord.Intents.default()
    bot = discord.Client(intents=intents)
    @bot.event
    async def on_message(message):

        if message.guild is None and not message.author.bot:  # Check if the message is in a DM
            await message.channel.send("Hi, Currently the bot is in training mode! Please help me improve the bot by training it!")
            await message.channel.send("Please supply a selection of queries and then a selection of responses in the following syntax:\n query1|query2|query3 , response1|response2|response3")
            try:
                msg = await bot.wait_for('message', check=lambda msg: msg.author == message.author and msg.guild is None, timeout=60.0)
                await message.channel.send("Thank you!")
                reply = msg.content
                reply = splitingtool(reply," , ")
                query = reply[0]
                response = splitingtool(reply[1], "|")
                add_training_data(query, response)
                add_training_data(query, options)
                print(f" New data trained Query - {query} , Responses - {response}")
            except:
                message.channel.send("An error has occured, please send Y to try again.")

    # Run the Discord bot
    bot.run(apikey)

