from escpos.printer import Usb
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("~/scanner-d8c37-firebase-adminsdk-gg1hp-549bb9ca05.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

p = Usb(0x4b43, 0x3538, 0, 0x81, 0x03)
# p.text('Once upon a time in a computer  mainframe far far away...\n')
# imagename = '1 - A baby in jail with prison clothes on and a robber outfit as pixel art.png'
# p.image(imagename)
# p.barcode(code='8612163481903', function_type='B', bc='CODE128', height=128, width=2)
# p.text('blah\nblah\nblah\nblah\nblah\n')
# print_barcode(p, 'ND2xtYhxffVDNhcxZS86')
# p.cut()

def print_barcode(code):
    p.barcode(code=code, function_type='B', bc='CODE128', height=128, width=2)
    p.cut()

def on_snapshot(snapshot, changes, read_time):
    for change in changes:
        if change.type.name == "MODIFIED":
            print(f'Found new doc, printing barcode for {change.document.id}')
            print_barcode(change.document.id)

query = db.collection("tickets")
query_watch = query.on_snapshot(on_snapshot)
print(f'Listening to updates')
