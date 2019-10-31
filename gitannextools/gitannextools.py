# GitAnnexTools - utilities to aid working with git-annex repos
#
# Copyright (C) 2017  Silvio Ankermann
#
# This program is free software: you can redistribute it and/or modify it under the terms of version 3 of the GNU
# General Public License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be uselful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import int
from builtins import str
from future import standard_library
standard_library.install_aliases()
from future.utils import with_metaclass
from builtins import object


from abc import ABCMeta, abstractmethod

import sys
import string

