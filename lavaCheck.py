#!/usr/bin/env python
import os
import sys
import logging
from lavaCheck.plugins import *
from lavaCheck.modules import *



class Check(object):
	pass

def NodeSoftFail(Exception):
	pass

def NodeHardFail(Exception):
	pass

def JobSoftFail(Exception):
	pass

def JobHardFail(Exception):
	pass

def run_tests(mode):
	log=logging.getLogger("main.%s" % mode)
	if mode not in ("pre","post"):
		raise ValueError("Invalid mode specified: %s" % mode)
	log.info("Starting %s execution run")
	for plugin in get_subclasses(Check):
		log.info("Creating instance of %s" % plugin)
		test=plugin()
		try:
			getattr(test,mode)()
		except JobHardFail:
			pass
		except JobSoftFail:
			pass
		except NodeSoftFail:
			pass
		except NodeHardFail:
			pass
		except:
			pass

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
