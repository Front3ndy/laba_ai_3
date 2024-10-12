import numpy

class CarProblemExpertSystem:
    def __init__(self):
        self.questions = {
            "start": {
                "question": "Автомобиль не заводится?",
                "yes": "engine_start",
                "no": "engine_noise"
            },
            "engine_start": {
                "question": "Слышите ли вы щелчок при повороте ключа?",
                "yes": "battery_problem",
                "no": "starter_issue"
            },
            "battery_problem": {
                "question": "Проверьте аккумулятор. Он старый?",
                "yes": "Проверьте аккумулятор и соединения.",
                "no": "Возможно, проблема в стартере."
            },
            "starter_issue": {
                "question": "Проблема со стартером. Вызывайте механика.",
            },
            "engine_noise": {
                "question": "Слышите ли вы странные звуки из двигателя?",
                "yes": "engine_overheat",
                "no": "Проверьте уровень масла."
            },
            "engine_overheat": {
                "question": "Двигатель перегревается?",
                "yes": "Проверьте уровень охлаждающей жидкости.",
                "no": "Проверьте другие компоненты двигателя."
            }
        }

    def ask_question(self, node):
        if isinstance(node, dict):
            print(node["question"])
            answer = input("Введите 'да' или 'нет': ").strip().lower()
            if answer == 'да':
                next_node = node.get("yes")
            else:
                next_node = node.get("no")

            if next_node:
                return self.ask_question(self.questions[next_node])
            else:
                print("Неизвестная проблема.")
        else:
            print(node)

# Пример использования
if __name__ == "__main__":
    expert_system = CarProblemExpertSystem()
    print("Добро пожаловать в экспертную систему диагностики автомобиля.")
    expert_system.ask_question(expert_system.questions["start"])
