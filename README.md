# Lexeme Project Steps

## 1. Pass full text from .txt file into clean_seperators function
* this function removes all seperators and returns a list of size 2
    * index 0 containing all seperators
    * index 1 containing text without seperators

## 2. Pass text without seperators into clean_quotes function
* this function removes all strings and returns a list of size 2
    * index 0 contains all strings
    * index 1 contains text without strings ****AND**** seperators

## 3. Pass text without strings and seperators into clean_operators function
* this function removes all operators and returns a list of size 2
    * index 0 contains all operators
    * index 1 contains text without operators ****AND**** strings ****AND**** seperators 

## 4. Pass text without operators, strings, and seperators into clean_keywords function
* this function removes all keywords and returns a list of size 2
    * index 0 contains all strings
    * index 1 contains text without keywords ****AND**** operators ****AND**** strings ****AND**** seperators 

## 5. Pass text without keywords, operators, strings, and seperators into clean_nums_and_indenifiers function
* this function removes all identifiers and returns a list of size 2
    * index 0 contains all identifiers
    * index 1 contains text without identifiers ****AND**** keywords ****AND**** operators ****AND**** strings ****AND**** seperators 

## 6. Main Driver Code
* Hash each token to values in .txt file and print out
