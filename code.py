import file_operations
from faker import Faker
import random
import os

letter_mapping = {
    'а': 'а͠',
    'б': 'б̋', 
    'в': 'в͒͠',
    'г': 'г͒͠', 
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}


fake = Faker("ru_RU")

skills = [
  "Стремительный прыжок",
  "Электрический выстрел", 
  "Ледяной удар", 
  "Стремительный удар", 
  "Кислотный взгляд",
  "Тайный побег", 
  "Ледяной выстрел",
  "Огненный заряд"
]

for i in range(1,11):
  context = {
    "first_name": fake.first_name_male(),
    "last_name": fake.last_name_male(),
    "town": fake.city(),
    "job": fake.job(),
    "strength": random.randint(3,18),
    "agility": random.randint(3,18),
    "endurance": random.randint(3,18),
    "intelligence": random.randint(3,18),
    "luck": random.randint(3,18)
  }

  
  unique_skills = random.sample(skills, 3)
  modified_skills = []

  
  for skill in unique_skills:
    modified_skills = [  
      ''.join(letter_mapping.get(char, char) for char in skill) for skill in unique_skills
    ]
  
  context["skill_1"] = modified_skills[0]
  context["skill_2"] = modified_skills[1]
  context["skill_3"] = modified_skills[2]

  os.makedirs('cards', exist_ok=True)
  files_name = f"cards/charsheet-{i}.svg"
  file_operations.render_template("charsheet.svg", files_name, context)
