#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

# ---------------------------------------------------------------------------
# This mapper accepts <title, radio> or <title, numListeners> values and makes
# an append of all elements
# ---------------------------------------------------------------------------

for line in sys.stdin:
  line       = line.strip()
  key_value  = line.split(",")
  # If the input does not have two fields, it is discarded
  if len(key_value) == 2:
    key_in     = key_value[0]
    value_in   = key_value[1]
    print( '%s\t%s' % (key_in, value_in) )
  else:
    continue
