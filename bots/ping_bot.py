from config import app
from mirai import Mirai, GroupMessage, FriendMessage, Friend, Group, Plain

@app.receiver('GroupMessage')
async def gm(message: GroupMessage, group: Group):
    if message.toString() == 'ping':
        await app.sendGroupMessage(group, [Plain('pong')])

@app.receiver('FriendMessage')
async def fm(message: FriendMessage, sender: Friend):
    if message.toString() == 'ping':
        await app.sendFriendMessage(sender, [Plain('pong')])