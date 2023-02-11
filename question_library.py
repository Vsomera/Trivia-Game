from question import Question
import json
import random


class QuestionLibrary:
    def __init__(self, filename="trivia.json"):
        """ Constructor: Reads from json file takes in 1 filename param, default = trivia.json"""
        self.questions = []
        with open(filename, 'r') as file:
            trivia_data = json.load(file)
            for question in trivia_data:
                self.questions.append(Question(**question))
            for q in self.questions:
                print(q.__str__())

    def __len__(self):
        """Allows search for length"""
        return len(self.questions)

    def get_categories(self):
        """ Retursn a list of strings containing all categories from given json file """
        categories = []
        for item in self.questions:
            if item.category not in categories:
                categories.append(item.category)
        return categories

    def get_questions(self, category=None, difficulty=None, number=250):
        """ Gets questions based on user args """
        questions = []
        # ensures arg is a valid category
        if category not in self.get_categories():
            category = self.get_categories()
        # checks if arg is a valid difficulty
        if difficulty not in ["easy", "medium", "hard"]:
            difficulty = ["easy", "medium", "hard"]

        random.shuffle(self.questions)
        for item in self.questions:
            if item.category in category and item.difficulty in difficulty:
                if (len(questions) < number) and (item not in questions):
                    questions.append(item)
                else:
                    break
        return questions


QuestionLibrary()
