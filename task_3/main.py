from function import *
import sys

def main(args: list):

    try:
        logs = load_logs(args[1])

        if logs is not None:
            print(display_log_counts(count_logs_by_level(logs)))

            if len(args) > 2:
                level = args[2]
                filter_logs = filter_logs_by_level(logs, level)
                print(f'\nДеталі логів для рівня "{level.upper()}":')

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