#!/usr/bin/python2.7

import argparse
from src.core.questionnaire import Questionnaire

def getCommandLineArguments():
	"""
	Manages command line arguments and information.

	:return: Object containing arguments and values.
	"""
	parser = argparse.ArgumentParser(description="Clinical Trial Eligibility Questionnaire")
	return parser.parse_args()

def main():
	print "Welcome to the clinical trial eligibility questionnaire!\n"

	# Get any command line arguments supplied
	commandLineArguments = getCommandLineArguments()

	# Start the questionnaire
	Questionnaire().start()

if __name__ == '__main__':
	main()
