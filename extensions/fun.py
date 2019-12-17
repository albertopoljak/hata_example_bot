from hata import eventlist, Embed
from hata.events_compiler import ContentParser

extension = eventlist()


@extension
async def pat(self, message, content):
    await self.message_create(message.channel, embed=Embed(description=f"{self:m} pats {message.author:m}"))


@extension
@ContentParser("user, flags=mna, default='message.author'")
async def rate(client, message, target):
    if client is target:
        rating = 10
    else:
        rating = target.id % 11

    await client.message_create(message.channel, embed=Embed(description=f"I rate {target:m} {rating}/10."))
