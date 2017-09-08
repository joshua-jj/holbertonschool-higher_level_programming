#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
try:
    for i, line in enumerate(sys.stdin):
        tokens = line.split()
        status_tally[tokens[-2]] += 1
        file_size += int(tokens[-1])
        if (i + 1) % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key in status_codes:
                if status_tally[key]:
                    print("{:s}: {:d}".format(key, status_tally[key]))
except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key in status_codes:
        if status_tally[key]:
            print("{:s}: {:d}".format(key, status_tally[key]))
