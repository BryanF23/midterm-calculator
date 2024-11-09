class Calculator:
    def execute_command(self, command, *args):
        if command == "add":
            return sum(args)
        elif command == "subtract":
            return args[0] - args[1]
        elif command == "multiply":
            return args[0] * args[1]
        elif command == "divide":
            if args[1] == 0:
                return "Error: Cannot divide by zero"  # Consistent error message
            return args[0] / args[1]
        else:
            return "Error: Unknown command."

