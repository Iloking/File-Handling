# Function to display current student records
def view_records(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("No records found. Please add student details first.")

# Function to add student information
def add_record(file_name):
    name = input("Enter student's name: ")
    intro = input(f"Enter a brief introduction for {name}: ")
    subject = input(f"What is {name}'s favorite subject? ")
    
    with open(file_name, 'a') as file:
        file.write(f"Name: {name}\nIntroduction: {intro}\nFavorite Subject: {subject}\n\n")
    print(f"{name}'s information has been added.")

# Function to erase all records
def clear_records(file_name):
    open(file_name, 'w').close()
    print("All records have been cleared.")

# Main function to handle the program flow
def main():
    file_name = 'students.txt'
    
    while True:
        print("\nOptions:")
        print("1. View all student records")
        print("2. Add a new student record")
        print("3. Clear all records")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_records(file_name)
        elif choice == '2':
            add_record(file_name)
        elif choice == '3':
            clear_records(file_name)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
