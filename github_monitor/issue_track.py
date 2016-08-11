# -*- coding: utf-8 -*-
from urllib.request import urlopen
import re

PATTERN_WANTED = '文章认领'
PATTERN_CHECK = '校对认领'
target = 'https://api.github.com/repos/xitu/gold-miner/issues'

with urlopen(target) as res:
    wanted, need_checker = 0, 0
    json_str = str(res.read().decode('utf-8'))
    result = re.findall(PATTERN_WANTED, json_str)
    wanted = len(result)
    result = re.findall(PATTERN_CHECK, json_str)
    need_checker = len(result)
    import os
    os.system('say "Captain! Now we need {} checkers and {} translators."'.format(need_checker, wanted))
