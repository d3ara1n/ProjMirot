from services.conversations import ConversationFlow
from mirai import Plain

class Counter(ConversationFlow):

    mode = ConversationFlow.MODE_MUTIPLE | ConversationFlow.MODE_SINGLE
    triggerWord = 'count'

    def __init__(self, say, kill):
        self.callback_kill = kill
        self.callback_say = say
        self.count = {}

    async def handle(self, msg:str, sender: int, senderName: str):
        if msg == 'endcount':
            await self.callback_say([Plain('\n'.join([f'{self.count[k][0]}: {str(self.count[k][1])}' for k in self.count]))])
            self.count = {}
            self.callback_kill()
        else:
            if sender in self.count:
                self.count[sender] = (self.count[sender][0], self.count[sender][1] + 1)
            else:
                self.count[sender] = (senderName, 1)