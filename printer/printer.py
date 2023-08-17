from datetime import datetime
import os
import time
from escpos.printer import Usb
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(os.path.expanduser('~') + "/scanner-d8c37-firebase-adminsdk-gg1hp-549bb9ca05.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

p = Usb(0x0416, 0x5011, 0, 0x81, 0x01)
def print_barcode(code, name):
    p.text('\n\n\n\n')
    p.barcode(code=code, function_type='B', bc='CODE128', height=128, width=2, pos="OFF")
    p.text('\nID: ')
    p.text(name)
    p.cut(mode='PART')

initializing = True
def on_snapshot(snapshot, changes, read_time):
    global initializing
    if initializing:
        initializing = False
        return
    for change in changes:
        if change.type.name == "ADDED":
            print(f'Found new doc, printing barcode for {change.document.id}')
            print_barcode(change.document.id, change.document.to_dict()['name'])

query = db.collection("tickets")
query_watch = query.on_snapshot(on_snapshot)

print(f'Listening to updates since {datetime.now().isoformat()}')
while True:
    time.sleep(5*60)
    print(f'Still listening...')
