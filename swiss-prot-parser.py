import sys


def print_help():
    help_message = """
    Swiss-Prot-Parser Help:
    Usage: python swiss-prot-parser.py [Input_File] [-Key] [SearchTerm] ... [Output_File]
    
    Examples:
    - python swiss-prot-parser.py swissprot.dat.txt -AC Q197F8 output.txt
            -> Searches for entries with AC Q197F8 and saves the result in output.txt
    - python swiss-prot-parser.py swissprot.dat.txt -SQ MASNTV -OH "Aedes vexans" output.txt
            -> Searches for entries with the sequence 'MASNTV' and the host organism 'Aedes vexans' and saves the result in output.txt
    
    Arguments:
    - [Input_File] : The path to the data file (e.g., data/unip-mini.dat.txt)
    - [-Key] : A keyword from the entry (e.g., -ID, -SQ, -OH, etc.)
    - [SearchTerm] : The text to search for in the corresponding section of the entry
    - [Output_File] : The path where the results should be saved
    
    Use '--help' to display this help message.
    """
    print(help_message)


# Check for --help argument
if "--help" in sys.argv:
    print_help()
    sys.exit()


def search_entries(input_file_path, search_terms, output_file_path):
    """
    Searches for specific entries in a Swiss-Prot formatted file based on given search criteria and writes matching entries to an output file.

    @param input_file_path: str
        The path to the Swiss-Prot formatted file to be searched.

    @param search_terms: dict
        A dictionary where each key is a data entry field (like 'SQ', 'ID', 'AC') and the corresponding value is the search term for that field.
        The method searches for entries that contain all specified search terms in their respective fields.

    @param output_file_path: str
        The path to the file where matching entries will be written. If entries are found, they are written to this file, each followed by '//'.

    @return: None
        This method does not return anything. It writes matching entries to the specified output file and prints the number of entries found and saved.
        If no matching entries are found, it prints "No matching entries found!".
    """
    number_of_entries = 0
    entries_found = False
    with open(input_file_path, "r") as file, open(output_file_path, "w") as output_file:
        entry = ""
        sections = {key: "" for key in search_terms}
        current_section = None

        for line in file:
            if line.strip() == "//":
                if all(search_term in sections[key] for key, search_term in search_terms.items()):
                    output_file.write(entry + "//" + "\n")
                    entries_found = True
                    number_of_entries += 1

                entry = ""
                sections = {key: "" for key in search_terms}
                current_section = None
            else:
                entry += line
                line_parts = line.split(maxsplit=1)
                line_key = line_parts[0].strip()

                if line_key in search_terms and line_key != current_section:
                    current_section = line_key
                    sections[current_section] = line_parts[1].strip() if len(line_parts) > 1 else ""
                elif current_section and line.startswith(" "):
                    sections[current_section] += " " + line.strip()

    if not entries_found:
        print("No matching entries found!")
    elif number_of_entries == 1:
        print("1 entry saved!")
    else:
        print(f"{number_of_entries} entries saved!")


# Read input parameter
args = sys.argv[1:]

# Parse arguments and read search terms
if len(args) >= 4 and args[-2][0] != "-":
    input_file_path = args[0]
    output_file_path = args[-1]
    search_terms = {args[i][1:]: args[i + 1] for i in range(1, len(args) - 2, 2) if args[i].startswith("-")}
    search_entries(input_file_path, search_terms, output_file_path)
else:
    print("Incorrect input!")
    print_help()
