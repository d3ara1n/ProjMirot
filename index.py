from config import app, Base
# used bots region
from bots import connect_bot
# eng of bots region

if __name__ == "__main__":
    Base.metadata.create_all()
    app.run()