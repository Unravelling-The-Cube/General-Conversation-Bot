# BizBot - Discord Chatbot

BizBot is a simple Discord chatbot that can be trained with patterns and responses to provide automated responses based on user input. It uses the Discord API and allows you to switch between training mode and product mode.

## Setup

#### 1. Clone the repository:
```bash
git clone https://github.com/your-username/BizBot.git
cd BizBot
```
#### 2. Install the required dependencies using `pip`:
```bash
pip install discord.py
```
#### 3. Obtain a Discord bot token:
   - Create a new Discord application and bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the bot token.

#### 4. Replace the `apikey` variable in the code:
   - Open `BizBot.py` in a text editor.
   - Find the line `apikey = ""`.
   - Replace the value inside the double quotes with your Discord bot token obtained in step 3.

#### 5. Run the bot:
   - In a terminal or command prompt, navigate to the project directory.
   - Run the following command:
   ```bash
   python BizBotv2.py
   ```
## Usage

###  Training Mode:
  - In training mode, the bot will accept queries and their corresponding responses to improve its training data.
  - Send a direct message to the bot and follow the instructions to provide query-response pairs for training.
  - Each query can have multiple responses separated by `|`.
  - Example input: `query1|query2|query3 , response1|response2|response3`

### Product Mode:
  - In product mode, the bot will respond to incoming messages based on its trained data.
  - The bot will respond to direct messages with the most appropriate response based on the user input.

### Requirements
- Python 3.x

### Dislaimer
The code provided in this repository is for educational and informational purposes only. While we have made every attempt to ensure that the information contained in this repository is accurate and reliable, we disclaim all liability for any damages that may arise from its use.

By using the code provided in this repository, you agree to hold harmless the owners and contributors from any claims, damages, or losses that may result from its use. We make no guarantees or warranties regarding the accuracy, completeness, or adequacy of the information contained in this repository.

The code provided in this repository is not intended to be a substitute for professional advice. Users of this code should always seek the advice of qualified professionals for any specific questions or concerns regarding its use.

By using the code provided in this repository, you agree to indemnify, defend, and hold harmless the owners and contributors from any claims, damages, or losses that may arise from its use.

## Contributing

Contributions are welcome! If you find any issues or want to improve the code, feel free to create a pull request. If you would like to contribute a corpus submit it in an issue!
## Authors

- [@bizbazboz](https://www.github.com/bizbazboz)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
