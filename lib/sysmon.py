#!/usr/bin/python3


import psutil
import urllib.request

class sysmon:

	@staticmethod
	def ram_usage():
		return psutil.virtual_memory().percent

	@staticmethod
	def cpu_usage():
		return psutil.cpu_percent()

	@staticmethod
	def cpu_core_usage():
		return psutil.cpu_percent(percpu=True)

	@staticmethod
	def cpu_temp():
		with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
			temp = float(f.read()) / 1000.0

		return temp

	@staticmethod
	def check_connection(url):
		try:
			urllib.request.urlopen(url)
			return True
		
		except:
			return False

	
	@staticmethod
	def get_connections():

		data = []

		if_addrs = psutil.net_if_addrs()

		for interface_name, interface_addresses in if_addrs.items():
			for address in interface_addresses:
				if str(address.family) == 'AddressFamily.AF_INET':
					data.append([interface_name, address.address])


		return data	


	@staticmethod
	def get_partitions():
		
		data = []

		partitions = psutil.disk_partitions()

		for partition in partitions:
			
			partition_usage = psutil.disk_usage(partition.mountpoint).percent

			data.append([partition.device, partition.mountpoint, partition_usage])

		
		return data
