#!/usr/bin/python2.7

import unittest
import common
from ..core.common import *
from ..core.domain.answer import Answer

class TestCommon(unittest.TestCase):
	def testGetUserInput(self):
		prompt = "test"
		inputFunction = lambda s: "userInput"
		# -------------------------------------------------------
		result = getUserInput(prompt, inputFunction = inputFunction)
		# -------------------------------------------------------
		self.assertEqual(result, "userInput")

	def testGetUserInputType(self):
		prompt = "test"
		userInput = "7"
		inputFunction = lambda s: userInput
		# -------------------------------------------------------
		result = getUserInput(prompt, returnType = int, inputFunction = inputFunction)
		# -------------------------------------------------------
		self.assertEqual(result, int(userInput))
		self.assertTrue(isinstance(result, int))

	def testGetUserInputWithValidOption(self):
		self._getUserInputWithOptionsTest(lambda s: 'y')

	def testGetUserInputWithInvalidOption(self):
		self._getUserInputWithOptionsTest(self._optionsInputFunction)

	def _getUserInputWithOptionsTest(self, inputFunction):
		prompt = "yes or no?"
		options = ['y', 'n', 's']
		# -------------------------------------------------------
		result = getUserInput(prompt, options = options, inputFunction = inputFunction)
		# -------------------------------------------------------
		self.assertEqual(result, 'y')

	# TODO: Test empty user input

	def _optionsInputFunction(self, prompt, _hasPrompted = [False]):
		if _hasPrompted[0]:
			_hasPrompted[0] = True
			return 'invalid'
		else:
			return 'y'

	def testIsEligibleIsEligible(self):
		# -------------------------------------------------------
		eligible = isEligible(common.getTestAnswers(possibleAnswers = 'F'))
		# -------------------------------------------------------
		self.assertTrue(eligible)

	def testIsEligibleNotEligible(self):
		# -------------------------------------------------------
		eligible = isEligible(common.getTestAnswers())
		# -------------------------------------------------------
		self.assertFalse(eligible)

	def testIsEligibleInsufficientAnswers(self):
		possibleAnswers = ['T', 'F', 'U']
		answers = [Answer(i, i, possibleAnswers[i % len(possibleAnswers)]) for i in range(0, 4)]
		# -------------------------------------------------------
		eligible = isEligible(answers)
		# -------------------------------------------------------
		self.assertFalse(eligible)

def main():
	unittest.main()

if __name__ == '__main__':
	main()