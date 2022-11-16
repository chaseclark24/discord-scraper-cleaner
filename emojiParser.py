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
			if message['reactions']:
				for reaction in message['reactions']:
					content = message['content'].replace("\n", "")
					content = content.replace(",", "")
					author = message['author']['name'].replace(",", "")
					if reaction['emoji']['name'] is not None:
						str1 = message['timestamp'] + "," + content + "," + author + "," + (reaction['emoji']['name'])  + "," + reaction['emoji']['imageUrl'] + "," + str(reaction['count']) + '\n'

					with io.open('C:\\Users\\Chase\\Downloads\\id disc data\\emojiData.txt','a',encoding='utf8') as f:
						f.write(str1)
        
	else:
		continue