#!/bin/bash
tr FBLR 0101 < input | sort | tail -1 | python3 -c "print(int(input(),2))"
