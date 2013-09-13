# Copyright 2013 David Irvine
#
# This file is part of LavaCheck
#
# LavaCheck is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# LavaCheck is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LavaCheck. If not, see <http://www.gnu.org/licenses/>.
#
import os
from lavaCheck.generic import *
class CheckTmpDir(Check):
	def pre(self):
		try:
			tmpdir=os.environ["TMPDIR"]
		except KeyError:
			tmpdir="/tmp"
			self.log.debug("TMPDIR not defined, defaulting to: %s" % tmpdir)
		if not os.path.isdir(tmpdir):
			raise NodeSoftFailError("TMPDIR: %s is not a directory." % tmpdir)
		if tmpdir == "/tmp":
			perms=oct(os.stat(tmpdir).st_mode)[-4:]
			if perms != '1777':
				raise NodeHardFailError("Invalid perisions %s for directory: %s" % (perms, tmpdir))
