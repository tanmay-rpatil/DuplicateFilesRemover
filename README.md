# DuplicateFilesRemover
A python scipt that scans for dupicates files between two folders and removes them.

Currently tested in linux (Ubuntu 20.04), with Python 3.8

# To run

	1. Enter absolute path of directories to be scanned ( Open the directory in terminal and type pwd to get absolute path)
	2. If duplicates are found, enter 'y' to delete duplicates from the secodary directory, 'n' to cancel deletion.

# NOTES

	1. Currently doesn't account for the fact that one of the two dirs maybe sub directories, hence may delete the original versions of the files - working on a fix.
	2. Use it at your own risk - currently in development phase, try it on dummy files at the moment.