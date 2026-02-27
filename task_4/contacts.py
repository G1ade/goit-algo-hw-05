def parse_input(user_input: str) -> tuple:
    """
    Parse user input into command and arguments.
    
    Splits input string by spaces. First word becomes command,
    remaining words are collected into args list.
    
    Args:
        user_input (str): Raw input string from user
        
    Returns:
        tuple: (command, *args) where command is lowercase string
    """

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: tuple, path: str) -> str:
    """
    Add a new contact to the phone book file.
    
    If file doesn't exist, creates it. Appends contact in format 'name:phone'.
    
    Args:
        args (list): List containing [name, phone]
        path (str): Path to the contacts file
        
    Returns:
        str: Success message or error description
    """

    name, phone = args
    mode = 'a'

    # Loop until successfully written (handles missing file case)
    while True:
        try:
            with open(path, mode, encoding='utf-8') as file:
                file.write(f'{name}:{phone}\n')
                break
        except FileNotFoundError:
            mode = "w"

    return "Contact added."

def change_contact(args: tuple, path: str) -> str:
    """
    Update phone number for an existing contact.
    
    Reads all contacts, updates specified contact's phone,
    then rewrites the entire file.
    
    Args:
        args (list): List containing [name, new_phone]
        path (str): Path to the contacts file
        
    Returns:
        str: Success message or error description
    """

    desired_name, new_phone = args

    try:
        # Read existing contacts into dictionary
        with open(path, 'r', encoding='utf-8') as file:
            contacts = dict(el.strip().split(':') for el in file.readlines())

            # Check if contact exists
            if desired_name not in contacts:
                return f'contact {desired_name} not found.'
            else:
                contacts[desired_name] = new_phone
        
        # Rewrite file with updated data
        with open(path, 'w', encoding='utf-8') as file:
            for name, phone in contacts.items():
                file.write(f'{name}:{phone}\n')
                
    except FileNotFoundError:
        return "You haven't added any contacts yet!"
        
    return "contact changed"

def phone_username(args, path):
    """
    Retrieve phone number for a specific contact.
    
    Args:
        args (list): List containing [name]
        path (str): Path to the contacts file
        
    Returns:
        str: Contact info or error message
    """

    try:
        # Load contacts from file
        with open(path, 'r', encoding='utf-8') as file:
            contacts = dict(el.strip().split(':') for el in file.readlines())
            # Get phone for requested contact (args[0] is the name)
            return f'{args[0]} {contacts[args[0]]}'
        
    except KeyError:
        return f"The contact '{args[0]}' does not exist in your list"
    except FileNotFoundError:
        return "You haven't added any contacts yet!"

def all_contacts(path: str) -> str:
    """
    Display all contacts in formatted table.
    
    Args:
        path (str): Path to the contacts file
        
    Returns:
        str: Formatted table of contacts or error message
    """

    try:
        # Read all contacts
        with open(path, 'r', encoding='utf-8') as file:
            contacts = dict(el.strip().split(':') for el in file.readlines())
        
        # Build formatted output lines
        lines = []
        lines.append("-" * 25)
        lines.append(f"{'Name':<10} | {'Phone':<10}")
        lines.append("-" * 25)
        
        # Add each contact to table
        for name, phone in contacts.items():
            lines.append(f"{name:<10} | {phone}")
            
        lines.append("-" * 25)
        
        # Join all lines with newlines
        return "\n".join(lines)
        
    except FileNotFoundError:
        return "You haven't added any contacts yet!"