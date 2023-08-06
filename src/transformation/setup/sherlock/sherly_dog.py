import pkg_resources


def main():
    path = 'example.txt'
    filepath = pkg_resources.resource_filename(__name__, path)
    print("Sherlock the great dog!")
    for line in open(filepath):
        print(line)


if __name__ == '__main__':
    main()
