botsock
=========

Secure ssl socket server for bot communication.

>>> pip install botsock

commands.py
from botcom import Command, CommandHandler
class PingCommand(Command):
    def __init__(self):
        pass
class PingCommandHandler(CommandHandler):
    def handle(self, command):
        return 'pong'

client.py
from commands import PingCommand
from botsock import send_data
if __name__ == '__main__':
    data = send_data(PingCommand())
    print(data)

server.py
from botcom import Bus
from botsock import Server
bus = Bus()
def callback(cmd):
    return bus.execute(cmd)
if __name__ == '__main__':
    Server(callback=callback).serve_forever()
