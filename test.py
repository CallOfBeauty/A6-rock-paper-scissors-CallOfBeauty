######################################################################
# Authors: Dimitrios Ntentia
# Username: ntentiad
#
# Assignment: A06
# Purpose:  Test suite
#
######################################################################

import sys

from RPSLS import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6

    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def a06_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the willaby_wallaby() function.

    :return: None
    """
    print("\nRunning the funky_functions_test_suite()).")
    ##########################################
    testit(winner("rock", "paper") == "computer")
    testit(winner("paper", "rock") == "human")

    print("\nEnding of the test")


def main():
    """
    :return: None
    """
    a06_suite()


if __name__ == "__main__":
    main()



winningpairs=[["rock","scissors"],["rock", "lizzard"],["paper", "rock"],["paper", "spock"],["scissors", "lizard"],["scissors", "paper"],["spock", "scissors"],["spock", "rock"],["lizard", "spock"],["lizard", "paper"]]
for i in winningpairs:
    k=str(i[0])+str(i[1])
    l="rockscissos"
    if k == l:
        print("hi")