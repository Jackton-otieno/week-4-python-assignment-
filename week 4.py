def main():
    
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write the modified version: ")

    try:
        
        with open(input_filename, 'r') as infile:
            content = infile.read()

        
        modified_content = content.upper()

    
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read '{input_filename}' or write to '{output_filename}'.")

if __name__ == "__main__":
    main()
