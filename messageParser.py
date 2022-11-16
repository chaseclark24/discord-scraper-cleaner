import json
import os
import io

directory='C:\\Users\\Chase\\Downloads\\id disc data'
for filename in os.listdir(directory):
	if filename.endswith(".json"):
		print(filename)
		filePath=os.path.join(directory, filename)
		
		with open(filePath,"r", encoding='utf-8') as json_file:
			data = json.load(json_file)
	
		for message in data['messages']:
			str1 = message['timestamp'] + "|###x|" + data['channel']['name'] + "|###x|" + message['id']  + "|###x|" + message['author']['name'] + "|###x|" + message['content'].replace("\n", "") + '\n'
			with io.open('C:\\Users\\Chase\\Downloads\\id disc data\\messageData.txt','a',encoding='utf8') as f:
				f.write(str1)
		   
	else:
		continue




