3) db.tweets.aggregate([
    {$group:{_id:"$user.screen_name", "total_tweets": {$sum: 1}}},
		   {$sort: {"total_tweets": -1}}
]).pretty()

4) 

db.tweets.aggregate([
	{$group: {_id: "$place.name", "tweet_count": {$sum: 1}} },
		{$sort: {"tweet_count": -1}}
]).pretty()

5) 

db.tweets.aggregate([
		{$group: {_id: "$in_reply_to_screen_name", "num_replies": {$sum: 1}}},
			{$sort: {"num_replies": -1}}
])

6)

db.tweets.aggregate([
	{$unwind: "$entities.hashtags"},
		{$group: {_id: "$user.screen_name", "num_hashtags": {$sum: 1} }},
			{$sort: {"num_hashtags": -1}}
]).pretty()