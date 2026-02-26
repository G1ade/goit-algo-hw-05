from collections import Counter
from pathlib import Path

def parse_log_file(line: str) -> dict:

    date, time, level, message = line.split(" ", 3)
    return {'date': date, 'time': time, 'level': level, 'message': message}

def load_logs(file_path: str) -> list:

    file_path = Path(file_path)
    if file_path.suffix.lower() != '.log':
        print(f'Error: "{file_path.name}" must have ".log" extension')
        return []
    else:
        with open(file_path, 'r', encoding='utf-8' ) as file:
            logs = [parse_log_file(line.strip()) for line in file.readlines()]
            
        if not logs:
            print("Warning: log file is empty")
            return None
            
        return logs

def filter_logs_by_level(logs: list, level: str) -> list:

    arg_list = ['INFO', 'ERROR', 'DEBUG', 'WARNING']

    if level.upper() not in arg_list:
        print(f'The "{level}" is wrong argument!')
        return []
    else:
        return [f'{el['date']} {el['time']} - {el['message']}' for el in logs if el['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:

    return dict(Counter(log['level'] for log in logs))

def display_log_counts(counts: dict):

    lines = []
    lines.append(f"{'Рівень логування':<10} | {'Кількість':<10}")
    lines.append("-" * 17 + "|" + "-" * 13)

    for level, count in counts.items():
        lines.append(f"{level:<16} | {count}")

    return '\n'.join(lines)