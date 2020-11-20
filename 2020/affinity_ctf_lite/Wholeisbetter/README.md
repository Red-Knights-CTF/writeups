# Wholeisbetter

**Category: Forensics
**Points: 378

## Description
Given a pdf file, find the flag

## Solution
The first thing I did after downloading the file is to verify if it is a pdf file.

After that I checked the metadata with exiftool.

You can see some suspicious text here. It looks like a base64 encoded string, with unordered numbers at the ends.

Here's a bash one-liner to extract and decode the encoded text:

From the output, you can see slightly something that looks like text. We can substitute the dots into spaces to get a better look.

It looks like the flag, but something still looks odd. The numbers from before must be the correct order of these lines. After saving the output into a file, I corrected the order of the lines. Here's the flag:

FLAG - AFFCTF{IHATEMETADATA}
