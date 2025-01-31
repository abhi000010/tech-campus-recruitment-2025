# Discussion.md

## Solutions Considered:
I explored the following approaches to extract logs from a given file based on a specific date:

- Approach 1: Looping through the entire log file and checking each line for the specified date. This approach could be slow for large log files since it involves reading each line sequentially.
- Approach 2: Using `mmap` (memory-mapped file objects) to read the file efficiently, especially when the file size is large. This approach allows for more efficient memory use and faster line-by-line access.

I decided to proceed with **Approach 2** because it offers better performance when dealing with large log files. Memory mapping allows the system to handle file reading more efficiently by loading only the necessary portions of the file into memory. This reduces the overhead and speeds up the reading process, which is important for large logs.

## Source Code for Approach 2 -
```
import sys
import os
import mmap

def extract_logs(log_file, date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")

    try:
        with open(log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            with mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                for line in iter(mm.readline, b""):
                    if line.decode("utf-8").startswith(date):
                        outfile.write(line.decode("utf-8"))
        
        print(f"Logs for {date} have been saved in {output_file}")
    except FileNotFoundError:
        print("Error: Log file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date_arg = sys.argv[1]
    log_filename = "logs_2024.log"  
    extract_logs(log_filename, date_arg)

```
## Final Solution Summary:
I chose to use `mmap` for efficient file reading to extract logs based on a specific date. The solution reads through the log file line by line and checks if the line starts with the specified date. If a match is found, it writes that line to a new file. I decided to implement the solution in Python due to its ease of use, file handling capabilities, and the built-in support for `mmap`.

## Steps to Run:
1. **Download the files in src folder**
2. **Download the log file**
3. ** In the IDE terminal run ```python extract_logs.py 2024-12-01``` to get the output in output folder in the IDE output folder**    
