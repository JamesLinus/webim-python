
webim-python
============

webim python client

usage
=====

	import webim 

	endpoint = webim.Endpoint("uid1", "user1")

	c = webim.Client(endpoint, 'domain', 'apikey', host='127.0.0.1', port = 8000)

	c.online(['uid1','uid2','uid3'], ['grp1','grp2','grp3'])

	c.offline()
