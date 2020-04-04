from mirai import Mirai, Group, GroupMessage, Friend, Member, FriendMessage
from config import app
from services.conversations import ConversationManager, ConversationFlow
from conversations.counter import Counter

manager = ConversationManager()

# register conversation region
manager.registerFlow(Counter)
# end of conversation region

@app.receiver('GroupMessage')
async def gm(group: Group, message: GroupMessage, sender: Member):
    msg = message.toString()
    cflow = manager.getCurrentFlow(toGid(group.id)) or manager.getCurrentFlow(toGFid(group.id, sender.id))
    if cflow:
        await cflow.handle(msg, sender.id, sender.memberName)
    else:
        res = manager.match(msg)
        if res[0]:
            flow: ConversationFlow = res[1]
            async def say(msg):
                await app.sendGroupMessage(group, msg)
            if flow.mode == ConversationFlow.MODE_MUTIPLE:
                manager.beginWith(flow(say, lambda: manager.terminal(toFid(sender.id))), toFid(sender.id), sender.id, sender.memberName)
            elif flow.mode == (ConversationFlow.MODE_MUTIPLE | ConversationFlow.MODE_SINGLE):
                manager.beginWith(flow(say, lambda: manager.terminal(toGFid(group.id, sender.id))), toGFid(group.id, sender.id), sender.id, sender.memberName)
            

@app.receiver('FriendMessage')
async def fm(message: FriendMessage, sender: Friend):
    msg = message.toString()
    if manager.getCurrentFlow(toFid(sender.id)):
        await manager.getCurrentFlow(toFid(sender.id)).handle(msg, sender.id, sender.nickname)
    else:
        res = manager.match(msg)
        if res[0]:
            flow: ConversationFlow = res[1]
            async def say(msg):
                await app.sendFriendMessage(sender, msg)
            manager.beginWith(flow(say, lambda: manager.terminal(toFid(sender.id))), toFid(sender.id), sender.id, sender.nickname)

def toFid(id: int)->int:
    return id

def toGid(id: int)->int:
    return -id

def toGFid(gid: int, fid: int)->int:
    return gid * 10**12 + fid