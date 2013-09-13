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
import logging
class Check(object):
	def __init__(self):
		self.log=logging.getLogger(self.__class__.__name__)
	def pre(self):
		pass
	def post(self):
		pass
class NodeSoftFailError(Exception):
	pass

class NodeHardFailError(Exception):
	pass

class JobSoftFailError(Exception):
	pass

class JobHardFailError(Exception):
	pass

