from datetime import datetime
from pytz import timezone
import sqlite3
import os.path

datetoday = datetime.now(timezone('Asia/Kolkata')).strftime("%d/%m/%y")
# datetoday = "21/09/2005"

def getBDlist():
    global datetoday

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "students.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    bdlist = []
    sttable = cur.execute("select name,dob from students").fetchall()
    for i in sttable:
        if i[1][:5]==datetoday[:5]:
            bdlist.append(i[0])
    conn.close()
    return bdlist

if __name__=="__main__":
    bdlist = getBDlist()
    if len(bdlist)!=0:
        print("Today is birthday of:")
        for i in bdlist:
            print(i)
    else:
        print("Today is no one's birthday.")

