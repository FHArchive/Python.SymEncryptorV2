"""
Author Kieran
Year 2017

This is an symmetric encryption algorithm. It is a more glorified version of a
substitution cipher. However,  some substitutions are added that do not
correspond to a letter to try and confuse anyone trying to break the cipher
"""

# ENCRYPTOR V2.2.2
# Kieran (MIT License)

"""
Being pseudorandom, the random library perhaps isn't the best for an encryption
machine but this is more proof of concept
"""
import random
systemRandom = random.SystemRandom()

# THE ALPHABET OR TABLE THAT THIS PROGERM REFERS TO
"""
The allowed alphabet is fairly minimal, any lowercase character is converted to
uppercase. The only punctuation allowed is '.' and ' ' to improve readability of
the output
"""
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
			'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', '0', '1', '2', '3', '4', '5',
			'6', '7', '8', '9']

# THE ENCRYPTION KEYS
encryptionKeyA = ['KYL', 'JTD', 'RXQ', 'WEF', 'BRG', 'AWS', 'LHM', 'KWK', 'UIK',
				  'EHQ', 'GVT', 'UKE', 'WLV', 'HGI', 'KRI', 'PUE', 'HJB', 'FVL',
				  'ORQ', 'ROD', 'JKH', 'QOT', 'QLU', 'YSJ', 'JNT', 'PBC', 'HNC',
				  'YSG', 'NKI', 'SGU', 'OXG', 'WCG', 'HAB', 'GVC', 'UEJ', 'SGB',
				  'SWE', 'YKX']
encryptionKeyB = ['IDY', 'CBS', 'YSP', 'HTA', 'IGR', 'OBH', 'QEY', 'HCQ', 'RWB',
				  'CJC', 'RRD', 'MDO', 'JIF', 'QHH', 'MYL', 'NLK', 'PIB', 'SMD',
				  'HNH', 'LBD', 'CIY', 'SXE', 'AEW', 'LFV', 'MVV', 'YQU', 'WUI',
				  'LRW', 'UYY', 'RUC', 'SUR', 'OOR', 'WQE', 'KAX', 'LFB', 'XBO',
				  'GWF', 'WSY']
falseEncryption = ['EQS', 'NPO', 'PKA', 'FGA', 'BWR', 'PIE', 'IFE', 'GUM', 'XIN',
				   'EHT', 'MDU', 'CAX', 'OBY', 'MQP', 'PYF', 'PVI', 'GOS', 'YYG',
				   'FTQ', 'NDT', 'YHK', 'JVJ', 'NPV', 'BHE', 'JLJ', 'DUN', 'EPU',
				   'RKX', 'LOM', 'HVD', 'GIG', 'KRE', 'VVJ', 'HFY', 'QJU', 'VXB',
				   'OIF', 'XCE']

# RUN AGAIN - THE MODULAR FUNCTION TO ASK THE USER WHETHER THEY WOULD LIKE TO
# RUN THE CODE AGAIN
def runAgain(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption):

	try:
		play = str(input("\nWould you like to run again? \n\n>>>"))
		play = play.lower()
		play = play[0]
	except:
		print("\n!PLEASE TYPE 'YES' OR 'NO'!")
		runAgain(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)
	if play == "y":
		main(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)
	elif play == "n":
		print("Ok")
	else:
		print("\n!PLEASE TYPE 'YES' OR 'NO'!")
		runAgain(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)

# THE ENCRYPTION PROCESS
def encrypt(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption):
	# Get user input
	string = input("\nPlease input the message to encrypt \n\n>>>")
	string = string.upper()
	# The encrypted text
	new = ""
	for x in range(len(string)):
		for i in range(38):
			# Text the character is in the allowed alphabet
			if string[x] == alphabet[i]:
				encryptChoice = systemRandom.randint(0, 1)
				if encryptChoice == 0:
					new = new + encryptionKeyA[i]
				elif encryptChoice == 1:
					new = new + encryptionKeyB[i]
				# Add a random element from the false key
				new = new + falseEncryption[systemRandom.randint(0, 26)]
	print("\nHere is the new, encrypted message:\n\n"+new)
	runAgain(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)

# THE DECODING PROCESS
def decode(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption):
	# Get user input
	string = input("\nPlease input the message to decode as it was printed exactly \n\n>>>")
	string = string.upper()
	# The decoded text
	new = ""
	for x in range(int(len(string)/3)):
		for i in range(38):
			# Select the next 'chunk' of text and decrypt
			if string[x*3:(x*3)+3] == encryptionKeyA[i]:
				new = new + alphabet[i]
			elif string[x*3:(x*3)+3] == encryptionKeyB[i]:
				new = new + alphabet[i]
	print("\nHere is the original, decoded message:\n\n"+new)
	runAgain(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)

# THE MENU FOR THE PROGRAM
def main(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption):

	print("\nMain Menu:")
	print("Enter the number represented in the brackets to use the function.")
	try:
		mode = int(input("\nFunctions:\nEncrypt(0) \nDecode(1) \n\n>>>"))
		if mode == 0:
			encrypt(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)
		elif mode == 1:
			decode(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)
	except:
		print("\n!PLEASE INPUT 0 TO ENCRYPT OR 1 TO DECODE!")
		main(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)

# THE INITIAL STARTUP PROCESS,  SEPARATE FROM THE MENU SO IT ONLY RUNS ONCE
def preStart(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption):

	print("Welcome to the encryption machine version 2.2.2!")
	print("Designed and developed by Kieran.")
	main(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)

# THE COMMAND EXECUTED TO START THE PROGRAM
preStart(alphabet, encryptionKeyA, encryptionKeyB, falseEncryption)
