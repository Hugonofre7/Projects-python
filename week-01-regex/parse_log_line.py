import re

def parse_log_line(line):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|WARN|INFO|DEBUG) \[(.+?)\] (.+)'
    
    match = re.match(pattern, line)
    
    if match:
        return {
            'timestamp': match.group(1),
            'level':     match.group(2),
            'service':   match.group(3),
            'message':   match.group(4)
        }
    
    return None

line_ok  = "2024-01-15 14:32:01 ERROR [auth-service] Login failed for user: admin"
line_bad = "--- system startup ---"

print(parse_log_line(line_ok))
print(parse_log_line(line_bad))