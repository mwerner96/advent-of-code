#!/bin/bash
tr FBLR 0101 < input | sort | python3 findseat.py
