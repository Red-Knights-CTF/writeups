# Active directory
**category: forensics**  
**points: 483**

## Description
Once upon a time in Active Directory, Red Teamers used to love it! Microsoft loves leaking keys :P  
We are given a zip file, find the flag.

## Solution
Inside the zip file is a windows directory structure containing several files. Here's the output of tree.

```
$ tree 329d7767b42f3d8e9f498e98fbabc83c/
329d7767b42f3d8e9f498e98fbabc83c/
└── Policies
    ├── {25B2A34C-016D-51D2-945F-11C04GB984F9}
    │   ├── MACHINE
    │   │   ├── Microsoft
    │   │   │   └── Windows NT
    │   │   │       └── SecEdit
    │   │   │           └── GptTmpl.inf
    │   │   └── Registry.pol
    │   ├── USER
    │   └── GPT.INI
    ├── {2AC1451C-016F-11D2-945F-00C04fB984F9}
    │   ├── MACHINE
    │   │   └── Microsoft
    │   │       └── Windows NT
    │   │           └── SecEdit
    │   │               └── GptTmpl.inf
    │   ├── USER
    │   └── GPT.INI
    ├── {75DE8F0A-DEC0-441F-AE29-90DFAFCF632B}
    │   ├── Group Policy
    │   │   └── GPE.INI
    │   ├── Machine
    │   ├── User
    │   │   └── Preferences
    │   │       └── Groups
    │   │           ├── base64
    │   │           └── Groups.xml
    │   └── GPT.INI
    └── {C7BD6C6D-A1C8-4C23-815E-3D8D4187640F}
        ├── Machine
        │   ├── Microsoft
        │   │   └── Windows NT
        │   │       └── SecEdit
        │   │           └── GptTmpl.inf
        │   └── Scripts
        │       ├── Shutdown
        │       └── Startup
        ├── User
        └── GPT.INI

28 directories, 11 files
```

Maybe the flas is in some of these files. After some googling, I found out about several things:
- Active Directory (AD) is a database and set of services that connect users with the network resources they need to get their work done. The database (or directory) contains critical information about your environment, including what users and computers there are and who’s allowed to do what. For example, the database might list 100 user accounts with details like each person’s job title, phone number and password. It will also record their permissions.
- This awesome [post](https://adsecurity.org/?p=2362) detailing how to attack active directories.

Most of the time, the user passwords are stored in xml files. Lets cat the output of Groups.xml.

```
$ cat Groups.xml 
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Administrator (built-in)" image="1" changed="2014-02-06 19:33:28" uid="{C73C0939-38FB-4287-AC48-478F614F5EF7}" userContext="0" removePolicy="0"><Properties action="R" fullName="Administrator" description="Administrator" cpassword="3g4TWcMxZ0ZrE2jVR7dTo35mGErheJS8w6opX3UW9a3FvxHRskfK/CUOf1GBB8z7MYH1u8jUnJxHZs7DjYM0bQ" changeLogon="0" noChange="0" neverExpires="1" acctDisabled="0" subAuthority="" userName="Administrator (built-in)"/></User>
</Groups>
```
There we can see the GPP(Group Policy Preferences) password `cpassword="3g4TWcMxZ0ZrE2jVR7dTo35mGErheJS8w6opX3UW9a3FvxHRskfK/CUOf1GBB8z7MYH1u8jUnJxHZs7DjYM0bQ"`.  
Windows users can use this powershell [script](https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Get-GPPPassword.ps1) to decrypt the password.  
There is also a [tool](https://tools.kali.org/password-attacks/gpp-decrypt) in kali called `gpp-decrypt` to decrypt it.

```
$ gpp-decrypt 3g4TWcMxZ0ZrE2jVR7dTo35mGErheJS8w6opX3UW9a3FvxHRskfK/CUOf1GBB8z7MYH1u8jUnJxHZs7DjYM0bQ
b00t2root{Grp_p0l1c13s_sUck}
```

**FLAG:** `b00t2root{Grp_p0l1c13s_sUck}`

