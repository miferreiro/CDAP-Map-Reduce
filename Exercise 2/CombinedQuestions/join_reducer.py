#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
prev_card = "  "
card_section = {} # Stores the section and the costs for the current payment method
card_sectionComputers = {} # Stores the cards and the costs on the section "Computers"

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

  #Question 1
  # If the tuple belongs to the "Computers" section
  if section == 'Computers':
    # If the card is not in the dictionary, it is added to it, and if it is
    # already there, the cost is added to the accumulated value
    if card_sectionComputers.has_key(curr_card):
      card_sectionComputers[curr_card] += price
    else:
      card_sectionComputers[curr_card] = price


  #Question 2
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

if prev_card != "  ":
  # Show the answer to the question for the last method of payment:
  # For each payment method, which is the section that makes the most sales?
  max_section,max_price = max(card_section.iteritems(), key=lambda x:x[1])
  print('For the payment method "%s", the section that makes the largest amount is "%s" with a value of "%s"' % (prev_card, max_section, str(max_price)) )

  print('-------------------------------------------------------------------')
  print('-------------------------------------------------------------------')

  # Show the answer to the question:
  # What is the most used payment method for the purchase of computers?
  max_card = max(card_sectionComputers.keys())
  print('The most used payment method for the purchase of "Computers":\n%s\t%s' % (max_card, str(card_sectionComputers.get(max_card))) )