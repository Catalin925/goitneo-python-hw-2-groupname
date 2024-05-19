def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(args, kwargs):
        try:
            return func(args, kwargs)
        except ValueError:
            return "Give me name and phone number, please."
        except KeyError:
            return "Unable to find contact."
        except IndexError:
            return "Invalid command"

    return inner

@input_error
def add_contact(*args, contact):
    name, phone = args
    contact[name] = phone
    return "Contact added successfully"

@input_error
def change_contact(*args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated successfully"
    else:
        return "Unable to find contact"

