from mirai import Mirai
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env import _MASTERS_QQ_LIST_, _SELF_QQ_, _MIRAI_AUTHKEY_, _MIRAI_ENDPOINT_

qq = _SELF_QQ_
masters = _MASTERS_QQ_LIST_
authKey = _MIRAI_AUTHKEY_
mirai_api_http_locate = _MIRAI_ENDPOINT_
app = Mirai(f"mirai://{mirai_api_http_locate}?authKey={authKey}&qq={qq}")

engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)