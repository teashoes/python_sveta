

def get_a(question):
    answer={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    q=answer.get(question)
    print(q)

a=input()
s=get_a(a)


