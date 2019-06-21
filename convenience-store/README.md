# Convenience Store

Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item. Change will always be represented in the following order: quarters, dimes, nickels, pennies.

To illustrate: change_enough([25, 20, 5, 0], 4.25) should yield true, since having 25 quarters, 20 dimes, 5 nickels and 1 penny gives you 6.25 + 2 + .25 + 0 = 8.50.

So write a function named "change_enough" that takes an array of four numbers (representing the change), and a number (representing the amount needed), and you return a true or false, depending on whether there is enough change.

Examples:
```
change_enough([2, 100, 0, 0], 14.11) ➞ false

change_enough([0, 0, 20, 5], 0.75) ➞ true

change_enough([30, 40, 20, 5], 12.55) ➞ true

change_enough([10, 0, 0, 50], 3.85) ➞ false

change_enough([1, 0, 5, 219], 19.99) ➞ false
```

Notes:
* quarter: 25 cents / $0.25
* dime: 10 cents / $0.10
* nickel: 5 cents / $0.05
* penny: 1 cent / $0.01
