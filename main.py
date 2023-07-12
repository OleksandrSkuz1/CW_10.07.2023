import json
if __name__ == '__main__':
    # with open("data.json", "r") as file:      # зчитуємо файл json
    #     data = json.load(file)
    #     print(data['name'])



    # x = {                     # СТВОРЕННЯ СПИСКУ
    #     "name": "John",
    #     "age": 25
    # }

    # y = json.dumps(x)     # даною командою перетвор. dict в json
    # print(y)

    # with open("data.json","w") as file:       # зберігаємо в json
    #     json.dump(x, file)


        # Додаємо учня в список

    # name = input("Введіть імя учня: ")
    # age = input("ведіть вік: ")
    #
    # frame_student = {                 # frame - якщо потрібно використати шаблон словника
    #     "name": name,
    #     "age": age
    # }
    # with open("students_data.json", "r") as file:
    #     students = json.load(file)
    #     students.append(frame_student)
    #
    # with open("students_data.json", "w") as f:
    #     json.dump(students, f)

    # for product in product:

        # total_price = 0
        # for product in products:
        #     total_price += product["price"]
        #     print(round(total_price, 2))


    # знаходження найдорожчого товару
    # with open("products.json", "r") as file:
    #    products = json.load(file)
    # max_price = 0
    # for product in products:
    #     if product['price'] > max_price:
    #         max_price = product["price"]
    # print(max_price)
    #

    # знаходження найдешевшого товару

    # with open("products.json", "r") as file:
    #
    #     products = json.load(file)
    # min_price = 9999999999
    # for product in products:
    #     if product['price'] < min_price:
    #         min_price = product["price"]
    # print(min_price)






