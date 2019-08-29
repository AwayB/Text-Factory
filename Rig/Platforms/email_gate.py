#from smtplib import SMTP
from email.message import EmailMessage
import email
import os
from email.policy import default
from imaplib import IMAP4_SSL
import getpass
from filesystem_gate import dump_in_file
import html
import html.parser
import bs4

class Email_Handler:
    def __init__(self, host='', username='', password=''):
        self.msgNum = 1
        if (host != '' and username != '' and password != ''):
            self.mailbox = self.connect(host, username, password)
        else:
            self.mailbox = IMAP4_SSL()

    def connect(self, host, username, password, use_tls=False):
        """Establishes an IMAP connection, optionally over TLS."""
        mailbox = IMAP4_SSL(host)
        mailbox.login(username, password)
        mailbox.select()
        return(mailbox)

    def get_attachments(self, msg):
        if len(msg.get_payload()) > 2:
            attachment = msg.get_payload()[1]
            print(attachment.get_content_type())
            #exit()

    def dump_message_text(self, msg):
        if msg.is_multipart():
            for payload in msg.get_payload():
                print(payload.get_payload(decode=True))
        else:
            soup = bs4.BeautifulSoup(msg.get_payload(decode=True), features='html.parser')
            for script in soup(['script', 'style']):
                script.extract()
            complete = str()
            complete += 'From:' + msg['from'] + '\n'
            complete += 'To:' + msg['to'] + '\n'
            complete += 'Date:' + msg['date'] + '\n'
            complete += soup.get_text()
            dump_in_file('test.html', complete)

    def get_next_message(self, amount):
        mailbox = self.mailbox
        #print(mailbox.recent())
        data = mailbox.search(None, 'ALL')[1]
        msg = list()
        for _ in range(amount):
            data = mailbox.fetch(data[0].split()[amount], '(RFC822)')[1]
            msg += email.message_from_bytes(data[0][1])
        return(msg)

    def get_message(self, message=None):
        mailbox = self.mailbox
        print(mailbox.recent())
        data = mailbox.search(None, 'ALL')[1]
        data = mailbox.fetch(data[0].split()[0], '(RFC822)')[1]
        msg = email.message_from_bytes(data[0][1])
        return(msg)

    def __exit__(self, exc_type, exc_value, traceback):
        self.mailbox.close()
        self.mailbox.logout()



e = Email_Handler('imap', 'me', getpass.getpass())
e.get_attachments(e.get_next_message(200))
#e.dump_message_text(e.get_message())
# with SMTP('') as smtp:
#     print(smtp.ehlo(''))
#     smtp.help()
#     smtp.connect('172.16.196.109', port=25)
