from doctrine import Doctrine


def main():
    doctrine = Doctrine.load("standard_public_template")
    receipt = doctrine.mount()
    print(receipt["instruction_context"])


if __name__ == "__main__":
    main()
