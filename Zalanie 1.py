user_age = int(input("Введите ваш возраст"))
           
def user_activiti(user_age):
    if  3 <= user_age <= 7:
        return print("Детсад")
    elif 7 <= user_age <= 17:
        return print("Школа")
    elif 17 <= user_age <= 24:
        return print("ВУЗ")
    elif 24 <= user_age <= 65:
        return print("Иди работай") 
    elif 65 <= user_age <= 100:
        return print("Пенсия")
    else:
        return print("Столько не живут")      

user_activiti (user_age) 