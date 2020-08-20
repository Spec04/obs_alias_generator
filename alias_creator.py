"""
Alias file creator for Obsidian vault.

INPUT1: Path to vault
INPUT2: Alias search key/string
INPUT3: Filename of saved YAML file
INPUT4: Number of lines to limit search from top of note file (enter 0 or "" for all)
"""
import os, sys
from datetime import datetime
import yaml


def main():
    # Use the inputs from the CLI or BAT file
    if len(sys.argv) > 1:
        search_path   = sys.argv[1] # Location of the Vault folder
        search_str    = sys.argv[2] # Alias indicator key to search for at start of line
        save_filename = sys.argv[3] # Filename of the YAML file
        line_limit    = sys.argv[4] # Limit search of key to only top 'n' lines for speed
    else:
        # Ask the user to enter string to search
        search_path   = input("Enter directory path to search : ")
        search_str    = input("Enter the search string : ")
        save_filename = input("Enter the filename of the YAML file : ")
        line_limit    = input("Enter how many lines to limit search to : ")

    # Set blank line_limit as zero (infinite lines) if blank
    if not line_limit:
        line_limit = 0
    else: # set type as an int value
        line_limit = int(line_limit)

    # Collect all markdown files within the vault
    filepaths = []
    file_extn = '.md'
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith(file_extn):
                filepaths.append(os.path.join(root,file))

    # Store the Filenames and the Aliases in a Dictionary list
    dict_file = []
    # Repeat for each file in the directory
    for fpath in filepaths:
        # Open file for reading
        fo = open(fpath)
        # Read the first line from the file
        line = fo.readline()
        # Initialize counter for line number
        line_no = 1
        # Boolean to check limit condition
        limit = False

        # Loop until EOF and while Line number is within limit range
        while (line != '') and (limit == False):
            # Search for string in line
            index = line.find(search_str)
            
            # if (index != -1): # check for occurrence across the whole line
            if (index == 0): # check for occurrence at the start of line only
                
                # Remove the search string from the line and split into list if multiple
                line = line.replace(search_str,"").split(",")
                # Remove all leading and trailing whitespaces
                line = [x.rstrip() for x in line]
                line = [x.lstrip() for x in line]

                # Get filename without extension
                fname = os.path.split(fpath)[1].split('.')[0]
                # Append the filename and aliases to the dictionary list
                dict_file.append({fname:line})

            # Read next line
            line = fo.readline()
            # Increment line counter
            line_no += 1
            # Check whether we've reached the line_limit if one is set
            if (line_no > line_limit) and (line_limit != 0):
                limit = True
        # Close the files
        fo.close()

    # Merge list of dict to a single dict
    # dict_file = dict(j for i in dict_file for j in i.items())

    # Construct the header for the Alias file
    title  = f"# {'-'*30}\n# ALIAS FILE FOR OBSIDIAN VAULT"
    vault  = f"# Vault: {os.path.split(search_path)[1]}"
    create = f"# Created: {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}"
    inputs = f"# Alias Key: '{search_str}'\n# Line Limit: {line_limit} lines"
    header = f"{title}\n{vault}\n{create}\n# {'-'*30}\n{inputs}\n# {'-'*30}\n"


    # Save the dictionary list as a YAML file
    with open(save_filename+'.yml', 'w') as file:
        file.writelines(header+"\n")
        print(header)
        for d in dict_file:
            documents = yaml.dump(d, file)
            print(d)
            file.writelines("\n")



if __name__ == "__main__":

    main()
    print(f"\n# {'-'*30}")
    
