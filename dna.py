from sys import exit, argv
import csv
from csv import DictReader


def main():
    # Proper Number of Command Line Arguments
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit()

    # Open CSV into memory
    sequences = []
    profiles = []

    with open(argv[1], mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        sequences = reader.fieldnames[1:]
        # Populate profiles with the lists of each person and their STR counts
        for row in reader:
            profiles.append(row)

    # Create STR count dictionary
    str_count = dict.fromkeys(sequences, 0)

    # Open txt file into memory
    with open(argv[2], mode="r") as txt_file:
        s = txt_file.readline()
        # Populate sequence header dictionary with counts of repeats
        for sequence in sequences:
            str_count[sequence] = max_repeats(s, sequence)

    # Check to see if str_count matches any of the profiles
    for profile in profiles:
        counter = 0

        # If each count for each sequence matches btwn the profile you're looking at and the txt string, then increment counter, else, check next one
        for sequence in sequences:
            if int(profile[sequence]) == str_count[sequence]:
                counter += 1
            else:
                continue

        if counter == len(sequences):
            print(profile['name'])
            exit()

    print("No match")
    exit()


def max_repeats(s, substring):
    # calc max number of repeats in a substring
    # Iterate through string from end, if you find a substring in string which matches the substring, update longeststreak with the number of repeats

    i = 0
    streak = 0
    longeststreak = 0
    while i < len(s):
        if s[i: i + len(substring)] == substring:
            streak += 1
            i = i + len(substring)
        else:
            i = i + 1
            if longeststreak < streak:
                longeststreak = streak
                streak = 0
            else:
                streak = 0
    return longeststreak


if __name__ == "__main__":
    main()