import discord
from discord.ext import commands

TOKEN = 'your token here'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# # destination guild & channel
# # union for now
# # change with yours
destination_guild_id = 1232900006831194132
destination_channel_id = 1232900197106061332


@bot.listen('on_message')
async def message_listener(message):
  start_permission = False
  # # # work with both text channel  & private
  source_channel_name = message.channel  # return dm =name , channel = name
  source_channel_id = message.channel.id  # return dm = id , channel = id
  source_message = message.content  # return text of message
  source_channel_type = message.channel.type  # return private or text
  source_sender_id = (message.author.id)  # return id ~ user id
  source_mention = message.author.mention  # return mention user
  archive_message_form = ''
  source_guild_name = ''
  source_channel_name = ''
  source_guild_id = ''
  is_bot_value = False  # change it , its not good way later

  if message.guild:  # come from server
    # # source channels
    # # # only for text channel not private
    source_guild_name = message.guild  # return dm =error , guild = name
    source_channel_name = message.channel.name  # return dm =error , channel = name
    source_guild_id = message.guild.id  # return dm = error , guild = id
    is_bot_value = message.author.bot
    if destination_channel_id != source_channel_id:  # to not take memo from destination_channel_id, and can set memo in destination_channel_id manuly
      start_permission = True

  else:  # come from dm
    is_bot_value = message.author.bot
    start_permission = True
  if is_bot_value == False:
    if start_permission == True:

      send_box_message = source_message
      noted = False
      send_box_message = send_box_message.strip().replace("  ", " ")
      middle = " note "
      start = "note "
      if len(send_box_message) >= len(middle) or len(send_box_message) >= len(
          start):
        if middle in send_box_message:
          text_note = send_box_message.index(middle) + len(middle)
          final_text_note = send_box_message[text_note:].strip()
          noted = True
        elif start in send_box_message:
          text_note = send_box_message.index(start) + len(start)
          final_text_note = send_box_message[text_note:].strip()
          noted = True
        else:
          #"-note order start = none"
          pass
      else:
        #"-note order len = None-"
        pass

      if noted == True:
        channel_destination = bot.get_channel(destination_channel_id)
        destination_channel_link = f'https://discord.com/channels/{destination_guild_id}/{destination_channel_id}'
        if message.guild:
          archive_message_form = '------\n\nctitle: ' + message.guild.name + '\n' + 'userName: ' + message.author.name + '\n' + 'userGName: ' + message.author.global_name + '\n' + 'Memo: ' + '\n' + final_text_note + '\n\n------'
        else:
          archive_message_form = '------\n\nctitle: ' + 'BotFriends' + '\n' + 'userName: ' + message.author.name + '\n' + 'userGName: ' + message.author.global_name + '\n' + 'Memo: ' + '\n' + final_text_note + '\n\n------'

#destination_message_link = f'https://discord.com/channels/{destination_guild_id}/{destination_channel_id}/<message_id>' # need get message id that will store before store it then use it to send link to user if he from another server
        note_report_to_user = ''
        await channel_destination.send(archive_message_form)
        if destination_guild_id != source_guild_id:
          note_report_to_user = f"Ya Ho .. \n\tYour Memo\n\t\twas shared\n\nyou can see you Memo here:\n{destination_channel_link}"
        else:
          note_report_to_user = f"Ya Ho .. \n\tYour Memo\n\t\twas shared"
        await message.reply(note_report_to_user)
bot.run(TOKEN)
