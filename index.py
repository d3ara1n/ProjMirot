from config import app, Base
from mirai import Group, GroupMessage, Member, Friend, FriendMessage
# used bots region
from bots import connect_bot, conversation_bot, ping_bot, rank_bot
# end of bots region

if __name__ == "__main__":
    Base.metadata.create_all()
    app.run()