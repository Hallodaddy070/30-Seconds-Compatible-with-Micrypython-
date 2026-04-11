# 30-Seconds-Compatible-with-Micrypython (It is fixed)-
30 seconds is a game where there are teams of 2 players. One person gets 5 random words and has to describe them to their teammate. Their teammate has to guess what word they are describing. After 30 seconds the amount of words your teammate guessed become points. After typing your points you give the calculator to the next team. The next time it is your turn the roles switch. First to 30 wins. Made for fx-CG50, probably functional in other graphing calculators with Micropython.

v2

There were some duplicate words that are now removed, and the word lists get shuffled (extra randomness) when you start the game now. It will stop the same words appearing all the time.

WARNING:
-
Because there is no time module on the fx-CG50, I used busy-wait loops to keep track of the time. These may use alot of battery, but how bad it is is not something I know. This was made for the fx-CG50 so the wait loop probably won't be 30 seconds on other calculators. If you want to change the time so it's 30 seconds on your calculator change n. n = 137500 for ~ 30 seconds on the fx-CG50. You have to experiment with it a little bit so it is right on your non fx-CG50 calculator.

# How to download
After connecting your fx-CG50, paste the file (the one with the highest number is the newest one) beside the other files (not inside any folder, you can paste it inside a folder in the Python app but this is the fastest way.). When you open Python you will see it there, click run to play.

