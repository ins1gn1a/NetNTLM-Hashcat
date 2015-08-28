# NetNTLM2HashCat
Converts John The Ripper format hashes (singular, or in bulk) to HashCat compatible hash format.

## Usage
-i / --hash                     :  Singular hash input, it will prompt you after running the script.
-f / --file [/file/path]        :  Import and process hashes using a list of hashes stored in a file.
-o / --output [/file/path.txt]  :  Output hashes to a file. If this option is not used then hashes will be sent to stdout.

## To Do
I need to fix file output as the output files are currently empty when being written (I have no idea why).
