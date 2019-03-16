# Wordsearch
A fun little exercise in Python.

Search a randomly generated board of letters for words. Valid search
directions include horizontal, vertical, diagonal (left to right), 
diagonal (right to left) and the reverse for each direction. 

The goal is to search a 15x15 board in under a half second. 

## Search
When a board is created, a list of strings is created to search. Each string 
is a valid search direction. Currently generation of the diagonal search strings
is a bit confusing and needs to be re-written to use a proper algorithm. 

The actual search algorithm walks the list of words, peering into each search string
to locate an instance of it. 

### Enhancement idea
Pre-process the dictionary. If there are words that are contained in a larger word, 
order those so that they aren't searched for. 

Example: if 'Robert' is found, then 'Rob' would be found as well. 
