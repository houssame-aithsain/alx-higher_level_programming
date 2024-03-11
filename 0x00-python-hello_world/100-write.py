#!/usr/bin/python
import os
data = "and that piece of art is useful - Dora Korpar, 2015-10-19".encode('utf-8')
os.write(2, data)
exit(1)
