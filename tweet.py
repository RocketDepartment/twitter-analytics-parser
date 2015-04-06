class Tweet(object):

	def __init__(self, id, link, text, time, impress, engage, engage_rate, retweets, replies, favs):

		self._id = id
		self._link = link
		self._text = text
		self._time = time
		self._impress = impress
		self._engage = engage
		self._engage_rate = engage_rate
		self._retweets = retweets
		self._replies = replies
		self._favs = favs

	def __repr__(self):
		return '{}\n {}\n {}\n RT: {}, Replies: {}, Favs: {}\n'.format(self._link,
								  								  self._text,
								  								  self._time,
								  								  self._retweets,
								  								  self._replies,
								  								  self._favs)

	def get_retweets(self):
		return self._retweets

	def get_replies(self):
		return self._replies

	def get_favs(self):
		return self._favs