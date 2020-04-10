from config import Session

session = None

def getSession():
    global session
    if not session:
        session = Session()
    return session