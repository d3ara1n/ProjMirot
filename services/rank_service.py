from data.rank_data import MessageCount
from data import getSession

class RankService():

    def __init__(self):
        self.session = getSession()

    def put(self, group:int, sender:int):
        msgCnt: MessageCount = self.session.query(MessageCount).filter(MessageCount.group == group, MessageCount.person == sender).first()
        if msgCnt:
            msgCnt.count += 1
        else:
            msgCnt = MessageCount(person=sender,group=group,count=1)
            self.session.add(msgCnt)
        self.session.commit()
    
    def query(self, group:int)->list:
        # [(id, count)]
        return [(x.person, x.count) for x in self.session.query(MessageCount).filter(MessageCount.group == group).order_by(MessageCount.count.desc()).all()]

    def clear(self, group: int):
        self.session.query(MessageCount).filter(MessageCount.group == group).delete()
        self.session.commit()
        