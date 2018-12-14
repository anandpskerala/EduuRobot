import config
import requests
import time
import os

bot = config.bot


def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/print ') or msg['text'].startswith('!print '):
            try:
                sent = bot.sendMessage(msg['chat']['id'], 'Tirando print...',
                                reply_to_message_id=msg['message_id'])
                ctime = time.time()
                r = requests.get(f"https://api.thumbnail.ws/api/{config.keys['screenshots']}/thumbnail/get",
                                params=dict(url=msg['text'][7:], width=1280))
                with open(f'{ctime}.png', 'wb') as f:
                    f.write(r.content)

                bot.sendPhoto(msg['chat']['id'],
                              open(f'{ctime}.png', 'rb'),
                              reply_to_message_id=msg['message_id'])
                bot.deleteMessage((msg['chat']['id'], sent['message_id']))
            except Exception as e:
                bot.editMessageText((msg['chat']['id'], sent['message_id']), f'Ocorreu um erro ao enviar a print, favor tente mais tarde.\nErro: {e}')
            finally:
                os.remove(f'{ctime}.png')
            return True
