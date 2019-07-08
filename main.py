#! /usr/bin/env python

import wmi

c = wmi.WMI()
countP = 0
wql = "SELECT IPAddress FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = 'True'"
process_watcher = c.Win32_Process.watch_for("operation")

print ('OS is: {0}'.format(c.Win32_OperatingSystem() [0].Caption))
print ('Disk freespace [0] - total {1}'.format(c.Win32_LogicalDisk() [0].Freespace,c.Win32_LogicalDisk()[0].Size))
print ('Total Memory: {0}'.format(c.Win32_ComputerSystem() [0].TotalPhysicalMemory))

print('Local IP address: {0}'. format(''.join(c.query(wql)[0].IPAddress)))

while countP < 5:
	countP += 1
	current_process = process_watcher()
	print(current_process.Caption)
