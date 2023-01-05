from module_test import*
if __name__ == "__main__":
    with open('./answer.txt', 'r', encoding='UTF-8') as key:
        list_answer = key.readline()
    instruction = 'Чтобы ответить на вопрос, необходимо ввести номер ответа. \nУдачи\n'
    for i in instruction:
        print(i, end='')
        time.sleep(0.05)
    with open('./question.txt', 'r', encoding='UTF-8') as file:
        list_question = file.readlines()
        for index, line1 in enumerate(list_question):
            list_with_question = line1.split(':')
            question = list_with_question[0]
            var1 = list_with_question[1]
            var2 = list_with_question[2]
            var3 = list_with_question[3]
            keys = list_answer[index]
            Question(question, var1, var2, var3).print_question()
            answer = input()
            Answer(keys, answer).answer_of_test()
        result(list_answer)









