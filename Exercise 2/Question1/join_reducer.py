#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

# --------------------------------------------------------------------------
# Takes a <card, price> file and it keeps track of the number of the expenditure
# made with each card in the section "Computers" and calculates which method of
# payment is most used. There is no need to check the keys (card) because hadoop
# puts them in order and the tuples containing the "Computers" section have been
# collected in the mapper.
# --------------------------------------------------------------------------
prev_card = "  "
curr_card = "  "
card_sectionComputers = {} # Stores the cards and the costs on the section "Computers"

for line in sys.stdin:
  line       = line.strip()
  key_value  = line.split('\t')

  # If the input does not have two fields, it is discarded
  if len(key_value) != 2:
    continue

  curr_card = key_value[0]
  price = key_value[1]

  # Convert price (currently a string) to float
  try:
    price = float(price)
  except ValueError:
    continue

  # If the card is not in the dictionary, it is added to it, and if it is
  # already there, the cost is added to the accumulated value
  if card_sectionComputers.has_key(curr_card):
    card_sectionComputers[curr_card] += price
  else:
    card_sectionComputers[curr_card] = price

  prev_card = curr_card


# Show the answer to the question:
# What is the most used payment method for the purchase of computers?
if prev_card != "  ":
  max_card = max(card_sectionComputers.keys())
  print('The most used payment method for the purchase of "Computers":\n%s\t%s' % (max_card, str(card_sectionComputers.get(max_card))) )