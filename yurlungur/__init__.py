from __future__ import print_function, unicode_literals, absolute_import
import sys
assert sys.version_info > (2, 7), ('yurlungur currently requires Python 2.7 later')
sys.dont_write_bytecode = True

# yurlungur
from yurlungur.core import * # noQA
from yurlungur.tool import qt
from yurlungur.tool.meta import meta
from yurlungur.tool.util import cache, trace, timer
from yurlungur.tool.math import YVector, YMatrix, YColor

__all__ = []
__version__ = "0.9.2"
name = __name__
version = __version__

# logger
from logging import basicConfig, getLogger, StreamHandler, DEBUG
basicConfig(level=DEBUG)
logger = getLogger(name)
handle = StreamHandler()
logger.addHandler(handle)
