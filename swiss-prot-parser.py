import sys


def print_help():
    help_message = """
    Swiss-Prot-Parser Help:
    Usage: python swiss-prot-parser.py [Input_File] [-Key SearchTerm] ... [Output_File]
    
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
    else:
        print("Entries saved!")


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
