fieldArr = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 4, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 4, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 4, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 4, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 0, 1, 0, 0, 5, 5, 5, 4, 5, 5, 4, 5, 5, 5, 0, 0, 1, 0, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 0, 1, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 5, 0, 0, 1, 0, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 2, 2, 2, 2, 2, 2, 0, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 0, 2, 2, 2, 2, 2, 2, 0, 4, 2, 2, 4, 2, 2, 2, 2, 2, 8],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 2, 2, 2, 2, 2, 2, 0, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1, 0, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 0, 1, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 0, 0, 1, 0, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 0, 0, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 3, 1, 1, 0, 0, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 0, 0, 1, 1, 3, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 4, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 4, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
# 0 - стена
# 1 - проход
# 2 - недостижимые для пакмана места / места без зерен
# 3 - большие зерна
# 4 - точка проверки приведений
# 5 - район обитания вишенок
# 8 - правый портал того, чтобы не было ошибки в коллизии
