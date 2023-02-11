from question_library import QuestionLibrary


class Game:
    def __init__(self, filename="trivia.json", category=None, difficulty=None, number=250):
        self.library = QuestionLibrary(filename)
        self.questions = self.library.get_questions(
            category, difficulty, number)
        self.score = 0 

    def play(self):
        """ Loops through each iteration of the game """
        for question in self.questions:
            print(question.question) 
            print(question.answers)  
            print(f'Difficulty: {question.difficulty}')

            while True:  
            # Loops to confirm user input is valid
                player_input = input("Enter correct answer: ")
                if player_input in ["1", "2", "3", "4"]:
                    player_input = int(player_input)
                    break
                print("Invalid input: Enter a number between 1 - 4")

            
            score_increment = 1 if question.difficulty == 'easy' else 2 if question.difficulty == 'medium' else 3
            if player_input == question.answer_id: 
                self.score += score_increment
                print("Correct!")
                print(f'You\'re score is {self.score}')  
            else:  
            # If answer is incorrect: display the correct answer
                print("That is incorrect")
                print(
                    f'The correct answer was {question.answers[question.answer_id - 1]}')
                print(f'You\'re score is {self.score}') 
