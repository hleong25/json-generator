import logging


def setup():
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def main():
    setup()

    logging.info("hello world")


if __name__ == "__main__":
    main()
