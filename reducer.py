# Python reducer script
#!/usr/bin/env python3
import sys

current_candidate = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    try:
        candidate, count = line.split('\t')
        count = int(count)
    except ValueError:
        continue

    if current_candidate == candidate:
        current_count += count
    else:
        if current_candidate:
            print(f"{current_candidate}\t{current_count}")
        current_candidate = candidate
        current_count = count

# Output the final candidate total
if current_candidate:
    print(f"{current_candidate}\t{current_count}")
