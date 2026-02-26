def load_logs(file_path: str) -> list:

    with open(file_path, 'r', encoding='utf-8' ) as file:
        data = [el.strip() for el in file.readlines()]
        
    return data