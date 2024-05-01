


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    start_private_msg = ' welcome to private chat'
    help_private_msg = 'how help you?'
    start_supergroup_msg = f' welcome to our {message.chat.title} chat'
    help_supergroup_msg = 'how help you?'
    if message.chat.type == 'supergroup':
        start_command = '/start'+'@MrMemosBot'
        help_command = '/help'+'@MrMemosBot'
        if message.text == start_command:
            bot.reply_to(message, start_supergroup_msg)
        elif message.text == help_command:
            bot.reply_to(message, help_supergroup_msg)
        #set option to /mention_admin to send (help message) to online admins
    elif message.chat.type == 'private':
        start_command = '/start'
        help_command = '/help'
        if message.text == start_command:
            bot.reply_to(message, start_private_msg)
        elif message.text == help_command:
            bot.reply_to(message, help_private_msg)

####

destination_channel_id = -1.....
@bot.message_handler(content_types=['text'])
def forward_message(message):
    #if message.chat.id == source_channel_id:
    if message.chat.id != destination_channel_id:
        if message.from_user.is_bot is False:
            def note_order(send_box_message=None):
                noted = False
                send_box_message = send_box_message.strip().replace("  ", " ")
                middle = " note "
                start = "note "
                if len(send_box_message) >= len(middle) or len(send_box_message) >= len(start):
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
                     if message.chat.type != 'private':
                        archive_message_form = 'ctitle::'+message.chat.title+'\n'+'cUName::'+message.chat.username+'\n'+'cId::'+str(message.chat.id)+'\n'+'fName::'+message.from_user.first_name+'\n'+'uName::'+message.from_user.username+'\n'+'uId::'+str(message.from_user.id)+'\n'+'uMessage::'+final_text_note 
                    else:
                        archive_message_form = 'ctitle::'+'Bot_private'+'\n'+'cUName::'+message.chat.username+'\n'+'cId::'+str(message.chat.id)+'\n'+'fName::'+message.from_user.first_name+'\n'+'uName::'+message.from_user.username+'\n'+'uId::'+str(message.from_user.id)+'\n'+'uMessage::'+final_text_note 
                    bot.send_message(destination_channel_id, archive_message_form)
                    note_report_to_user = f"{final_text_note} is saved"
                    bot.reply_to(message, note_report_to_user)
            send_box_message= note_order(message.text)
'''
# destination_channel_group_id = -100 
# destination_channel_id = -10021  
@bot.message_handler(content_types=['text'])
def forward_message(message):
    #destination_channel_link =
       # if group id != channel id to check if not come from channel that store notes inside of it
    if message.chat.id != destination_channel_id:
        if message.from_user.is_bot is False:
            # you do not need (def function note_order, so can write else codes without it, when add and store inside another db also, then can use def and another def to display and show memos in anothers group-private-channels, as list for each own one was send it)
            def note_order(send_box_message=None):
                noted = False
                send_box_message = send_box_message.strip().replace("  ", " ")
                middle = " note " # you can change word, like " botname note " # this for store from inside of some statement 
                start = "note " # change word here too like "botname note " # this for store from start of some statement 
                if len(send_box_message) >= len(middle) or len(send_box_message) >= len(start):
                    if middle in send_box_message:
                        text_note = send_box_message.index(middle) + len(middle)
                        final_text_note = send_box_message[text_note:].strip()
                        noted = True
                    elif start in send_box_message:
                        text_note = send_box_message.index(start) + len(start)
                        final_text_note = send_box_message[text_note:].strip()
                        noted = True
                    else:
                        #"-note order start = none" # use it if you add wait user write bot name with "note" word or else
                        pass
                else:
                    #"-note order len = None-" # use it if you add wait user write bot name with "note" word or else
                    pass
                if noted == True:
                    # note import to write all this in archive_message_form, you just store the note memo alone
                    if message.chat.type != 'private':
                        
                        archive_message_form = '------\n\nctitle: ' + message.chat.title + '\n' + 'fName: '  + message.from_user.first_name + '\n' + 'uName: ' + message.from_user.username + '\n' + 'Memo:' + final_text_note + '\n\n------'
                    else:
                        archive_message_form = '------\n\nctitle: ' + 'BotFriends' + '\n' + 'fName: '  + message.from_user.first_name + '\n' + 'uName: ' + message.from_user.username+'\n' + 'Memo:' + final_text_note + '\n\n------'
                    #here send to channed to store, not know how send images , or check if it only text or with image also
                    bot.send_message(destination_channel_id, archive_message_form)
                    note_report_to_user = ''
                    # if destination_channel_id != source that message come from: # then need to send link of channel
                    note_report_to_user = f"Ya Ho .. \n\tYour Memo\n\t\twas shared\n\nyou can see you Memo here:\n{destination_channel_link}"
                    #elif it come from group that follow store channel, then no need to send channel link
                    note_report_to_user = f"Ya Ho .. \n\tYour Memo\n\t\twas shared"
                    bot.reply_to(message, note_report_to_user)
            send_box_message= note_order(message.text)
bot.infinity_polling()
'''
