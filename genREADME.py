#!/usr/bin/env python3
import re
import subprocess

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

    m = re.match(r'^#(\w+)\s+(["\'])(.+?)\2$', line)
    if m:
      cmd = m.group(1)
      arg = m.group(3)
      if cmd == 'shell':
        p = subprocess.Popen(
          arg,
          shell=True,
          stdin=file('/dev/null'),
          stdout=subprocess.PIPE,
          stderr=subprocess.STDOUT,
        )
        fd = p.stdout
      elif cmd == 'include':
        fd = file(arg)
      else:
        outfd.write(line)
        continue
      infds.append(fd)
    else:
      outfd.write(line)

expand('README-template.md', 'README.md')
