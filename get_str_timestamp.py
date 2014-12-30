def get_str_timestamp():
	import time, datetime
	ts = time.time()
	ts_str = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	return ts_str