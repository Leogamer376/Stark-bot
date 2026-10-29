import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

LAYOUT = {
    "🪵 ｜ 𝘌𝘯𝘵𝘳𝘢𝘯𝘤𝘦 𝘈𝘳𝘦𝘢": ["👋｜𝘈𝘳𝘳𝘪𝘷𝘢𝘭-𝘨𝘢𝘵𝘦𝘴", "📜｜𝘓𝘢𝘸𝘴-𝘰𝘧-𝘵𝘩𝘦-𝘯𝘰𝘳𝘵𝘩", "🛡️｜𝘑𝘰𝘪𝘯-𝘵𝘩𝘦-𝘸𝘢𝘵𝘤𝘩", "🤝｜𝘕𝘰𝘳𝘵𝘩𝘦𝘳𝘯-𝘢𝘭𝘭𝘪𝘢𝘯𝘤𝘦𝘴"],
    "📢 ｜ 𝘓𝘢𝘵𝘦𝘴𝘵 𝘙𝘢𝘷𝘦𝘯𝘴": ["📢｜𝘚𝘦𝘳𝘷𝘦𝘳-𝘢𝘯𝘯𝘰𝘶𝘯𝘤𝘦𝘮𝘦𝘯𝘵𝘴", "⚔️｜𝘌𝘷𝘦่น𝘵-𝘢𝘯𝘯𝘰𝘶𝘯𝘤𝘦𝘮𝘦𝘯𝘵𝘴"],
    "🏆 ｜ 𝘛𝘩𝘦 𝘛𝘰𝘶𝘳𝘯𝘢𝘮𝘦𝘯𝘵 𝘎𝘳𝘰𝘶𝘯𝘥𝘴": ["🏹｜𝘛𝘰𝘶𝘳𝘯𝘦𝘺-𝘧𝘪𝘦𝘭𝘥", "🔊｜𝘛𝘩𝘦 𝘚𝘵𝘢𝘨𝘦"],
    "🏰 ｜ 𝘞𝘪𝘯𝘵𝘦𝘳𝘧𝘦𝘭𝘭 𝘊𝘰𝘶𝘳𝘵𝘺𝘢𝘳𝘥": ["🍻｜𝘞𝘪𝘯𝘵𝘦𝘳𝘧𝘦𝘭𝘭-𝘩𝘢𝘭𝘭", "🎭｜𝘑𝘦𝘴𝘵𝘦𝘳-𝘤𝘰𝘶𝘳𝘵𝘺𝘢𝘳𝘥", "📷｜𝘋𝘪𝘳𝘦𝘸𝘰𝘭𝘧-𝘥𝘦𝘯", "🛡️｜𝘉𝘢𝘯𝘯𝘦𝘳𝘮𝘦𝘯-𝘥𝘪𝘴𝘱𝘭𝘢𝘺"],
    "🔊 ｜ 𝘛𝘩𝘦 𝘎𝘳𝘦𝘢𝘵 𝘏𝘢𝘭𝘭": ["🔊｜𝘛𝘩𝘦 𝘎𝘳𝘦𝘢𝘵 𝘏𝘢𝘭𝘭", "🔊｜𝘛𝘩𝘦 𝘊𝘳𝘺𝘱𝘵𝘴", "🔒｜𝘓𝘰𝘳𝘥𝘴 𝘚𝘰𝘭𝘢𝘳", "🔒｜𝘔𝘢𝘦𝘴𝘵𝘦𝘳𝘴 𝘛𝘰𝘸𝘦𝘳"],
    "⚔️ ｜ 𝘛𝘩𝘦 𝘞𝘢𝘳 𝘙𝘰𝘰𝕞": ["🔊｜𝘛𝘢𝘣𝘭𝘦 𝘐", "🔊｜𝘛𝘢𝘣𝘭𝘦 𝘐𝘐", "🔊｜𝘛𝘢𝘣𝘭𝘦 𝘐𝘐𝘐", "🔊｜𝘛𝘢𝘣𝘭𝘦 𝘐𝘝", "🔊｜𝘛𝘢𝘣𝘭𝘦 𝘝", "🔊｜➕ 𝘚𝘶𝘮𝘮𝘰ﻥ 𝘉𝘢𝘯𝘯𝘦𝘳𝘮𝘦𝘯"],
    "🤖 ｜ 𝘛𝘩𝘦 𝘊𝘪𝘵𝘢𝘥𝘦𝘭 𝘍𝘰𝘳𝘨𝘦𝘴": ["#🤖｜𝘊𝘪𝘵𝘢𝘥𝘦𝘭-𝘧𝘰𝘳𝘨𝘦𝘴"],
    "🎵 ｜ 𝘛𝘩𝘦 𝘉𝘢𝘳𝘥𝘴 𝘏𝘦𝘢𝘳𝘵𝘩": ["#🎵｜𝘚𝘰𝘯𝘨𝘴-𝘰𝘧-𝘪𝘤𝘦", "🔊｜𝘛𝘩𝘦 𝘉𝘢𝘳𝘥𝘴 𝘊𝘰𝘳𝘯𝘦𝘳", "🔊｜𝘔𝘪𝘯𝘴𝘵𝘳𝘦𝘭 𝘏𝘢𝘭𝘭"]
}

@bot.event
async def on_ready():
    print("House Stark bot is online!")

@bot.command()
async def build_stark(ctx):
    await ctx.send("🔨 Building Winterfell... Please wait.")
    for cat_name, channels in LAYOUT.items():
        category = await ctx.guild.create_category(cat_name)
        for ch_name in channels:
            if "🔊" in ch_name or "🔒" in ch_name:
                await ctx.guild.create_voice_channel(ch_name, category=category)
            elif "𝘚𝘵𝘢𝘨𝘦" in ch_name:
                await ctx.guild.create_stage_channel(ch_name, category=category)
            else:
                await ctx.guild.create_text_channel(ch_name, category=category)
    await ctx.send("❄️ **Winterfell is complete!**")

bot.run(MTU2NTM0OTU3ODM5ODYzODEzMg.GbMrQ_.KyHUiZ_9FIAwBo3PDIzHds5H2Dv9lNUPh0xPQc)
