# main.py

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

def append_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())

def main():
    file_path = input("Enter file path: ")

    while True:
        choice = input("\nChoose: 1-Read, 2-Write, 3-Append, 4-Count lines, 5-Exit: ")

        if choice == '1':
            print(read_file(file_path))
        elif choice == '2':
            write_file(file_path, input("Enter text: "))
        elif choice == '3':
            append_file(file_path, input("Enter text: "))
        elif choice == '4':
            print(f"Total lines: {count_lines(file_path)}")
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
