# NetNTLM2HashCat
Converts John The Ripper format hashes (singular, or in bulk) to HashCat compatible hash format.

## Usage
* -i / --hash                     :  Singular hash input, it will prompt you after running the script.
* -f / --file [/file/path]        :  Import and process hashes using a list of hashes stored in a file.
* -o / --output [/file/path.txt]  :  Output hashes to a file. If this option is not used then hashes will be sent to stdout.

### Example Usage
*  ./netntlm2hashcat.py -i
*  ./netntlm2hashcat.py --hash
*  ./netntlm2hashcat.py -f hash_list.txt -o converted_hashes.txt
*  ./netntlm2hashcat.py -f hash_list.txt

## Hash Formats
* John The Ripper: ins1gn1a:$NETNTLM$b6230fa64e2f98a8$47ddd5e7d46114b6d65029d02ac1dd41e4ebd15121c4b772
* Hashcat: ins1gn1a::::47ddd5e7d46114b6d65029d02ac1dd41e4ebd15121c4b772:b6230fa64e2f98a8
