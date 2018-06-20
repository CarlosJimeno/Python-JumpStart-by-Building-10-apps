import os


def load(name):
    """
    Loads the journal if it exists, otherwise it returns an empty list

    :param name: the name of the journal to load
    :return: the journal in list format
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    Saves the journal on the folder 'journals' with as 'name.jrl'
    :param name: the name of the journal to save
    :param journal_data: the data to save
    """
    filename = get_full_pathname(name)
    print('... Saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    """
    Gets the full path of the journal.
    It must be on the folder 'journals'

    :param name: the name of the journal
    :return: the full path of the journal
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + 'jrl'))
    return filename


def add_entry(text, journal_data):
    """
    Adds an entry to the journal_data

    :param text: entry
    :param journal_data: journal_data in list format
    """
    journal_data.append(text)
