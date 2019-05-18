# Python Email Communication System
# How to use the email package to read, write, and send 
# simple email messages, as well as more complex MIME 
# messages.
# This demonstrates how to create an HTML message with an alternative 
# plain text version. 
# To make things a bit more interesting, we include a related image 
# in the html part, and we save a copy of what we are going to send to 
# disk, as well as sending it.
 

#!/usr/bin/env python3

import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

# Create the base text message.

msg = EmailMessage()
msg['Subject'] = "Ayons asperges pour le d�jeuner"
msg['From'] = Address("Pep� Le Pew", "pepe", "example.com")
msg['To'] = (Address("Penelope Pussycat", "penelope", "example.com"),
             Address("Fabrette Pussycat", "fabrette", "example.com"))
msg.set_content("""\
Salut!

Cela ressemble � un excellent recipie[1] d�jeuner.

[1] http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718

--Pep�
""")

# Add the html version.  This converts the message into a multipart/alternative
# container, with the original text message as the first part and the new html
# message as the second part.

asparagus_cid = make_msgid()
msg.add_alternative("""\

<html>
  <head></head>
  <body>
    <p>Salut!</p>
    <p>Cela ressemble � un excellent
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
            recipie
        </a> d�jeuner.
    </p>
    <img src="cid:{asparagus_cid}" />
  </body>
</html>

""".format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

# note that we needed to peel the <> off the msgid for use in the html.

# Now add the related image to the html part.

with open("roasted-asparagus.jpg", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid)

# Make a local copy of what we are going to send.

with open('outgoing.msg', 'wb') as f:
    f.write(bytes(msg))

# Send the message via local SMTP server.

with smtplib.SMTP('localhost') as s:
    s.send_message(msg)
