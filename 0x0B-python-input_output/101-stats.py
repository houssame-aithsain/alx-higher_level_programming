#!/usr/bin/python3
"""Print statistics from stdin."""


import sys


def print_statistics(total_size, status_codes):
    """Prints the computed statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """Parses a single line and updates the statistics."""
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        file_size = int(parts[-1])
        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
    return total_size, status_codes

def parse_input():
    """Reads stdin line by line and computes statistics."""
    total_size = 0
    status_codes = {}
    line_count = 0
    try:
        for line in sys.stdin:
            total_size, status_codes = parse_line(line.strip(), total_size, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    parse_input()
