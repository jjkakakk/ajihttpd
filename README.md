
AJIHTTPD - Web Server for AddJavascriptInterface Sample App
==============

A simple web server that serves examples pages with some examples of the
exploitation of AddJavascriptInterface.

To be used alongside sample android application (ajitest) that uses a webview with 
addjavascriptinterface, pulling from an IP address that you specify in
the application. 

Running
--------------

- Working python tornado
- python ./run.py
- in your device/emulator launch the app, and point it at your
  server:port like 'http://192.168.1.1:8585/aji/ls'

Contains
--------------

- emu-writesd.html (write a file to the sdcard)
- example1.html (example the shows toast/logcat message, intended
  behaviour of app, these are the '@JavascriptInterface' enabled
methods)
- id (short form pointing at id.html)
- id.html (shows the id of the user)
- ls (short form pointing at ls.html)
- ls.html (list the /mnt/sdcard/ contents)
- lsd (short form pointing at lsd.html)
- lsd.html (list the /mnt/sdcard/Download contents, useful after 'write')
- n (short form point at example1.html)
- old (working dir, broken stuff)
- run.py (main server)
- sms (short form pointing at sms.html)
- sms.html (send a sms through aji (hence why android app has send sms
  perms))
- template.html (blah)
- write (short form pointing at emu-writesd.html)


