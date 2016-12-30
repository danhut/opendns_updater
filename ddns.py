import requests, time, yaml, argparse
from subprocess import call

def Synlog(sev,code,message):
    call(["synologset1", "sys", sev, code, message])

parser = argparse.ArgumentParser(description='Update DNS-o-Matic & OpenDNS with your IP')
parser.add_argument('--config', help='Configure your account details into ddns.yaml')

args = parser.parse_args()

last_ip,r = 'None','None'

try:
    f = open('ddns.yaml', 'r')
except:
    Synlog('err', "0x11800000", "DDNS updater could not start.  No config file")
    raise
        
config = yaml.safe_load(f)
username, password, update_time = config['username'],config['password'],config['update_seconds']

while True:
    try:
        r = requests.get('http://myip.dnsomatic.com/')
    except:
        Synlog('err','0x11800000','DDNS updater could not reach DNS-o-matic')
        raise
    if last_ip != r.text:
        last_ip = r.text
        str = 'https://' + username + ':' + password + '@updates.dnsomatic.com/nic/update?myip=' + r.text + '&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG'
        try:
            r = requests.get(str)
            print r.text
            Synlog('info', "0x11800000", "DDNS Updated to " + last_ip)
        except:
            Synlog('err', "0x11800000", "DDNS updater could not reach DNS-o-matic")
            raise
    else:
        Synlog('info', "0x11800000", "No DDNS Update this time")
    time.sleep(update_time)
    
    
