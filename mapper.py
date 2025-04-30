# Python mapper script
#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    parts = line.split('|')
    
    # Ensure we have exactly two parts: [location, candidate]
    if len(parts) == 2:
        candidate = parts[1]
        print(f"{candidate}\t1")
