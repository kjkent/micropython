# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import machine, os, vfs
sd = machine.SDCard(slot=0, cmd=38, sck=39, data=[40])
vfs.mount(sd, '/sdcard')
