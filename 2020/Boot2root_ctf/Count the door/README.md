# Count the doors
**category: programming**  
**points: 440**

## Description
N = 898399329838283293892392328398239832

There are N doors, all closed. In a nearby cage are N apes.

The first ape is let out, and runs along the doors opening every one. The second ape is then let out, and runs along the doors closing the 2nd, 4th, 6th,… - all the even-numbered doors. The third ape is let out. He attends only to the 3rd, 6th, 9th,… doors (every third door, in other words), closing any that is open and opening any that is closed, and so on. After all N apes have done their work in this way, how many doors are still open.

Enclose the number in b00t2root{}

## Solution
This problem is like the [100 doors challenge](https://rosettacode.org/wiki/100_doors) but with a really large integer. The solution is to count the number of perfect squares up to N as noted [here](https://rosettacode.org/wiki/Talk:100_doors). To get the number of perfect squares, we just have to get the square root of N. We can use this [website](https://www.calculator.net/big-number-calculator.html) to do calculations on big numbers.

**FLAG:** `b00t2root{947839295365139044}`

