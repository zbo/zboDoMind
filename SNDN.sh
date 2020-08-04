git pull
ps aux |grep chrome|awk '{print $2}'|xargs -i kill {}
/usr/bin/python SN.py
/usr/bin/python DN.py
