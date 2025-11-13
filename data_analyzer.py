dataset = []  

def input_dataset():
    global dataset

    print("\nChoose data type:")
    print("1. 1D Dataset")
    print("2. 2D Dataset")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        user_input = input("Enter numbers separated by spaces: ")
        dataset = [int(x) for x in user_input.split()]
        print("1D Data stored successfully!")
        print("Your Data:", dataset)

    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        dataset = []
        print("Enter data row by row:")
        for i in range(rows):
            row_data = [int(x) for x in input(f"Row {i+1}: ").split()]
            if len(row_data) != cols:
                print("You must enter exactly", cols, "numbers.")
                return
            dataset.append(row_data)
        print("2D Data stored successfully!")
        print("Your 2D Data:")
        for row in dataset:
            print(row)

    else:
        print("Invalid choice! Please choose 1 or 2.")

def display_summary():
    if not dataset:
        print("Please enter data first using option 1.")
        return
    if isinstance(dataset[0], list):
        print("This summary works only for 1D data, not 2D.")
        return
    print("\nDATA SUMMARY")
    print("Total Elements:", len(dataset))
    print("Sum of Elements:", sum(dataset))
    print("Minimum Value:", min(dataset))
    print("Maximum Value:", max(dataset))
    print("Average Value:", sum(dataset)/len(dataset))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_menu():
    if not dataset:
        print("Please enter data first using option 1.")
        return
    n = int(input("Enter a number to find factorial: "))
    print(f"Factorial of {n} = {factorial(n)}")

def filter_data():
    if not dataset:
        print("Please enter data first using option 1.")
        return
    if isinstance(dataset[0], list):
        print("This function works only for 1D data.")
        return
    limit = int(input("Enter a threshold value: "))
    filtered = list(filter(lambda x: x >= limit, dataset))
    print(f"Values greater than or equal to {limit} are: {filtered}")

def sort_data():
    if not dataset:
        print("Please enter data first using option 1.")
        return
    if isinstance(dataset[0], list):
        print("Sorting works only for 1D data.")
        return
    print("1. Ascending Order")
    print("2. Descending Order")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("Sorted Data (Ascending):", sorted(dataset))
    elif choice == "2":
        print("Sorted Data (Descending):", sorted(dataset, reverse=True))
    else:
        print("Invalid choice!")

def dataset_statistics():
    if not dataset:
        print("Please enter data first using option 1.")
        return
    if isinstance(dataset[0], list):
        print("Statistics works only for 1D data.")
        return
    total = sum(dataset)
    average = total / len(dataset)
    return min(dataset), max(dataset), total, average

def show_statistics():
    stats = dataset_statistics()
    if stats:
        print("\nDATASET STATISTICS")
        print("Minimum Value:", stats[0])
        print("Maximum Value:", stats[1])
        print("Total Sum:", stats[2])
        print("Average:", round(stats[3], 2))

def exit_program():
    print("Thank you for using the Data Analyzer Program!")
    print("Goodbye")
    exit()

while True:
    print("\n========== Functional Treat Menu ==========")
    print("1. Input Dataset (1D or 2D)")
    print("2. Display Data Summary (1D only)")
    print("3. Find Factorial (Recursion)")
    print("4. Filter Data (Lambda Function - 1D only)")
    print("5. Sort Data (1D only)")
    print("6. Dataset Statistics (1D only)")
    print("7. Exit Program")
    print("=================*******=====================")

    choice = input("\nEnter your choice (1–7): ")

    match choice:
        case "1":
            input_dataset()
        case "2":
            display_summary()
        case "3":
            factorial_menu()
        case "4":
            filter_data()
        case "5":
            sort_data()
        case "6":
            show_statistics()
        case "7":
            exit_program()
        case _:
            print("Invalid Choice! Please select between 1 to 7.")