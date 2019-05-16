# Apartado 1: cálculo del sentimiento de un conjunto de tweets

def total_feelings(tweets_file, feelings_file):

	import json
	with open(feelings_file) as sentimientos:
		feelings = {}
		for line in sentimientos:
			word, value = line.split('\t')
			feelings[word] = int(value)

	with open(tweets_file) as file:
		tweets = []
		for line in file:
			complete_tweet = json.loads(line)
			
			if 'text' in complete_tweet.keys():
				tweets.append(str(complete_tweet['text']))

	total_feelings = 0
	for tweet in tweets:
		split_tweet_lower = tweet.lower().split(' ')
		for word in split_tweet_lower:
			if word in feelings.keys():
				total_feelings += feelings[word]
		print(f'The following tweet: "{tweet}" has a feeling value of: {total_feelings}\n')
		total_feelings = 0

total_feelings('salida_tweets.txt', 'Sentimientos.txt')



# Apartado 2: asignación de valores de sentimiento a palabras no registradas (primera forma)

def assign_val(tweets_file, feelings_file):

	import json
	with open(feelings_file) as sentimientos:
		feelings = {}
		for line in sentimientos:
			word, value = line.split('\t')
			feelings[word] = int(value)

	with open(tweets_file) as file:
		tweets = []
		for line in file:
			complete_tweet = json.loads(line)
			
			if 'text' in complete_tweet.keys():
				tweets.append(str(complete_tweet['text']))

	total_feelings = 0
	for tweet in tweets:
		split_tweet_lower = tweet.lower().split(' ')
		print(f'Words without a feeling value in tweet "{tweet}":')
		for word in split_tweet_lower:
			if word in feelings.keys():
					total_feelings += feelings[word]
		for word in split_tweet_lower:
			if word not in feelings.keys():
				print(f'{word}: {total_feelings}')
		print('\n')
		total_feelings = 0

assign_val('salida_tweets.txt', 'Sentimientos.txt')


# Apartado 2: asignación de valores de sentimiento a palabras no registradas (segunda forma)

def assign_avg(tweets_file, feelings_file):

	import json
	with open(feelings_file) as sentimientos:
		feelings = {}
		for line in sentimientos:
			word, value = line.split('\t')
			feelings[word] = int(value)

	with open(tweets_file) as file:
		tweets = []
		for line in file:
			complete_tweet = json.loads(line)
			
			if 'text' in complete_tweet.keys():
				tweets.append(str(complete_tweet['text']))

	total_feelings = 0
	for tweet in tweets:
		split_tweet_lower = tweet.lower().split(' ')
		print(f'Words without a feeling value in tweet "{tweet}":')
		for word in split_tweet_lower:
			if word in feelings.keys():
					total_feelings += feelings[word]
		for word in split_tweet_lower:
			if word not in feelings.keys():
				try:
					print(f'{word}: {round(len(split_tweet_lower)/total_feelings, 2)}')
				except:
					print(f'{word}: None')
		print('\n')
		total_feelings = 0

assign_avg('salida_tweets.txt', 'Sentimientos.txt')