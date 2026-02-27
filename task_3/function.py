from collections import Counter
from pathlib import Path

def parse_log_file(line: str) -> dict:

    """
    Parse a single log line into dictionary components.
    
    Expected format: "YYYY-MM-DD HH:MM:SS LEVEL Message"
    
    Args:
        line: Single log line string
        
    Returns:
        dict: {'date': str, 'time': str, 'level': str, 'message': str}
    """
    date, time, level, message = line.split(" ", 3)
    return {'date': date, 'time': time, 'level': level, 'message': message}

def load_logs(file_path: str) -> list:

    """
    Load and parse log file.
    
    Validates file extension (.log) and checks if file is not empty.
    
    Args:
        file_path: Path to the log file
        
    Returns:
        list: List of parsed log dictionaries, or None if error/empty
    """
    file_path = Path(file_path)

    # Validate file extension
    if file_path.suffix.lower() != '.log':
        print(f'Error: "{file_path.name}" must have ".log" extension')
        return []
    else:
        # Read and parse log file
        with open(file_path, 'r', encoding='utf-8' ) as file:
            logs = [parse_log_file(line.strip()) for line in file.readlines()]
        
        # Check if file is empty
        if not logs:
            print("Warning: log file is empty")
            return None
            
        return logs

def filter_logs_by_level(logs: list, level: str) -> list:

    """
    Filter logs by specified level.
    
    Args:
        logs: List of log dictionaries
        level: Log level to filter by (case-insensitive)
        
    Returns:
        list: Formatted log strings matching the level, or empty list if invalid level
    """
    arg_list = ['INFO', 'ERROR', 'DEBUG', 'WARNING']

    # Validate level argument
    if level.upper() not in arg_list:
        print(f'The "{level}" is wrong argument!')
        return []
    else:
        # Filter and format matching logs
        return [f'{el['date']} {el['time']} - {el['message']}' for el in logs if el['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:

    """
    Count occurrences of each log level.
    
    Args:
        logs: List of log dictionaries
        
    Returns:
        dict: {level: count, ...}
    """
    return dict(Counter(log['level'] for log in logs))

def display_log_counts(counts: dict):

    """
    Format log counts as a text table.
    
    Args:
        counts: Dictionary of {level: count}
        
    Returns:
        str: Formatted table string
    """
    lines = []
    # Table header
    lines.append(f"{'Рівень логування':<10} | {'Кількість':<10}")
    lines.append("-" * 17 + "|" + "-" * 13)

    # Table rows
    for level, count in counts.items():
        lines.append(f"{level:<16} | {count}")

    # Join all lines with newlines
    return '\n'.join(lines)