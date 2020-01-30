This is a program that sends messages from a Discord Channel into a GroupMe Chat.  I am working on implementing messages from the GroupMe into the Discord.

To run this, run the following code in your terminal first:
    ```pip install json
    pip install discord
    pip install requests```
Then, create the following two files:
    discord_files/token_manager.py
    groupme_files/token_manager.py

Each of these should be a python file with the following code:
    `TOKEN = 'INSERT_TOKEN_HERE'`
For the Discord one, set the token to a token for a Discord bot.  For GroupMe, set the token to a GroupMe Bot ID (gotten at https://dev.groupme.com/bots).

If this isn't clear enough, make a pull request request and I can clarify this!

Enjoy!