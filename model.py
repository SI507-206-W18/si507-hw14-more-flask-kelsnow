import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init(app):
    global entries
    global next_id
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        if len(entries) > 0:
            next_id = len(entries) +1

    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE,next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    next_id+=1
    entry = {"author": name, "text": text, "id":str(next_id),"timestamp": time_string}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(p_id):
    global entries,next_id,GUESTBOOK_ENTRIES_FILE
    for i in entries: 
        if p_id == i['id']:
            entries.remove(i)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not delete the entry")




