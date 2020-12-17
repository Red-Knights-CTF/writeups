# Anonymous
**category: Forensics**  
**points: 100**

## Description
> Anonymous sended it's another message this year. But everyone doesn't know how they send a secret message through this video to their spy can you able to find it.

## Solution
We are provided with [mp4](video.mp4) file. Listening it on `3:25` we get some noise. I went to https://www.dcode.fr/spectral-analysis to look for `spectogram` on `3:25` and i got the flag there

![](spectogram.png)

FLAG : `hf0x01{FINALLY_Y0U_G0T_S3CR3T_MESSAg3}`
