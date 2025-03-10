from pathlib import Path

def read_recipes(filename):
    cook_book = {}
    # Получаем путь до текущей директории, где находится скрипт
    current_dir = Path(__file__).parent
    # Формируем полный путь к файлу
    file_path = current_dir / filename
    
    # Проверка существования файла
    if not file_path.exists():
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    
    with file_path.open(encoding='utf-8') as file:
        while line := file.readline().strip():
            dish_name = line
            ingredient_count = int(file.readline().strip())
            ingredients = []
            
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            
            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку между рецептами
    
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    
    # Перебираем каждое блюдо из списка
    for dish in dishes:
        # Проверяем, есть ли такое блюдо в cook_book
        if dish in cook_book:
            # Перебираем ингредиенты блюда
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                
                # Если ингредиент уже есть в списке, суммируем количество
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' отсутствует в кулинарной книге.")
    
    return shop_list


filename = "recipes.txt"  # Имя файла относительно текущей директории
cook_book = read_recipes(filename)
print(cook_book)
input('Enter')
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(result)