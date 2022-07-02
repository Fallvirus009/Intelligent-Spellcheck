# Intelligent-Spellcheck
An intelligent spellcheck function built in python for use in any scenario. Free for use and integration but proper credits to Daniel Elkoni and this README included somewhere in the final repository.
## Use Cases
This code can be used in many applications. Including both non and case-sensitive testing applications, to intelligently check user input and accept it even when the user might be innacurate with their spelling, word processing, autocorrect (if integrated with a word bank[possible future integration]), and many more user inpute processing situations.
## V1.0.0
Can check a word(user input) against a key word and determine if they were meant to be the same word, example: SpellCheck(input, key)
## V1.1.0
Can take a degree of accuracy to check the similarity between the key and input. This number is expressed in whole number percent, example: SpellCheck(input, key, 70)
## V1.2.0
Can now accept a case sensitive or non case sensitive boolean, example: SpellCheck(WORD, word, 70, true). This example would find no similarities between the two words as the lower and uppercase letters do not match and the operation is specified to be case sensitive
## V.2.1
Now has "slippage tolerance", if an accidental space is inserted into the phrase by a user, the function recognizes this and the interal key is shifted with said space. This shift allows the user entered phrase to be compared character by character with the key and to allow such mistakes to possibly be made by an end user.
### Slippage Tolerance
Phrase: "wha t" <br />
Key: "what" <br />
"w" == "w", "h" == "h", "a" == "a", " " != ("t" != " ") <br />
At this point in the process, the computer recognizes a possible mistaken space by a user and in this case an additional space would be inserted into the "t"'s spot on a secondary copy of the key. This all allows the computer to see that the words are an exact match but the user has accidentally inserted a space where it does not belong.
