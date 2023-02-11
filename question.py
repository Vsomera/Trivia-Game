import random


class Question:
    def __init__(self, question: str, correct_answer: str,
                 incorrect_answers: list, category: str, difficulty: str):

        if difficulty not in ["easy", "medium", "hard"]:
            raise AttributeError

        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers  # a list of strings
        self.category = category
        self.difficulty = difficulty
        self.answers = self.incorrect_answers  # list of strings

        self.answers.append(correct_answer)
        random.shuffle(self.answers)
        # makes the correct answer accessible through this attribute
        self.answer_id = self.answers.index(correct_answer)

    def __str__(self):
        """Returns question, answer and indices"""
        answers_str = '\n'.join(
            f'{i + 1} {answer}' for i, answer in enumerate(self.answers))
        return f'{self.question}\n{answers_str}'
