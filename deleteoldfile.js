import os
import datetime

def shouldkeep(file):
    if datetime.datetime.fromtimestamp( os.path.getmtime(file) ) > \
        datetime.datetime.now() - datetime.timedelta(15):
        return True
for i in os.walk('/home/stevenli/control_center/share/web_control_center/data/debuglog/'):
     for j in i[2]:
        if not shouldkeep(os.path.join(i[0],j)):
            print os.path.join(i[0],j)
            #os.remove( os.path.join(i[0],j) )