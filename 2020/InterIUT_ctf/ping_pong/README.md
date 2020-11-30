# Ping! pong!
**category: forensics**  
**score: ?**

## Description
Given a .pcapng file, find the flag.

## Solution
First, lets take a look at the packets.
```
$ tshark -r ping_pong.pcapng
    1 0.000000000     10.5.0.2 → 10.5.0.3     ICMP 45 Echo (ping) request  id=0x0123, seq=0/0, ttl=64
    2 0.000049302     10.5.0.3 → 10.5.0.2     ICMP 45 Echo (ping) reply    id=0x0123, seq=0/0, ttl=64 (request in 1)
    3 1.075985187     10.5.0.2 → 10.5.0.3     ICMP 45 Echo (ping) request  id=0x0123, seq=0/0, ttl=64
    4 1.076089068     10.5.0.3 → 10.5.0.2     ICMP 45 Echo (ping) reply    id=0x0123, seq=0/0, ttl=64 (request in 3)
    5 2.139551863     10.5.0.2 → 10.5.0.3     ICMP 45 Echo (ping) request  id=0x0123, seq=0/0, ttl=64
    6 2.139657099     10.5.0.3 → 10.5.0.2     ICMP 45 Echo (ping) reply    id=0x0123, seq=0/0, ttl=64 (request in 5)
    7 3.207655238     10.5.0.2 → 10.5.0.3     ICMP 45 Echo (ping) request  id=0x0123, seq=0/0, ttl=64
    8 3.207781748     10.5.0.3 → 10.5.0.2     ICMP 45 Echo (ping) reply    id=0x0123, seq=0/0, ttl=64 (request in 7)
    9 4.253002521     10.5.0.2 → 10.5.0.3     ICMP 45 Echo (ping) request  id=0x0123, seq=0/0, ttl=64
   10 4.253103699     10.5.0.3 → 10.5.0.2     ICMP 45 Echo (ping) reply    id=0x0123, seq=0/0, ttl=64 (request in 9)
   11 5.302315828     10.5.0.2 → 10.5.0.3     ICMP 45 Echo (ping) request  id=0x0123, seq=0/0, ttl=64
   12 5.302436526     10.5.0.3 → 10.5.0.2     ICMP 45 Echo (ping) reply    id=0x0123, seq=0/0, ttl=64 (request in 11)
   ...
```
We can see that all of the packets are sent by the same two devices, and all of them use the ICMP protocol. Then, we can use this
filter to get the data being sent.
```
$ tshark -r ping_pong.pcapng -T fields -e data.data
48
48
32
32
47
47
32
32
7b
7b
...
```
The output looks like hexadecimal, and each line is duplicated. Here is a bash one-liner to remove the duplicates and decode the bytes.
```
$ echo $(tshark -r ping_pong.pcapng -T fields -e data.data | sed 'n; d' | xxd -r -p)
```
FLAG - `H2G2{y0u_r34lly_7h1nk_y0u'r3_60nn4_b3_4bl3_70_c0py_7h3_fl46_m4nu4lly?_y0u'd_b3773r_m4k3_4_5cr1p7_70_3x7r4c7_7h15_v3ry_v3ry_v3ry_v3ry_l0000000nnnnnnnnnnnnnnn666666666_fl46_7h47_y0u'll_n3v3r_h4v3_71m3_70_c0py!_l0r3m_1p5um_d0l0r_517_4m37,_c0n53c737ur_4d1p15c1n6_3l17,_53d_d0_31u5m0d_73mp0r_1nc1d1dun7_u7_l4b0r3_37_d0l0r3_m46n4_4l1qu4._u7_3n1m_4d_m1n1m_v3n14m,_qu15_n057rud_3x3rc174710n_ull4mc0_l4b0r15_n151_u7_4l1qu1p_3x_34_c0mm0d0_c0n53qu47._du15_4u73_1rur3_d0l0r_1n_r3pr3h3nd3r17_1n_v0lup7473_v3l17_3553_c1llum_v3r174715_37_qu451_4rch173c70_b34743_v1743_d1c74_5un7_3xpl1c4b0._n3m0_3n1m_1p54m_v0lup7473m_qu14_v0lup745_517_45p3rn47ur_4u7_0d17_4u7_fu617,_53d_qu14}
`
