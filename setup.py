from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

LONG_DESCRIPTION    = """Aggregate pairwise comparisons."""
NAME                = 'pairwise'
DESCRIPTION         = 'Aggregate pairwise comparisons.'
MAINTAINER          = 'Allen B. Riddell',
MAINTAINER_EMAIL    = 'abr@ariddell.org',
URL                 = 'https://github.com/ariddell/pairwise'
LICENSE             = 'GPLv3'

MAJOR = 0
MINOR = 9
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=MAINTAINER,
      author_email=MAINTAINER_EMAIL,
      py_modules=['pairwise'],
      scripts=['pairwise-ballot.py'],
      license=LICENSE,
      url=URL,
      platforms='any')
