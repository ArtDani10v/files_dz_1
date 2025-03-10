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




filename = "recipes.txt"  # Имя файла относительно текущей директории
cook_book = read_recipes(filename)
print(cook_book)
