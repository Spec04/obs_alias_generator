# Obsidian Alias File Generator

A python script that compiles a yaml file of noted aliases for all notes within an obsidian vault. Makes easier forward linking possible.

Useful in creating shorthand names for notes due to acronym usage or to link in intext citations.

### Function
This script performs the following function:
- Searches an obsidian vault for all markdown files 
- Inspects each file for an alias keyword tag
- If tag found, extracts the subsequent alias names for that file
- Compiles all filenames and related tags into a YAML file

### NOTE
This script is designed to do some of the heavy lifting of creating a YAML file to feed into [**Ben Perkins'** great work to create forward links in obsidian notes](https://github.com/perkinsben/obs_tools/tree/master/forward_linker)

The intent of this script/method is to manage the alias names directly within obsidian notes, rather in a secondary document (the .yaml file)

------
## Requirements

### Python 
* Python 3 + pip
* [PyYAML](https://pypi.org/project/PyYAML/)

```
pip install pyyaml
```

### Obsidian
Withing your markdown note files an alias 'tag' must be added in the text to identify that the line contains aliases for the filename. This tag can be any unique string, but should be placed at the beginning of the line. 

Alias tags can be any combination of characters (string), if you plan on using the tag later in the document and dont want it flagged, set the ```line_limit``` value to a small enough number before you intend to use the tag (i.e. top 10 lines). Best to avoid this and only use a unique tag.

I tend to use ```::::``` as it is subtle and unobtrusive and place my aliases directly under the note title. But just as easily could be ```See Also:``` or ```=)``` you are only limited by your imagination

------

## Running the code
### Command line
#### If using the guided CLI prompts:
Run the following command in a terminal window. Python will prompt for additional inputs
```
python alias_creator.py
```

### If using CLI directly:
Alternatively you can enter the inputs directly as arguments to speed up the process
```
python alias_creator.py {obsidian vault root} {alias key} {yaml filename} {line limit}
```
The following would create an ```aliases.yml``` file for my ```Example_Vault``` by searching the first ```10``` lines of all files for the ```::::``` alias tag.
```
python "alias_creator.py" "C:/Obsidian/Example_Vault" "::::" "aliases" "10"
```


### For Windows users:
For making it even easier you can create a .BAT file (.txt file with extension change to .bat) and add the direct CLI commands from above. This makes it easier to run as a shortcut, and keep the inputs on hand if you regularly update your alias file.

```cmd
@echo off
python alias_creator.py {obsidian vault root} {alias key} {yaml filename} {line limit}
pause
```
The following would create an ```aliases.yml``` file for my ```Example_Vault``` by searching the first ```10``` lines of all files for the ```::::``` alias tag.
``` cmd
@echo off
python ^
    "alias_creator.py" ^
    "C:/Obsidian/Example_Vault" ^
    "::::" ^
    "aliases" ^
    "10"
pause
```
-------
## Example usage

While working on your note called ```Working from home.md``` you would add the alias tag ```::::``` which identifies alternative aliases for the file, and add additional aliases you wish to link this note to.
```md
# Working from home
----
:::: Remote working, Remote worker, WFH

A side effect of the ...
```
Executing the script will generate the following entry into your yml alias file:

```yaml
Working from home:
- Remote working
- Remote worker
- WFH
```

The script will also include some additional header information within your alias file for tracking when it was last run and under what inputs. This additional header does not negatively impact forward linking code.

An example of the full output would be:

```yaml
# ------------------------------
# ALIAS FILE FOR OBSIDIAN VAULT
# Vault: Example_Vault
# Created: 19-08-2020, 22:32:05
# ------------------------------
# Alias Key: '::::'
# Line Limit: 10 lines
# ------------------------------

Working from home:
- Remote working
- Remote worker
- WFH
```

---------


## Acknowledgments
* Shoutout to [Ben Perkins](https://github.com/perkinsben/obs_tools/tree/master/forward_linker) for his useful script that inspired this one.
