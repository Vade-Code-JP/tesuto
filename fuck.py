discord.py
import discord

TOKEN = "MTQ2Mjc3NzQzMDI3NTI2NDY1NQ.GxYgRE.Xf-CIMvrhrIKxPF3xMtISG5g8sUYTDOWEN0nnc"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"ログイン完了: {client.user}")

    for guild in client.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send("ハロー")
                print(f"{guild.name} / #{channel.name} に送信")
                return  # 1回送ったら終了
            except:
                continue

client.run(TOKEN)