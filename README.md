All you have to do is find your favorite artist, open inspect elements, go to network, select XHR, vote then you will see the data sent by the vote

example:
{"action": "media_poll_vote", "poll_id": "10523173", "post_id": 884664, "answer_id": "48703415"}


Take that and put it into the program on line 3 where data is.

Now you can automate voting for the xxl freshman

I created 2 version vote_once.py (runs once) and vote_infinite.py (loops infinitely)
When done with vote_infinite.py press control + c to end the program