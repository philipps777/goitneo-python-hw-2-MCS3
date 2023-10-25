def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Give me name and phone please."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    result = "\n".join(
        [f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def main():
    print("Welcome to the assistant bot!")

    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print(f"Invalid command. Use 'add {name} {phone}'.")

        elif command == "change":
            if len(args) == 2:
                name, phone = args
                print(change_contact(contacts, name, phone))
            else:
                print(f"Invalid command. Use 'change {name} {phone}'.")

        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                result = show_phone(contacts, name)
                print(result)
            else:
                print(f"Invalid command. Use 'phone {name}'.")

        elif command == "all":
            result = show_all(contacts)
            print(result)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
