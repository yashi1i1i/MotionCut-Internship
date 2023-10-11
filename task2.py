#importing the time module
import time
import random
#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#here we set the secret. You can select any word to play with.
words = [
    "academic", "education", "learning", "teaching", "research",
    "scholarship", "curriculum", "instructor", "professor", "student",
    "classroom", "lecture", "study", "knowledge", "university",
    "college", "school", "academia", "degree", "thesis",
    "dissertation", "coursework", "semester", "academician", "pedagogy",
    "syllabus", "intellectual", "literature", "lecture", "assignment",
    "textbook", "exam", "grading", "homework", "essay",
    "paper", "publication", "library", "citation", "reference",
    "plagiarism", "scholar", "academic writing", "critical thinking", "researcher",
    "conference", "peer review", "academic journal", "graduate", "undergraduate",
    "postgraduate", "scholastic", "academic year", "professorship", "department",
    "faculty", "adviser", "mentor", "study group", "study materials",
    "lecture hall", "attendance", "graduation", "valedictorian", "thesis defense",
    "classmate", "transcript", "tutor", "alumni", "classical education",
    "distance learning", "online courses", "academic discipline", "academic probation",
    "academic advising", "campus", "extracurricular activities", "academic achievement", "student council",
    "grading system", "oral presentation", "academic calendar", "academic achievement", "tuition",
    "scholarship", "student loans", "academic advisor", "academic conference", "academic research",
    "academic institution", "academic program", "academic rigor", "academic standards", "academic success",
    "academic support", "academic excellence", "academic record", "academic standing", "academic probation",
    "academic integrity", "academic progress", "academic requirement", "academic scholarship", "academic suspension",
    "academic transcript", "academic year", "academic department", "academic conference", "academic journal",
    "academic discipline", "academic library", "academic paper", "academic publication", "academic writing"
]

word= random.choice(words)
#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

    # see if the character is in the players guess
        if char in guesses:

        # print then out the character
            print (char,end=""),

        else:

        # if not found, print a dash
            print ("_",end=""),

        # and increase the failed counter with one
            failed += 1

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print ("You won")
    # exit the script
        break
    # ask the user go guess a character
    guess = input("guess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

     # turns counter decreases with 1 (now 9)
        turns -= 1

    # print wrong
        print ("Wrong")

    # how many turns are left
        print ("You have", + turns, 'more guesses' )

    # if the turns are equal to zero
        if turns == 0:

        # print "You Lose"
            print ("You Lose"  )
