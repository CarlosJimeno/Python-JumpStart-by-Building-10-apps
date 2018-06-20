import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')


def print_header():
    print('-------------------------------------')
    print('          FILE SEARCH APP')
    print('-------------------------------------\n')


def get_folder_from_user():
    folder = input('What folder do you want to search in? ')

    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def search_folders(folder, text):
    items = os.listdir(folder)

    for item in items:

        full_item = os.path.join(folder, item)

        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)

        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    matches = []

    with open(filename, 'r', encoding='utf-8') as fin:
        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(file=filename, line=line_number, text=line)
                yield m

    return matches


def main():
    print_header()

    folder = get_folder_from_user()

    if not folder:
        print("Sorry we can't search that location.")
        return

    text = get_search_text_from_user()

    if not text:
        print("Sorry we can't search for nothing.")
        return

    matches = search_folders(folder, text)

    match_count = 0

    for m in matches:
        match_count += 1
        print('--------- MATCH ---------')
        print('file: ' + m.file)
        print('line: ' + str(m.line))
        print('text: ' + m.text)
        print()

    print('Found {:,} matches.'.format(match_count))


if __name__ == '__main__':
    main()
