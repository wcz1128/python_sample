#!/usr/bin/python
#coding:utf8
'for my av'
__author__ = 'Hippo'

import struct



pad = struct.pack('!If',10240099,3.3)
print pad
i,f = struct.unpack('!If', pad)
print hex(i),f








'''
Character       Byte order              Size        Alignment
@               native                  native      native
=               native                  standard    none
<               little-endian           standard    none
>               big-endian              standard    none
!               network (= big-endian)  standard    none



Format      C Type              Python type         Standard size       Notes
x           pad byte            no value
c           char                bytes of length 1   1
b           signed char         integer             1                   (1),(3)
B           unsigned char       integer             1                   (3)
?           _Bool               bool                1                   (1)
h           short               integer             2                   (3)
H           unsigned short      integer             2                   (3)
i           int                 integer             4                   (3)
I           unsigned int        integer             4                   (3)
l           long                integer             4                   (3)
L           unsigned long       integer             4                   (3)
q           long long           integer             8                   (2), (3)
Q           unsigned long long  integer             8                   (2), (3)
n           ssize_t             integer                                 (4)
N           size_t              integer                                 (4)
e           (7)                 float               2                   (5)
f           float               float               4                   (5)
d           double              float               8                   (5)
s           char[]              bytes
p           char[]              bytes
P           void *              integer                                 (6)



Notes:
    1.  The '?' conversion code corresponds to the _Bool type defined by C99. If this type is not available, it is simulated using a char. In standard
    mode, it is always represented by one byte.
    
    2.  The 'q' and 'Q' conversion codes are available in native mode only if the platform C compiler supports C long long, or, on Windows, __int64.
    They are always available in standard modes.

    3.  When attempting to pack a non-integer using any of the integer conversion codes, if the non-integer has a __index__() method then that method
    is called to convert the argument to an integer before packing.
    Changed in version 3.2: Use of the __index__() method for non-integers is new in 3.2.

    4.  The 'n' and 'N' conversion codes are only available for the native size (selected as the default or with the '@' byte order character). For the
    standard size, you can use whichever of the other integer formats fits your application.

    5.  For the 'f', 'd' and 'e' conversion codes, the packed representation uses the IEEE 754 binary32, binary64 or binary16 format (for 'f', 'd' or
    'e' respectively), regardless of the floating-point format used by the platform.

    6.  The 'P' format character is only available for the native byte ordering (selected as the default or with the '@' byte order character). The
    byte order character '=' chooses to use little- or big-endian ordering based on the host system. The struct module does not interpret this as
    native ordering, so the 'P' format is not available.

    7.  The IEEE 754 binary16 “half precision” type was introduced in the 2008 revision of the IEEE 754 standard. It has a sign bit, a 5-bit exponent
    and 11-bit precision (with 10 bits explicitly stored), and can represent numbers between approximately 6.1e-05 and 6.5e+04 at full precision.
    This type is not widely supported by C compilers: on a typical machine, an unsigned short can be used for storage, but not for math operations.
    See the Wikipedia page on the half-precision floating-point format for more information.

'''
