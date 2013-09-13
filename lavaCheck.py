#!/usr/bin/env python
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
import sys
import logging
from lavaCheck.generic import *
from lavaCheck.plugins import *
from lavaCheck.modules import *


def run_tests(mode):
	logging.basicConfig()
	log=logging.getLogger("main.%s" % mode)
	if mode not in ("pre","post"):
		raise ValueError("Invalid mode specified: %s" % mode)
	log.info("Starting %s execution run")
	for plugin in get_subclasses(Check):
		log.info("Creating instance of %s" % plugin)
		test=plugin()
		try:
			getattr(test,mode)()
		except JobHardFailError:
			logging.error("Test: %s raised JobHardFailError. Exiting witn  ode (-1" % test)
			sys.exit(-1)
		except JobSoftFailError:
			logging.error("Test: %s raised JobSoftFailError. Exiting with code -3" % test)
			sys.exit(-3)
			pass
		except NodeSoftFailError:
			logging.error("Test: %s raised NodeSoftFailError. Exiting with code -4" % test)
			sys.exit(-4)
		except NodeHardFailError:
			logging.error("Test: %s raised NodeHardFailError. Exiting with code -2" % test)
			sys.exit(-2)
		except Exception as e:
			logging.exception("Test: %s has generated the following exception: %s" % ( test, e))
		logging.info("%s-execution completed successfully" % mode)

def get_subclasses(c):
	subclasses = c.__subclasses__()
	for d in list(subclasses):
		subclasses.extend(get_subclasses(d))
	return subclasses
    
if os.path.basename(__file__) == "pre.py":
	run_tests("pre")
elif os.path.basename(__file__) =="post.py":
	run_tests("post")
else:
	raise ValueError("Unable to determine role: %s" % os.path.basename(__file__))
sys.exit(0)

