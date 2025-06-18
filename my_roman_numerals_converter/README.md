# Welcome to My Roman Numerals Converter
***

## Task
The challenge in this project is to convert inputed integers into corresponding roman numerals. 
## Description
I've solved this problem by creating a dictionary that contanins the integer values that correspond to roman numeral symbols.
The function iterates through the dictionary checking how many times each roman numera can be sbtracted form the input number.
The algorithm isterates the dictionary startgin from the largest value to the samllest
For each roman numeral, the fucntion checks how many times the riman numeral fits into the given number, appends the apppriate symbol to the output string
and then subtracts the corresponding value from hte number



## Installation
No special installation is needed for this project. You just need to have Python installed.

## Usage
Summary of steps:
1- Repeatedly subtratic the roman numeral values from the input number
2 - append the roman numeral symbos to a result string at each subtration
3 - once the input number becomes zero, the function returns the roman numeral string

For example, if you input 2022, the function will do the following:

2022 is greater than 1000, so it will append "M" and subtract 1000 from the number.
Now the number is 1022, and again it will subtract 1000, append another "M".
Now the number is 22.

Since 22 is less than 1000, it moves on to the next largest value, which is 10.
22 is greater than or equal to 10, so it appends "X" and subtracts 10 from the number.
Now the number is 12.

It checks again, and since 12 is still greater than or equal to 10, it appends another "X" and subtracts another 10.
Now the number is 2.

Next, it moves to the value 1.
2 is greater than or equal to 1, so it appends "I" and subtracts 1 from the number.
Now the number is 1.

It appends another "I" and subtracts 1 again.
Now the number is 0.

Since the number is now zero, the process stops, and the Roman numeral representation is complete.

The final result is "MMXXII".

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
