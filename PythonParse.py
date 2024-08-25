import re


#writing the function 
def parse_log(log_file):
    with open(log_file, 'r') as f:
        for line in f:
            if re.search(r'failed|error|unauthorized|malicious', line, re.IGNORECASE):
                print(f"Suspicious Activity: {line}")



# storing the variable 
log_file = 'system_logs.log'

#executing
parse_log(log_file)

