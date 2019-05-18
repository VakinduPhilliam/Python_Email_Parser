# Python Email Communication System
# How to use the email package to read, write, and send 
# To copy all mail from a Babyl mailbox to an MH mailbox, converting 
# all of the format-specific information that can be converted:
 
import mailbox

destination = mailbox.MH('~/Mail')
destination.lock()

for message in mailbox.Babyl('~/RMAIL'):
    destination.add(mailbox.MHMessage(message))

destination.flush()
destination.unlock()
