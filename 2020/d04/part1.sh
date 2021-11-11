#!/bin/bash
perl -p -e 's/(.+)\n/\1 /g' < input | grep byr: | grep iyr: | grep eyr: | grep hgt: | grep hcl: | grep ecl: | grep pid: | wc -l
