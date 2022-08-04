var_1 = 100# глобальная переменная
var_2 = 10# глобальная переменная
print(var_1, var_2)

def total():
    #var_1 = 30# локальная переменная
    #var_2 = 40# локальная переменная
    result = var_1 + var_2
    print(result)

def total_sub():
    var_2 = 30# локальная переменная для функции важнее и в вычисление пойдет она
    result = var_1 - var_2
    print(result)

def total_multi():
    result = var_1 * var_2
    print("Это умножение: ", result)
total()
total_sub()
total_multi()