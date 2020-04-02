class ConversationFlow:
    
    TARGET_FRIEND = 1
    TARGET_GROUP = 2
    
    target = TARGET_FRIEND
    triggerWord = None

    def __init__(self, callback_say, callback_kill):
        self.callback_say = callback_say
        self.callback_kill = callback_kill
    
    def handle(self, message: str, sender: int, senderName: str):
        pass

    def onBegin(self, sender:int, senderName: str):
        pass

class ConversationManager:

    def __init__(self):
        self.flows = []
        self.sessions = {}

    def getCurrentFlow(self, id:int)->ConversationFlow:
        return self.sessions[id] if id in self.sessions else None

    def registerFlow(self, flow):
        self.flows.append(flow)

    def match(self, message: str)->tuple:
        flows = [x for x in self.flows if message.startswith(x.triggerWord)]
        if flows:
            return (True, flows[0])
        else:
            return (False, None)

    def beginWith(self, flow: ConversationFlow, id: int, sender: int, senderName: int):
        self.sessions[id] = flow
        flow.onBegin(sender, senderName)

    def terminal(self, id:int):
        del self.sessions[id]