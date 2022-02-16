function myHashtagMapper() {
    //The mapper function is called with each document, which has the special name 'this'
    //Emit a key-value pair for each hashtag with a 1 to count occurrences:
	for (hashtag of this.entities.hashtags) {
		//Hashtags are contained in the "text" field of the hashtags object
		emit(hashtag.text, 1);
	}

}

function myHashtagReducer(key, values) {
    //The reducer is called once for each key, and is passed an array
    //containing all values corresponding to that key.
    // This function will simply sum the 1 associated with each key to count num of occurrences
    return Array.sum( values );
}

db.tweets.mapReduce(myHashtagMapper, myHashtagReducer, { query: {}, out: "mroutput" })
db.mroutput.aggregate({$sort: {value: -1}})

// END OF MY FUNCTION