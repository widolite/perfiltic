# Inputs:
# 1. Cama de Perro,001,100.00,2.00
# 2. Juguete de Gato,001,300.00,8.00
# 3. Piano,003,100.00,2.00
# 4. Guitarra,003,300.00,8.00
# 5. Anillo,000,100.00,2.00
# 6. Otro,000,300.00,8.00

#Outputs:
# 1. Cama de Perro,146.67
# 2. Juguete de Gato,506.15
# 3. Piano,155.29
# 4. Guitarra,535.92
# 5. Anillo,132.00
# 6. Otro,455.53

from sys import stdin


def process_input(input):
    params = input.split(",")
    return calculate_price(params[0], params[1], params[2], params[3])


def cal_costo_envio(peso=0):
    cost = 10.00
    if peso > 4:
        for peso in range(4, peso):
            cost += 2.00
    return cost


def cal_prod_iva(cost=0.00, cost_envio=0.00, cost_arancel=0.00):
    cost_iva = 0.00
    if cost > 200.00:
        cost_iva = ((cost + cost_envio + cost_arancel) * 19) / 100
        return cost_iva
    else:
        return 0.00


def cal_prod_com(parcial_price=0.00, category="000"):
    categories = {"000": 0, "001": 10, "002": 5, "003": 15}
    percent = categories[category] / 100
    comision_prod = parcial_price * (percent / (1 - percent))
    return comision_prod


def cal_prod_ten_percent(partial_cost=0.00):
    return partial_cost * 0.10


def cal_prod_arancel(cost=0.00):
    return (cost * 10) / 100


def calculate_price(product_name, category, cost, weight):
    # su código va acá
    cost = float(cost)
    weight = int(float(weight))
    cost_envio = cal_costo_envio(weight)
    print("Costo Envio: {}".format(cost_envio))
    cost_arancel = cal_prod_arancel(cost)
    print("Costo Arancel {}".format(cost_arancel))
    cost_iva = cal_prod_iva(cost, cost_envio, cost_arancel)
    print("Costo IVA {}".format(cost_iva))
    parcial_cost = cost + cost_envio + cost_arancel + cost_iva
    print("Costo Parcial {}".format(parcial_cost))
    parcial_price = parcial_cost + cal_prod_ten_percent(parcial_cost)
    cost_comision = cal_prod_com(parcial_price, category)
    total_price = parcial_price + cost_comision
    print("{:.2f}".format(total_price))
    return product_name


if __name__ == '__main__':
    # tener cuidado en python con los newlines
    for lineinput in stdin:
        print(process_input(lineinput))
