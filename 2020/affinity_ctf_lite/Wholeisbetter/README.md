# Wholeisbetter

**Category: Forensics**  
**Points: 378**

## Description
Given a pdf file `There_is_a_flag_somewhere.pdf`, find the flag.

## Solution
The first thing I did after downloading the file is to verify if it is a pdf file
```bash
$ file There_is_a_flag_somewhere.pdf\
There_is_a_flag_somewhere.pdf: PDF document, version 1.7 (password protected)
```

After that I checked the metadata with exiftool.  
```bash
$ exiftool There_is_a_flag_somewhere.pdf
ExifTool Version Number         : 12.00
File Name                       : There_is_a_flag_somewhere.pdf
Directory                       : .
File Size                       : 16 kB
File Modification Date/Time     : 2020:11:20 16:06:38+07:00
File Access Date/Time           : 2020:11:20 16:09:09+07:00
File Inode Change Date/Time     : 2020:11:20 16:06:38+07:00
File Permissions                : rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Warning                         : Install Compress::Zlib to process filtered streams
Page Count                      : 1
Language                        : pl-PL
Tagged PDF                      : Yes
XMP Toolkit                     : Image::ExifTool 10.80
Creator                         : Li4tLS0tLi4uLS0tLS0tLi4tLS0tLS0uLi4tLS0tLi4uLS0tLS0tLi4tLS0tLS0uLi4uLS0tLS4uLS0tLS0tLi4tLS4uLS0uLi4tLS0tLi4uLS0tLS0tLi4tLS0tLS0uLi0tLi4uLS0uLi0tLS0tLS4uLS0tLS0tLi4uLS0tLS4uLi0tLS0tLi4uLi0tLS0uLi4tLS0tLS0uLi4tLS0tLi4uLS0tLS4uLgo=#1
Subject                         : Li0tLS0tLS4uLS0tLS4uLi4tLS0tLi4uLi0tLi4uLi4uLi4tLS4uLi4tLS0tLi4uLi0tLS4uLi4uLi4tLS4uLi4tLS0tLS0uLi0tLS0tLS4uLi4tLS4uLi4tLS0tLi4uLi0tLi0uLS0uLi0tLS0uLi4uLi4tLS4uLi4tLS0tLS0uLi0tLi4tLS4uLS0tLS0tLi4uLi0tLi4uLi0tLS0tLS4uLi4uLS0tLgo=#3
Author                          : Li0tLi4tLS4uLS0uLi4uLi4tLS4uLi4uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi4uLS0uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi0tLi4uLS0uLi0tLi4uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLS0uLi0tLi4uLi0tLi4uLi0tLi4tLS4uLi4tLS4uLgo=#4
Producer                        : Li0tLi4tLS4uLS0uLi4uLi4tLS4uLi4uLi4tLS0tLi4uLi4tLS4uLi4tLS4uLi4uLi4uLS0tLS4uLS0tLS0tLi4tLS4uLS0uLi0tLi4tLS4uLi4tLS4uLi4tLS0tLS0uLi0tLi4uLS0uLi0tLS0tLS4uLi4tLS4uLi4tLS4uLS0uLi0tLS0tLi4uLS0uLi0tLi4uLi0tLi4uLi0tLi4tLS4uLS0tLS4uLgo=#5
Keywords                        : Li0tLi4tLS4uLS0uLi4uLi4tLS4uLi4uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi4uLS0uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLi4tLS4uLi4tLS4uLi4uLi0tLS4tLS0uLi0tLi4uLi4uLi4tLS4uLi4tLS4uLS0uLi0tLi4tLS4uLS0uLi0tLi4uLi0tLi4uLi0tLi4tLS4uLi4tLS4uLgo=#2
```

You can see some suspicious text here. It looks like a base64 encoded string, with unordered numbers at the ends.
Here's a bash one-liner to extract and decode the encoded text:  
```bash
$ exiftool There_is_a_flag_somewhere.pdf | tail -n 5 | grep -oP '(?<=: ).*=' | base64 -d
..----...------..------...----...------..------....----..------..--..--...----...------..------..--...--..------..------...----...-----....----...------...----...----...
.------..----....----....--........--....----....---.......--....------..------....--....----....--.-.--..----......--....------..--..--..------....--....------.....---.
.--..--..--......--......--..--....--....--........--......--....--..--..--..--....--....--......--...--..--........--....--..--..--..--..--..--....--....--..--....--...
.--..--..--......--.......----.....--....--........----..------..--..--..--..--....--....------..--...--..------....--....--..--..-----...--..--....--....--..--..----...
.--..--..--......--......--..--....--....--........--......--....--..--..--..--....--....--......---.---..--........--....--..--..--..--..--..--....--....--..--....--...
```

From the output, you can see slightly something that looks like text. We can substitute the dots into spaces to get a better look.
```bash
$ exiftool There_is_a_flag_somewhere.pdf | tail -n 5 | grep -oP '(?<=: ).*=' | base64 -d | tr '.' ' '
  ----   ------  ------   ----   ------  ------    ----  ------  --  --   ----   ------  ------  --   --  ------  ------   ----   -----    ----   ------   ----   ----   
 ------  ----    ----    --        --    ----    ---       --    ------  ------    --    ----    -- - --  ----      --    ------  --  --  ------    --    ------     --- 
 --  --  --      --      --  --    --    --        --      --    --  --  --  --    --    --      --   --  --        --    --  --  --  --  --  --    --    --  --    --   
 --  --  --      --       ----     --    --        ----  ------  --  --  --  --    --    ------  --   --  ------    --    --  --  -----   --  --    --    --  --  ----   
 --  --  --      --      --  --    --    --        --      --    --  --  --  --    --    --      --- ---  --        --    --  --  --  --  --  --    --    --  --    --   
```

It looks like the flag, but something still looks odd. The numbers from before must be the correct order of these lines. After saving the output into a file, I corrected the order of the lines. Here's the flag:  
```bash
$ cat flag.txt 
  ----   ------  ------   ----   ------  ------    ----  ------  --  --   ----   ------  ------  --   --  ------  ------   ----   -----    ----   ------   ----   ----   
 --  --  --      --      --  --    --    --        --      --    --  --  --  --    --    --      --- ---  --        --    --  --  --  --  --  --    --    --  --    --   
 ------  ----    ----    --        --    ----    ---       --    ------  ------    --    ----    -- - --  ----      --    ------  --  --  ------    --    ------     --- 
 --  --  --      --      --  --    --    --        --      --    --  --  --  --    --    --      --   --  --        --    --  --  --  --  --  --    --    --  --    --   
 --  --  --      --       ----     --    --        ----  ------  --  --  --  --    --    ------  --   --  ------    --    --  --  -----   --  --    --    --  --  ----   
```  

FLAG - AFFCTF{IHATEMETADATA}
