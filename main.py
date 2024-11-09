from app.calculator import Calculator 

def left_align_text(text, width=50):
    """Aligns the provided text to the left within the specified width.

    Args:
        text (str): Text to align.
        width (int): Total width to align within.

    Returns:
        str: The left-aligned text.
    """
    return text.ljust(width)

def display_header(text):
    """Prints a header with left-aligned text without borders."""
    print("\n" + left_align_text(text, 50) + "\n")

def main():
    """Runs the interactive calculator, handling user input and commands."""
    calculator = Calculator()

    display_header("Welcome to the Calculator!")
    print(left_align_text("Type 'help' for a list of commands.") + "\n")

    while True:
        user_input = input(">>> Enter a command: ").strip().lower()

        if user_input in ['exit', 'quit']:
            display_header("Exiting the calculator.")
            break

        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        try:
            # Convert arguments to float if possible
            args = [float(arg) for arg in args]
            output = calculator.execute_command(command, *args)

            if isinstance(output, (int, float)):
                display_header(f"Result: {output}")
            elif isinstance(output, list):
                display_header("History:")
                for item in output:
                    print(left_align_text(str(item), 50))
                print("\n")
            else:
                display_header(output)  # Messages like help text or errors

        except ValueError:
            display_header("Error: Invalid input.")
            print(left_align_text("Please ensure all arguments are numbers.", 50) + "\n")
        except Exception as e:
            display_header(f"Error: {e}")

if __name__ == "__main__":  # pragma: no cover
    main()
