import argparse
import os.path
import random

parser = argparse.ArgumentParser("moon_picker")
parser.add_argument(
  "-i",
  "--input",
  type=str,
  default="vanilla.csv",
  help="The CSV input file from which moon data is read. Each line defines a single moon and must contain two values: the moon's name and its cost respectively. If no input option is provided, 'vanilla.csv' in the current directory will be used instead."
)
parser.add_argument(
  "-c",
  "--credit",
  type=int,
  default="-1",
  help="The current amount of money that your crew possesses. Any moon whose cost exceeds your savings will be ignored so that you are guaranteed to get a moon you can pay for."
)
args = parser.parse_args()

CREDIT = args.credit
FILE_PATH = args.input

if(not os.path.isfile(FILE_PATH)):
  print("❌ File at the specified "+FILE_PATH+" path couldn't be found.")
  quit()

moons = []
with open(FILE_PATH) as file:
  for line in file:
    [moon,cost] = line.split(",")

    if(moon == "" or cost == ""):
      print("⚠️ Invalid line detected, skipping line...")
      continue

    cost = cost.replace("\n","").strip()
    if(not cost.isdigit()):
      print("⚠️ Cost value (\""+cost+"\") is not a number, skipping line...")
      continue

    cost = int(cost)
    if(CREDIT == -1 or CREDIT >= cost):
      moons.append(moon)
  
if(len(moons) == 0):
  print("❌ No moon could be found in the file. Please check the format and try again...")
  quit()

moonIndex = random.randint(0,len(moons)-1)
print("✅🌑 You are going to...   " + moons[moonIndex] + "!")