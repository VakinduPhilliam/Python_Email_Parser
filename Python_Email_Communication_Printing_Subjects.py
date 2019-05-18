# Python Email Communication System
# How to use the email package to read, write, and send 
# A simple example of printing the subjects of all messages in 
# a mailbox that seem interesting:
 
import mailbox

for message in mailbox.mbox('~/mbox'):
    subject = message['subject']       # Could possibly be None.

    if subject and 'python' in subject.lower():
        print(subject)
