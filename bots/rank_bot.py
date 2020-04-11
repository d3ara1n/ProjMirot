from services.rank_service import RankService
from config import app, masters
from mirai import Group, GroupMessage, Member, Plain, At, MemberChangeableSetting

service = RankService()

@app.receiver('GroupMessage')
async def gm(group: Group, sender: Member, message: GroupMessage):
    if message.toString() == '!rank.query':
        msg = [Plain('rank:\n')]
        members = await app.memberList(group.id)
        for x in service.query(group.id):
            member = [y for y in members if y.id == x[0]]
            if member:
                msg.append(Plain(f'{member[0].memberName}:{str(x[1])}\n'))
        await app.sendGroupMessage(group, msg)
    elif message.toString() == '!rank.clear' and sender.id in masters:        
        service.clear(group.id)
        await app.sendGroupMessage(group, 'rank.clear')
    else:
        service.put(group.id, sender.id)