import os
import datetime

# scanned paths
Paths = '/home/edzyl/oldlog'
# delete days
Dday = 15


def shouldkeep(file):
    if datetime.datetime.fromtimestamp( os.path.getmtime(file) ) > \
        datetime.datetime.now() - datetime.timedelta(Dday):
        return True
for i in os.walk(Paths):
     for j in i[2]:
        if not shouldkeep(os.path.join(i[0],j)):
            print os.path.join(i[0],j)
            os.remove( os.path.join(i[0],j) )
