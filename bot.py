import os
import importlib
from dotenv import load_dotenv
from hata import Client, start_clients, events, Embed

extensions = ("mew", "fun")

load_dotenv()
hata_client = Client(os.getenv("BOT_TOKEN"))
on_command = hata_client.events(events.CommandProcesser("!")).shortcut

for extension in extensions:
    module = importlib.import_module(f"extensions.{extension}")
    on_command.extend(module.extension)


@hata_client.events
class Ready:
    def __init__(self):
        self.called = False

    async def __call__(self, client):
        login_message = f" --> {client:f} ({client.id}) logged in UwU"

        if self.called:
            print(f"Reconnected {login_message}")
            return
        self.called = True

        await client.update_application_info()
        print(f"Hello {client.owner:f} {login_message}")


@on_command
async def invalid_command(client, message, command, content):
    await client.message_create(message.channel,
                                embed=Embed(description=f"Mew! I do not know such thing as `{command}`"))


start_clients()
