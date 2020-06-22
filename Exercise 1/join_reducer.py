#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

# --------------------------------------------------------------------------
# Takes a <title, value> file and it keeps track of the number of listeners
# to titles broadcast by RNE1, showing the title and the total number.  There
# is no need to check the keys (title) because hadoop puts them in order
# (The tuples <title, numListeners> will be placed before the tuples <title, radio>).
# --------------------------------------------------------------------------

prev_title = "  "
titles_to_output = [] # Stores the titles that will be shown on the output
numListeners_to_output = [] # Stores the number of listeners that will be shown on the output
numListeners = 0 # Number of listeners to the current title

for line in sys.stdin:
  line       = line.strip()
  key_value  = line.split('\t')

  # If the input does not have two fields, it is discarded
  if len(key_value) != 2:
    continue

  curr_title  = key_value[0]
  value_in   = key_value[1]

  # Convert value_in (currently a string) to int
  # This makes it possible to distinguish between radio stations where the title is
  # heard and those where the list of number of listeners is heard.
  try:
    value_in = int(value_in)
  except ValueError:
    value_in = value_in

  # If the title is changed, the count of the number of listeners is reset
  if prev_title != curr_title:
    numListeners = 0

  # If the value field is numerical, the number of listeners to that topic is added.
  if type(value_in) is int:
    numListeners += value_in
    # If the value field is a string, if the radio is RNE1, the title is added to the final list.
  elif type(value_in) is str:
    if (value_in == 'RNE1'):
      titles_to_output.append(curr_title)
      numListeners_to_output.append(numListeners)

  prev_title=curr_title


# ---------------------------------------------------------------
# Show the output
# ---------------------------------------------------------------
for i in range(len(titles_to_output)):
  print('{0} {1}'.format(titles_to_output[i],str(numListeners_to_output[i])))