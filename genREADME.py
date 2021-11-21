#!/usr/bin/env python3
import re
import subprocess

def expand(src, dst):
  outfd = open(dst, 'w')
  infds = [open(src)]
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
          stdin=open('/dev/null'),
          stdout=subprocess.PIPE,
          stderr=subprocess.STDOUT,
          text=True,
        )
        fd = p.stdout
      elif cmd == 'include':
        fd = open(arg)
      else:
        outfd.write(line)
        continue
      infds.append(fd)
    else:
      outfd.write(line)

expand('README-template.md', 'README.md')
