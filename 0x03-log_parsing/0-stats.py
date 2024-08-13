#!/usr/bin/python3
"""Log parsing """

import sys
import re

def print_stats(total_size, status_counts):
    """Print statistics"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    """Main function"""
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    log_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

    try:
        for line in sys.stdin:
            match = log_pattern.match(line)
            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
                
                if status_code in status_counts:
                    status_counts[status_code] += 1
                
                total_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
            
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
