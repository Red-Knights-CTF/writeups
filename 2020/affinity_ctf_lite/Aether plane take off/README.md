# Writeup: Aether Plane Take off :triangular_flag_on_post:

***Category : Forensic***:minidisc:\
***Points : 725***\
***Author : Angel Barre (Skynet)*** \
***Team : Red-Knights***:warning:

![forense](https://img.shields.io/badge/analitycs-forensic-green) ![play](https://img.shields.io/badge/Play-CTF-red)

## Description
> We managed to intercept the signal from the mole that shifted the phase with some keys 31 minutes ago. Can you help us read it?
- [file](https://github.com/Red-Knights-CTF/writeups/blob/master/2020/affinity_ctf_lite/Aether%20plane%20take%20off/aether_plane_take_off.wav)

First we start by doing a `file` to the file to verify that it is a wav file and not another fileFirst we start by doing a file to the file to verify that it is a wav file and not another file.
```
file aether_plane_take_off.wav
```
It is indeed wav file

Now let's strings to the wav file to check that it doesn't have some loose data
```
strings aether_plane_take_off.wav
```
I did not find anything interesting let's see by other means.
<!-- --------------- -->

## Analysis  📦

- [x] Sonic-visualizer
- [x] Audacity

We analyze the file in those two programs to analyze audio files after the analysis I find nothing interesting! Until now.

Analyzing the file a little more and googling a bit I was able to find the PSK31 encryption.

# What is PSK31 encoding?

>The PSK31 is a digital mode where the information is encoded in the phase of the signal, unlike other digital modes such as RTTY where the encoding is in the frequency (AFSK or FS)

>The signal is modulated in such a way that it occupies only 31 Hz of bandwidth, hence the name of the mode (PSK 31)



<!-- --------------- -->
## PSK31 analysis :computer:

| PSK31 | 
| :--------------- | 
| RTTY         |
| 31 Hz         |

## Decoding PSK31 :radio:

Looking for ways to decode PSK31 I found a `fldigi` program, its use is the following: ` Download fldigi` >  `Upload File` > `Playback`

- [Download fldigi](http://www.w1hkj.com/files/fldigi)

## Result :smile:

![fldigi](figidi-result.png)


```
Flag : AFFCTF{PSKPSKSPK31}
```
