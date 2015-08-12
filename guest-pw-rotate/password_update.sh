#!/bin/sh
# this script sets a random guest wifi password for the 
# BloomLab Guests network from a list of passwords contained
# within passwords.txt

# runs on ddwrt within the wireless router itself

# picking a random password from a text file using the limited
# ddwrt commands is hard
n=$(</dev/urandom tr -dc 0-9 | dd bs=5 count=1)
j=$(echo $n | sed 's/^0*//')
m=$((j % 350))
wpa_password=`sed -n "${m}p" < /jffs/guest-pwrotate/passwords.txt` 

# write the password to the on-board webserver so we can
# query it remotely at http://<router>:81/cur_password.txt
# (must make sure the webserver is on in ddwrt settings)
echo $wpa_password
echo $wpa_password > /jffs/www/cur_password.txt

# the next few lines change the NVRAM variable of your wireless 
# interface and commit it to memory 
# in our case specifically the guest wifi is wl0.1
nvram unset wl0.1_wpa_psk 
sleep 5 
nvram set wl0.1_wpa_psk=$wpa_password 
nvram commit 

# it's hard to actually apply the changes correctly without
# rebooting, so we take the easy way out and just make sure
# it only happens at like 4am so no one is annoyed
sleep 5
/sbin/reboot 
