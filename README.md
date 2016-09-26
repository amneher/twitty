# twitty
a small cli twitter client written in python3.


## syntax
this client has a git-like syntax. 
example:
- twitty push -m "This is a tweet."
- twitty (--authenticate or -a) 
	- Enter username: user
	- Enter passphrase: oranges
	- displays list of helpful options.
- twitty (--search or -s) search_criteria
	- append # for searching hashtags, @ for searching users.
