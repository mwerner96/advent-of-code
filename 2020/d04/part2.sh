#!/bin/bash
perl -p -e 's/(.+)\n/\1 /g' < input | grep -E 'byr:(19[2-9][0-9]|200[0-2]) ' | grep -E 'iyr:20(1[0-9]|20) ' | grep -E 'eyr:20(2[0-9]|30) ' | grep -E 'hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)' | grep -E 'hcl:#([0-9]|[a-f]){6} ' | grep -E 'ecl:(amb|blu|brn|gry|grn|hzl|oth) ' | grep -E 'pid:[0-9]{9} ' | wc -l
