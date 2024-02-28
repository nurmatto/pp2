#!/usr/bin/env python3

import re

nurma = re.compile(r"[a-z]+_[a-z]+")
print(nurma.findall("iamma_show_you_how_great_iam"))