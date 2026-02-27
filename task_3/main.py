from function import *
import sys

def main(args: list):
    """
    Main entry point for the log analyzer application.
    
    Processes command line arguments, loads log file, displays statistics
    and optionally filters logs by level.
    
    Args:
        args: Command line arguments (sys.argv)
              args[1] - path to log file
              args[2] - optional log level for filtering
    """
    try:
        # Load logs from file
        logs = load_logs(args[1])

        # Check if logs were loaded successfully
        if logs is not None:
            # Display log statistics table
            print(display_log_counts(count_logs_by_level(logs)))

            # If level filter specified
            if len(args) > 2:
                level = args[2]
                filter_logs = filter_logs_by_level(logs, level)
                print(f'\nДеталі логів для рівня "{level.upper()}":')

                # Display filtered logs if found
                for line in filter_logs:
                    print(line)

    
    except FileNotFoundError:
        print(f"Error: file '{args[1]}' not found")
    except ValueError:
        print('Error: file does not contain information or is in the wrong format')
    except IndexError:
        print('Error: Specify the file path')


if __name__ == "__main__":
    main(sys.argv)