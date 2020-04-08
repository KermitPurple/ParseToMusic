# Parsing Text to music

I'm sure that this has been done before but, I am trying to create a program that plays sound based on the specifc notes portrayed in a text file

## Syntax

They syntax is pretty simple. A peice is made up of notes and rests, these are seperated by spaces. A rest is 2 characters ling and only constists of the letter r and followed be the appropriate time. Notes are 3 characters long and consist of a note letter, an octive, and a time. The first character is Indicates the note letter (Such as C or D), the second indicates the octive (0-8), and the third indicates the note duration. 'w' for whole note, 'h' for half note, 'q' for quarter note, 'e' for eighth note, and 's' for sixteenth note. A note could look like 'C4e' and a rest would look like 'r3', without the quotes of course. Capitals matter because the way you indicate a flat is by making the first character lowercase. There is no sharp implimented. An example is already in the repo. It's called mego.txt and yes it is exactly what you think.
