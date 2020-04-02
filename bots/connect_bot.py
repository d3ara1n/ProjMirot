import re
from mirai import Member, Group, GroupMessage, Friend, FriendMessage, Plain
from config import qq, app, masters
from services.connect_service import ConnectService

service = ConnectService()

@app.receiver("GroupMessage")
async def event_gm(group: Group, sender: Member, message: GroupMessage):
    if sender.id != qq:
        await service.push(message.messageChain, sender.id, sender.memberName, group.id, group.name, callback)

async def callback(groupId, msg):
    await app.sendGroupMessage(groupId, msg)

@app.receiver("FriendMessage")
async def event_masterOp(sender: Friend, message: FriendMessage):
    if sender.id in masters:
        if message.toString() == 'listLink':
            lst = [str(x.fr) + ':' + str(x.to) for x in service.getLinks()]
            await app.sendFriendMessage(sender, [Plain('\n'.join(lst))])
        else:
            pattern = '^(.*)Link ([1-9][0-9]+):([1-9][0-9]+)$'
            match = re.match(pattern, message.messageChain.toString())
            if match:
                mode = match.group(1)
                fr = int(match.group(2))
                to = int(match.group(3))
                if mode == 'add':
                    res = service.addLink(fr, to)
                    await app.sendFriendMessage(sender, 'added {0}:{1}'.format(fr, to) if res[0] else res[1])

                elif mode == 'remove':
                    res = service.removeLink(fr, to)
                    await app.sendFriendMessage(sender, 'removed {0}:{1}'.format(fr, to) if res[0] else res[1])
                else:
                    await app.sendFriendMessage(sender, 'i dont know or it doesnt exist')
    else:
        await app.sendFriendMessage(sender, "小娜在国区已死, 有事烧纸, 没事也烧纸.")
        for master in masters:
            await app.sendFriendMessage(master, message.messageChain)