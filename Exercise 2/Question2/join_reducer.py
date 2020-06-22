#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

# --------------------------------------------------------------------------
# Takes a <card, section price> file and it keeps track of which section makes
# the most sales by payment method. There is no need to check the keys (card)
# because hadoop puts them in order.
# --------------------------------------------------------------------------
prev_card = "  "
card_section = {} # Stores the section and the costs for the current payment method

for line in sys.stdin:
  line       = line.strip()
  key_value  = line.split('\t')

  # If the input does not have three fields, it is discarded
  if len(key_value) != 3:
    continue

  curr_card   = key_value[0]
  section = key_value[1]
  price = key_value[2]

  # Convert price (currently a string) to float
  try:
    price = float(price)
  except ValueError:
    continue

  # Show the answer to the question when the method of payment is changed:
  # For each payment method, which is the section that makes the most sales?
  if prev_card != "  " and prev_card != curr_card:
    max_section,max_price = max(card_section.iteritems(), key=lambda x:x[1])
    card_section = {}
    print('For the payment method "%s", the section that makes the largest amount is "%s" with a value of "%s"' % (prev_card, max_section, str(max_price)) )

  # If the section is not in the dictionary, it is added to it, and if it is
  # already there, the cost is added to the accumulated value
  if card_section.has_key(section):
    card_section[section] += price
  else:
    card_section[section] = price

  prev_card=curr_card


# Show the answer to the question for the last method of payment:
# For each payment method, which is the section that makes the most sales?
if prev_card != "  ":
  max_section,max_price = max(card_section.iteritems(), key=lambda x:x[1])
  print('For the payment method "%s", the section that makes the largest amount is "%s" with a value of "%s"' % (prev_card, max_section, str(max_price)) )
