from mirai import Plain, MessageChain
from mirai.event.message.base import MessageComponentTypes
from config import Session
from data.connect_data import GroupLink

class ConnectService():
    def __init__(self):
        self.session = Session()

    def addLink(self, fr, to)->tuple:
        if self.session.query(GroupLink).filter(GroupLink.fr == fr and GroupLink.to == to).all():
            return (False, 'Link already exists.')
        else:
            link = GroupLink(fr=fr,to=to)
            self.session.add(link)
            self.session.commit()
            return (True,)

    def removeLink(self, fr, to)->tuple:
        link = self.session.query(GroupLink).filter(GroupLink.fr == fr and GroupLink.to == to).first()
        if link:
            self.session.delete(link)
            return (True,)
        else:
            return (False, 'Link does not exist.')

    async def push(self, msg: MessageChain, sender, senderName, group, groupName, callback):
        tar = [(x.fr, x.to) for x in self.getLinks() if x.fr == group]
        for (_,t) in tar:
            await callback(t, [Plain('({0}){1}:\n'.format(groupName, senderName))] + [x for x in list(msg) if x.type != MessageComponentTypes.Source])

    def getLinks(self):
        return self.session.query(GroupLink).all()