import json
from pprint import pprint
from collections import namedtuple
def main():
	with open('blood-die.json') as json_data:

		data = json.load(json_data)
		Landen=namedtuple('Landen', 'land classficaties')
		for line in data:
			line[3]=line[3].replace('\n',',')
			bloed=line[2].split(',')
			sterven=line[3].split(',')
			#goedelanden=[Landen(line[0],line[1]) for i in bloed if i in sterven] als ik dit probeer krijg ik lege lijsten terug, wat doe ik verkeerd?
			for i in bloed:
				if i in sterven:
					goedelanden=Landen(line[0],line[1])
					print(goedelanden)
		
		
		json_data.close()
		
main()
