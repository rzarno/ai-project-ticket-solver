from app.layout.Layout import Layout
from app.model.TicketImage import TicketImage

class Ticket:
    def __init__(
        self,
        layout: Layout,
    ):
        self.subject = layout.ticketSubject
        self.environment = layout.ticketEnvironment
        self.description = layout.ticketDescription
        self.url = layout.ticketUrl
        self.device = layout.ticketDevice
        self.user = layout.ticketUser

        if layout.ticketImage  is not None:
            #read file as bytes:
            bytes_data = layout.ticketImage .getvalue() #TODO handle file

    def __str__(self):
        return (f'''subject: {self.subject}\n
environment: {self.environment}\n
description: {self.description}\n
url: {self.url}\n
device: {self.device}\n
user: {self.user}\n
''')


