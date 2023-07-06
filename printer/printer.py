from escpos.printer import Usb

p = Usb(0x4b43, 0x3538, 0, 0x81, 0x03)
# p.text("Once upon a time in a computer  mainframe far far away...\n")
imagename = "1 - A baby in jail with prison clothes on and a robber outfit as pixel art.png"
p.image(imagename)
# p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.text("\n " + imagename)
p.cut()
