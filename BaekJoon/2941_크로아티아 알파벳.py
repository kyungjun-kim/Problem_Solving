# 문제 링크 : https://www.acmicpc.net/problem/5622

import re
a = 'dz=ak'
print(len(re.sub('c=|c-|dz=|d-|lj|nj|s=|z=','_',a).replace("_",''))+re.sub('c=|c-|dz=|d-|lj|nj|s=|z=','_',a).count("_"))