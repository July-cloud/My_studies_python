#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = [ 'father', 'mather', 'brother']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
   ['vladimir', 185], ['natalya',170], ['vlad',165]
]

print('Рост отца', my_family_height[0], 'cm')
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
summ_my_family_height = (my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1])

print('Общиий рост моей семьи', summ_my_family_height, 'cm')