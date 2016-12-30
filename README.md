This script will run on a Synology NAS, and will update an OpenDNS service with your home IP address - which is likely changed after you reboot your home router. 

You need to put your OpenDNS username and password into the ddns.yaml file.

By default the script will update every 5 minutes but you can change this in the YAML file

This script should be added to the startup for your NAS.

**

Full instructions of getting this working below:
1/ Create an account on OpenDNS

https://www.opendns.com/home-internet-security/


Use the Sign Up button


2/  In your OpenDNS account settings you can choose the level of filtering you want.  Medium will block porn, torrents, and lots of stuff.  You can customise it a lot


3/ On your home router you need to change which DNS server it uses.  This will depend a lot on the device so hopefully people can figure this out.  New DNS servers:

208.67.222.123   AND/OR 208.67.220.123


4/  Last part - your home router will usually get a new address from your service provider when it reboots - so you need to tell OpenDNS your address each time.  OpenDNS also runs this site to help:

https://dnsomatic.com/

This uses the same account as OpenDNS.  You need to sign in here and then enable it for OpenDNS service.

5/ Install this script into your NAS
I added this to run at startup on the NAS:

/etc/rc.local 

admin@DiskStation:~$ more /etc/rc.local
#!/bin/sh

python3 /var/services/homes/admin/ddns.py
