ps aux |grep chrome|awk '{print $2}'|xargs -i kill {}
/usr/bin/python WC.py