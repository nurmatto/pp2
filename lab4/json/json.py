# who's gonna carry the boats and the logs?

import json

with open('sample-data.json') as f:
	information = json.load(f)
	print('''Interface Status
	================================================================================
	DN                                                 Description           Speed    MTU  
	-------------------------------------------------- --------------------  ------  ------''')
	my_data = information['imdata']
	for things in imdata:
		
		my_item = item['l1PhysIf']
		atrs =  my_item['attributes']
		dnn = atrs['dn']
		speed = atrs['speed']
		mtu = atrs['mtu']
		out = ''
		
		if len(dnn)==42:
			out += dn + '                              ' + speed + '   ' + mtu
			
		else:
			out += dn + '                              ' + speed + '   ' + mtu
			
		print(out)
		