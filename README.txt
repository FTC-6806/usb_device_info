
    $ usb_device_info.py
    ~~~~~~~~^
   |
    ~~~~~~~< a simple usb info-getter

 dependencies:
 `pip install click`, and then `pip install pyusb --pre`

 usage:
 $ python usb_device_info.py <vid> <pid>

 output is human-readable.

 for FTC, vid = 0x0403 and pid = 0x6001
 