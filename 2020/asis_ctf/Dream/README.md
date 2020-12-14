# Dream 
**category:** Forensics  
**points:** 77
**solves:** 66

## Description
We are in a dream, within another dream!

## Solution
The challenge file is **flag.malformed**, examining it inside an hex editor I saw magicbytes like `FORM..|.DJVUINFO` which make me think it should be a DejaVu File.
After examining some deja vu files I realised only the first hex line was missing, so I repaired the files with : 
```
(echo -n "\x41\x54\x26\x54\x46\x4f\x52\x4d\x00\x00\x5c\x1a\x44\x4a\x56\x4d" ; cat flag.malformed) > flag.djvu
```
Now `file` recognize it as `DjVu multiple page document`: 
```
$ file flag.djvu 
flag.djvu: DjVu multiple page document
```

opening the file gives this : 
![](https://i.imgur.com/G4INaOp.png)

So the flag must be hidden inside the djvu file.
I run the following command : 
```
$ djvused flag.djvu -e output-all
select; remove-ant; remove-txt
# ------------------------- 
select "shared_anno.iff"
set-ant
(metadata
	(ModDate "2020-12-07 01:53:39+03:30")
	(CreationDate "2020-12-07 01:53:39+03:30")
	(Producer "GPL Ghostscript 9.53.3")
	(Creator "Draw") )
(xmp "<x:xmpmeta xmlns:x=\"adobe:ns:meta/\" x:xmptk=\"XMP Core 4.4.0-Exiv2\">\n   <rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\n      <rdf:Description rdf:about=\"\"\n            xmlns:pdf=\"http://ns.adobe.com/pdf/1.3/\">\n         <pdf:Producer>GPL Ghostscript 9.53.3</pdf:Producer>\n      </rdf:Description>\n      <rdf:Description rdf:about=\"\"\n            xmlns:xmp=\"http://ns.adobe.com/xap/1.0/\">\n         <xmp:ModifyDate>2020-12-07T01:53:39+03:30</xmp:ModifyDate>\n         <xmp:CreateDate>2020-12-07T01:53:39+03:30</xmp:CreateDate>\n         <xmp:CreatorTool>Draw</xmp:CreatorTool>\n         <xmp:MetadataDate>2020-12-07T01:53:48+03:30</xmp:MetadataDate>\n      </rdf:Description>\n      <rdf:Description rdf:about=\"\"\n            xmlns:xapMM=\"http://ns.adobe.com/xap/1.0/mm/\"\n            xmlns:stEvt=\"http://ns.adobe.com/xap/1.0/sType/ResourceEvent#\">\n         <xapMM:DocumentID>urn:uuid:185dbf2b-49d9-4510-9a6d-1ef0f14b6a5c</xapMM:DocumentID>\n         <xapMM:History>\n            <rdf:Seq>\n               <rdf:li rdf:parseType=\"Resource\">\n                  <stEvt:action>converted</stEvt:action>\n                  <stEvt:parameters>from application/pdf to image/vnd.djvu</stEvt:parameters>\n                  <stEvt:instanceID>urn:uuid:6c6d400f-1dda-4a0c-b091-e8e66fb4bf47</stEvt:instanceID>\n                  <stEvt:softwareAgent>pdf2djvu 0.9.17.1 (DjVuLibre 3.5.28, Poppler 20.09.0, GraphicsMagick++ 1.4, Exiv2 0.27.3)</stEvt:softwareAgent>\n                  <stEvt:when>2020-12-07T01:53:48+03:30</stEvt:when>\n               </rdf:li>\n            </rdf:Seq>\n         </xapMM:History>\n         <xapMM:InstanceID>urn:uuid:6c6d400f-1dda-4a0c-b091-e8e66fb4bf47</xapMM:InstanceID>\n         <xapMM:OriginalDocumentID>uuid:3d2f6866-702e-11f6-0000-216ee43aad0a</xapMM:OriginalDocumentID>\n      </rdf:Description>\n      <rdf:Description rdf:about=\"\"\n            xmlns:dc=\"http://purl.org/dc/elements/1.1/\">\n         <dc:format>image/vnd.djvu</dc:format>\n         <dc:title>\n            <rdf:Alt>\n               <rdf:li xml:lang=\"x-default\">Untitled</rdf:li>\n            </rdf:Alt>\n         </dc:title>\n      </rdf:Description>\n   </rdf:RDF>\n</x:xmpmeta>\n")
.
# ------------------------- 
select "p0001.djvu" # page 1
set-txt
(page 0 0 2550 3300
 (line 928 1833 1058 1841
  (word 928 1833 988 1841 "ASIS{_DJVU_f1L3")
  (word 989 1834 1026 1841 "_f0rM4t_iZ")
  (word 1027 1833 1058 1841 "_DejaVu}"))
 (line 552 2637 671 2668
  (word 552 2637 671 2668 "ASIS{"))
 (line 2186 2637 2197 2668
  (word 2186 2637 2197 2668 "}"))
 (line 252 2890 2386 2930
  (word 252 2900 284 2928 "A")
  (word 315 2899 464 2930 "dream")
  (word 497 2899 551 2930 "is")
  (word 587 2899 614 2922 "a")
  (word 648 2899 944 2930 "succession")
  (word 978 2899 1035 2930 "of")
  (word 1069 2890 1264 2930 "images,")
  (word 1310 2892 1475 2930 "ideas,")
  (word 1518 2892 1775 2930 "emotions,")
  (word 1820 2899 1909 2930 "and")
  (word 1942 2899 2235 2930 "sensations")
  (word 2269 2899 2386 2930 "that"))
 (line 253 2840 2388 2880
  (word 253 2840 462 2880 "usually")
  (word 519 2849 666 2872 "occur")
  (word 724 2840 1110 2880 "involuntarily")
  (word 1168 2850 1224 2880 "in")
  (word 1279 2849 1367 2880 "the")
  (word 1422 2849 1544 2880 "mind")
  (word 1598 2840 1777 2880 "during")
  (word 1833 2849 2040 2880 "certain")
  (word 2098 2840 2272 2879 "stages")
  (word 2331 2849 2388 2880 "of"))
 (line 256 2791 422 2831
  (word 256 2791 422 2831 "sleep.")))


```

The flag is : 
**ASIS{_DJVU_f1L3_f0rM4t_iZ_DejaVu}**
