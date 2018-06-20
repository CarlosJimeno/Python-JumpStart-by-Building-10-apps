import journal

print(help(journal))


def main():
    print_header()
    run_event_loop()


def print_header():
    print("----------------------------------")
    print("          JOURNAL APP")
    print("----------------------------------\n")


def run_event_loop():
    """
    Main loop of the journal app, saves the journal at the end.
    """
    print("What do you want to do with your journal?")
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    exit_cmds = ['x', 'exit', '']
    list_cmds = ['l', 'list']
    add_cmds = ['a', 'add']

    while cmd not in exit_cmds:
        cmd = input('[L]ist entries, [A]dd entry, E[x]it: ').lower().strip()

        if cmd in list_cmds:
            # print('Listing...')
            list_entries(journal_data)
        elif cmd in add_cmds:
            # print('Adding...')
            add_entry(journal_data)

        elif cmd not in exit_cmds:
            print("Sorry, I don't understand '{}'.".format(cmd))

    journal.save(journal_name, journal_data)
    print('Done, goodbye')


def list_entries(data):
    """
    List all the entries in the journal in reverse order

    :param data: the journal in list format
    """
    for i, entry in enumerate(reversed(data)):
        print("* [{}] {}".format(i + 1, entry))


def add_entry(data):
    """
    Add an entry to the journal

    :param data: the journal in list format
    """
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
