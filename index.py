import discord, os, contextlib

class Purger(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(request_offline_members=False, chunk_guilds_on_startup=False, guild_subscriptions=False, **kwargs)
    
    async def on_connect(self):
        print('Now purging')
        with contextlib.suppress('discord.errors.Forbidden'):
            if not self.user.friends:
                print('No friends to remove.')
                return
            for friend in self.user.friends:
                print(f'Removing {str(friend)}')
                await friend.remove_friend()                
            print('Finished purging friends.')
        
    def main(self):
        os.system('cls')
        token = input('Token: ')
        os.system('cls')
        try:
            self.run(token, bot=False)
        except: 
            print('Improper token was given.')
            os.system('pause')
            
(Purger()).main()
