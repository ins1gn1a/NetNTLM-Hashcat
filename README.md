# NTLM v1 & v2 > Hashcat
Converts Cain or John NTLMv1 and NTLMv2 hashes (singular, or in bulk) to HashCat compatible format.

## NTLMv1-Hashcat Arguments
* -i / --hash                     :  Singular hash input. You will get a prompt after running the script.
* -f / --file [/file/path]        :  Import and process hashes using a list of hashes stored in a file.
* -o / --output [/file/path.txt]  :  Output hashes to a file. If this option is not used then hashes will be sent to stdout.

### Example Usage
*  ./ntlmv1-hashcat.py -i
*  ./ntlmv1-hashcat.py --hash
*  ./ntlmv1-hashcat.py -f hash_list.txt -o converted_hashes.txt
*  ./ntlmv1-hashcat.py -f hash_list.txt

### Hash Formats
* John The Ripper: ins1gn1a:$NETNTLM$b6230fa64e2f98a8$47ddd5e7d46114b6d65029d02ac1dd41e4ebd15121c4b772
* Hashcat: ins1gn1a::::47ddd5e7d46114b6d65029d02ac1dd41e4ebd15121c4b772:b6230fa64e2f98a8

## NTLMv2-Hashcat Arguments
* Only one argument is taken, which is the input file of hashes.

### Example Usage 
* ./ntlmv2-hashcat.sh input-file.txt
