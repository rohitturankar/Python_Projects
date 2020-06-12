from Student import Student
from MultipleChoiceQuiz import Question
from InheritanceChef import Chef
myChef = Chef()

myChef.make_continental_specialdish()

student1 = Student("Rohit", "IECS", 1.0, False)
student2 = Student("Rajesh", "IECS", 1.2, True)

print(student1.is_honor_role())

##### Multiple choice question code
question_prompts = [
    "What color are apples?\n (a) Red/Green\n (b) Yellow\n (c) Blue\n\n",
    "What color are bananas?\n (a) Red\n (b) Yellow\n (c) Blue\n\n",
    "What color are strawberries?\n (a) Red\n (b) Yellow\n (c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer :
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)

x = 6
##3 Inheritance in Python

