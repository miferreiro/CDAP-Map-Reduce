# Starting on Map/reduce

These three exercises were made in the subject of "Computación Distribuída e de Altas Prestacións" in the Master Degree of Computer Engineering of the University of Vigo in 2020

### Exercise 1

This exercise is composed of a series of files containing audience data on topics broadcast on radio stations:
- The join_cad?.txt files consist of a list of music tracks and, for each track, the radio station where it was broadcast.
- The join_num?.txt files also contain playlists and, for each track, the number of listeners it has had.

The objective of this section is to implement a map/reduce task that provides an answer to the following question:

*What has been the total number of listeners (in all radio stations) to the topics that have been broadcast by RNE1?*

NOTE 1: the mapper for this task is simple. Once implemented, its operation can be checked in the terminal:

`$ cat join_*.txt | ./join_mapper.py | sort`

NOTE 2: the reducer will be a little more complex, but we must not lose sight of the fact that at its entry the data will be ordered alphabetically.

### Exercise 2

In order to do this exercise, the file containing information on the sales made in a chain of department stores in January 2012 is used as a starting point. Each line of the purchases.txt file contains the following fields: date, time, city, section, amount, means of payment.

We ask that you implement map/reduce programs that will allow you to answer the following questions:
- What is the most widely used payment method for the purchase of computers?
- For each means of payment, which section makes the most sales?

A small pdf document should be attached briefly justifying the decision taken on the content of the <key,value> fields and briefly explaining the implementation and results.