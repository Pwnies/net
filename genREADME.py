#!/usr/bin/env python2.7
import re
def expand(src, dst):
  outfd = file(dst, 'w')
  infds = [file(src)]
  while infds:
    fd = infds[-1]
    line = fd.readline()
    if not line:
      fd.close()
      infds.pop()
      continue

    m = re.match(r'^#include\s+(["\'])(.+?)\1$', line)
    if m:
      inc = m.group(2)
      infds.append(file(inc))
    else:
      outfd.write(line)

expand('README-template.md', 'README.md')
