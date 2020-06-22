#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

# ---------------------------------------------------------------------------
# This mapper accepts <card, price> values and makes an append of all elements
# ---------------------------------------------------------------------------

for line in sys.stdin:
  line       = line.strip()
  key_value  = line.split("\t")
  # If the input does not have six fields or the section isn't Computers, it is discarded
  if len(key_value) == 6 and key_value[3] == 'Computers':
    #<card, price>
    print( '%s\t%s' % (key_value[5], key_value[4]) )
  else:
    continue
