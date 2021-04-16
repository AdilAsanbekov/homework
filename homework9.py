import json
import datetime
import time

data = [
	"id,username,email,register_at".split(','),
	"1,admin,admin@example.com".split(','),
	"2,first_user,first_user@example.com".split(','),
	"3,second_user,second_user@example.com".split(',')
]

with open("data_file2.json", "w") as file:
	json.dump(data, file)
	file.close()

with open("data_file2.json", "r") as file:
	data = json.load(file)
	print(data)

print(time.ctime(time.time()))