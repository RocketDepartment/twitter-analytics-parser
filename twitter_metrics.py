import csv
from tweet import Tweet

tweets = []
top_count = 10
filename = 'tweet_activity_metrics.csv'

def main():

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		reader = csv.reader(csvfile)

		for row in reader:
			t = Tweet( row[0], row[1], row[2], row[3], row[4], row[5], row[6], int(row[7]), int(row[8]), int(row[9]) )
			tweets.append(t)

			top_retweets = sorted(tweets, key = lambda t: t.get_retweets(), reverse=True)
			top_replies = sorted(tweets, key = lambda t: t.get_replies(), reverse=True)
			top_favs = sorted(tweets, key = lambda t: t.get_favs(), reverse=True)

	data = [top_retweets, top_replies, top_favs]

	print "Welcome to the Twitter Metrics Parser"
	print "1) Top RTs"
	print "2) Top Replies"
	print "3) Top Favs"
	print ""
	selection = int(raw_input("Please select what data you are interested in: "))
	print ""

	while selection > len(data) or selection < 1:
		print "*** That is not a valid selection ****"
		selection = int(raw_input("Please select what data you are interested in: "))

	lst = data[ selection - 1 ]
	for i in range(top_count):
		print "--- #" + str(i+1) + " ---"
		print lst[i]

if __name__ == "__main__":
	main()