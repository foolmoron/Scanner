const escpos = require('escpos');
escpos.USB = require('escpos-usb');

const device = new escpos.USB(0x4b43, 0x3538);
const printer = new escpos.Printer(device);

device.open(function (error) {
    printer
        .font('a')
        .align('ct')
        .style('bu')
        .size(1, 1)
        .text('The quick brown fox jumps over the lazy dog')
        .then(() => {
            printer.cut().close();
        });
});
