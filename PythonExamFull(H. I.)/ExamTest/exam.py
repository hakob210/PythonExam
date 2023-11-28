import json

class Exam:

    def __init__(self):
        self.student = self.name_surname()
        with open("student.json", "r") as file:
            self.exam = json.load(file)
        self.answers = {}

    def name_surname(self):
        name = input("Write your name: ")
        surname = input("Write your surname: ")
        return {"student_name": name, "student_surname": surname}

    def question(self, number, data):
        print(f"\nQuestion {number}: {data['question']}")
        options = {"a": data["a"], "b": data["b"], "c": data["c"], "d": data["d"]}
        while True:
            for key, value in options.items():
                print(f"{key}. {value}")
            answer = input("\nAnswer: ").lower()
            if answer in options:
                return answer
            else:
                print("\nInvalid answer. Please enter one of these: A, B, C, D")

    def test(self):
        for number, data in self.exam["exam_content"].items():
            self.answers[number] = self.question(number, data)

    def display(self):
        print("\nCheck your answers for one last time before submitting:")
        print(f"\nName: {self.student['student_name']} {self.student['student_surname']}")
        print("\nAnswers:")
        for number, answer in self.answers.items():
            print(f"Question {number}: {answer}")

    def submit(self):
        confirmation = input("\nAre you sure you want to submit your answers? (y/n): ").lower()
        if confirmation == "y":
            file = f"{self.student['student_name']}_{self.student['student_surname']}_exam_answers.json"
            with open(file, "w") as final_answers:
                json.dump(self.answers, final_answers)
            print("Answers submitted!")
        else:
            print("Answers not submitted.")


def main():
    exam_submission = Exam()
    exam_submission.test()
    exam_submission.display()
    exam_submission.submit()


if __name__ == "__main__":
    main()
