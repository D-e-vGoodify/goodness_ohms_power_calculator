# Project title
Ohm's Law and Power Calculator

## What it does
The user chooses what to find (voltage, current, resistance or power), enters the known values and gets the answer with units.
While also getting an analysis, history and report
The program repeats until the user quits.


## How to run it
Install Python 3, then run: python goodify_ohms_power_calculator.py

## Sample output
Welcome to the Goodify Ohms Law & Power Calculator

What to find?
1. Voltage
2. Current
3. Resistance
4. Power
Reply: 1

from Power or Ohms Law?
1. Power(P=IV)
2. Ohms(V=IR)
Reply: 2

Resistance: 2
Current: 4
Voltage is 8.0V
....

## My own twist
I added a response section that after every calculation, gives features of current electrical value result
E.g If Voltage < 1.0, it responds with: ℹ️  Very low voltage. Seen in analog sensor signals or minor component drops. While also asking if changes to the same calculated value, and if so goes back for the user to enter new readings
Also, a history section at the end with proper analysis of Results. Showing;
1. linear trends of resluting values(increasing or decreasing)
2. Checks for linear-progression in resulting values

## What I learned
I learned quite a few new tricks:
Firstly, I learnt more on how to query and modify a calculator{} in addition to a list[], how to iterate through items in it and check individual object values
Secondly, I also learnt more of error management and how to handles errors to respond with a specific error message rather than the python script crashing
Also, I learnt how to modify the messages printed in the terminal, making the layout more clean E.g print("=" * 10), to act as a section separator or title companion
Lastly, I learnt more about code arrangement and syntax, especially in the context of python, since I'm already familiar with JavaScript. I was able to understand more on python syntax, how to use it properly, and how python sees and reads each type and block of code

## Author
Adekunle Goodness, ND1 Mechatronics Engineering Engineering, YabaTech.
