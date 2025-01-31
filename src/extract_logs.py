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
