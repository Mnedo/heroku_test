import asyncio

import discord
from requests import get

TOKEN = "ODMxMTY1MzE4Nzg0NjE0NDIw.YHRRBg.WisH7vsUwyAu1o3xDSeQaEU9UG4"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            if "stop" in message.content.lower():
                await 'logout'
            else:
                file = get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
                await message.channel.send(file)


client = YLBotClient()
client.run(TOKEN)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_ready())



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
