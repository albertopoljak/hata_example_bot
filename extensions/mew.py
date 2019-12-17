from hata import eventlist, Embed

extension = eventlist()


@extension
async def mew(client, message, content):
    await client.message_create(message.channel, embed=Embed(description="mew"))


@extension
async def default_event(client, message):
    if message.author.is_bot:
        return
    content = message.content
    if len(content) != 3:  # filter out totally useless cases
        return

    content = content.lower()

    if content == "owo":
        result = "OwO"
    elif content == "uwu":
        result = "UwU"
    elif content == "0w0":
        result = "0w0"
    else:
        return

    await client.message_create(message.channel, result)