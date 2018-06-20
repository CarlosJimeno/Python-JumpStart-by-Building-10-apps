import movie_service
import requests.exceptions


def print_header():
    print("------------------------------------------------")
    print("              MOVIE SEARCH APP")
    print("------------------------------------------------")


def run_search_loop():
    exit_cmds = ['x', 'exit', 'quit', 'q']
    search_term = "Search term"

    while search_term.lower() not in exit_cmds:

        search_term = input("\nWhat movie do you want to search for? ")
        if search_term not in exit_cmds:

            try:
                movies = movie_service.search_movie(search_term)
                movie_service.print_movies(movies)
            except requests.exceptions.ConnectionError:
                print('Error: your connection is down.')
            except ValueError:
                print('ValueError: Inappropriate argument value.')
            except Exception as e:
                print(type(e))
                print(e.__cause__)

    print('exiting...')


def main():
    print_header()
    run_search_loop()


if __name__ == '__main__':
    main()
