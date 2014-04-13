#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

#1. The files and directories to be backed up are specified in a list

source = ['/home/wh/.bashrc','/etc/init.d']

#2. backup directory 

target_dir = '/mnt/G/backup/'

#3. The files are backed up into a zip file
#4. The name of the zip archive is the current date and time

target = target_dir + time.strftime('%Y%M%d%H%M%S') + '.zip'

#5. use zip command to put the files in a zip archive

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# run 

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed'
