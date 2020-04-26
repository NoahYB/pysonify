# pysonify
Takes 2D csv data and produces a musexml score.
Still a work in progress let me know if you find any bugs.
Currently working with the LilyBloomData
Current paramaters are as follows - Path for the csv you want to convert, how many divisions you want to make 
(more divisions = more diversrity in note placement), Diatonic (enter in false if you dont want the sonifier 
to sample outside of the key of c)

To use (on mac) go to terminal
cd to the folder
type into terminal(without quotations) python3 datasonifier.py path_to_csv divisions_you_want true_or_false

to use the data in the folder copy and paste this into terminal with parameters I know work

python3 datasonifier.py LilyBloomData.csv 20 false

You will need a music score editing software to load the xml into a score

the xml is saved in the folder and titled "your_generated_score.xml"

Things I need to work on:
	getting rid of weird grey rests
	making sure it will work with different types of csv