import sys
from os.path import realpath, dirname, join

# mkbootimg.py imports gki which is in ./gki/. This will not work when
# mkbootimg is used as a package unless we add ./ to the paths searched by
# Python for top-level packages.
sys.path.append(realpath(join(dirname(__file__))))
