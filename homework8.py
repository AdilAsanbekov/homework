import csv

def csv_writer(data, path):
	with open(path, "w") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		for line in data:
			writer.writerow(line)

data = [
	"id,username,email,ip_address""1,root,root@example.com,192.168.0.1".split(','),
	"2,admin,admin@example.com,192.168.0.2".split(','),
	"3,test_user,test_user@example.com,192.168.0.3".split(','),
	"4,second_user,second_user@example.com,192.168.0.4".split(',')
]

	# for line in reader:
	# 	print(line)
	# 	print("--------------")
	# 	print(line["id,username,email,ip_address""1,root,root@example.com,192.168.0.1"])
	# 	print(line["2,admin,admin@example.com,192.168.0.2"])
	# 	print(line["3,test_user,test_user@example.com,192.168.0.3"])
	# 	print(line["4,second_user,second_user@example.com,192.168.0.4"])
	# 	print("--------------")

path = "data2.csv"
csv_writer(data, path)