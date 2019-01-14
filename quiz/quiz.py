def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option
    
def ask_questions():
    # create empty arrays for questions and answers
    questions = []
    answers = []
    
    # open questions file and split each line to be read individually
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
    
    # enumerate the individual lines and seperate them 
    # into question / answer category
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    # get number of questions
    number_of_questions = len(questions)
    # pair question and answer key/values
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
    
    # print question and check if it's correct
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print ("Correct")
            print (score)
        else:
            print("Wrong")
    
    # after all questions have been asked, print score total
    print("You answered {0} out of {1} correctly".format(score, number_of_questions))
    
def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("OK, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    # open file and append question and answer to end of file
    # before closing
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
def game_loop():
    while (True):
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")



game_loop()