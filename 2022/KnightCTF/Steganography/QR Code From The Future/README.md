# QR Code From The Future

**Category**: Steganography \
**Points**: 25

## Description

> The following file was found in a device from a crashed UFO. Can you solve that mystery?

![](que.png)
## Solution
Given file is [QR_Code_From_The_Future.gif](QR_Code_From_The_Future.gif)

![](QR_Code_From_The_Future.gif)

It's a gif made with lot of qr code images

Run the code below to extract all images from the gif to img folder

```bash
mkdir img && gm convert QR_Code_From_The_Future.gif -coalesce +adjoin ./img/%3d.png
```

I used my qrcan tool(https://github.com/sky9262/qrcan)

```bash
python3 qrcan.py ./img/
```

Got `}pvznalq_bg_pvgngf_zbes_qriybir_gbt_rqbp_ED{SGPX`

It looks like reversed rot13

[Just decode with cyberchef.](https://gchq.github.io/CyberChef/#recipe=Reverse('Character')ROT13(true,true,false,13)&input=fXB2em5hbHFfYmdfcHZnbmdmX3piZXNfcXJpeWJpcl9nYnRfcnFicF9FRHtTR1BYCg)

# Flag is `KCTF{QR_code_got_evolved_from_static_to_dynamic}`


