import argparse
import os.path

parser = argparse.ArgumentParser("moon_picker")
parser.add_argument("-i", "--input", help="The CSV input file from which moon data is read. Each line defines a single moon and must contain two values: the moon's name and its cost respectively. If no input option is provided, 'vanilla.csv' in the current directory will be used instead.")
parser.add_argument("-c","--credit", help="The current amount of money that your crew possesses. Any moon whose cost exceeds your savings will be ignored so that you are guaranteed to get a moon you can pay for.")
args = parser.parse_args()

CREDIT = int(0 if args.credit == None else args.credit)
FILE_PATH = args.input or "vanilla.csv"

if(not os.path.isfile(FILE_PATH)):
  print("❌ File at the specified "+FILE_PATH+" path couldn't be found.")
  quit()
