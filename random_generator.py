import random
import string

def generate_password(length=6):
        char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
        random_password = ''.join(random.choice(char_pool) for _ in range(length))
        return random_password

def generate_email():
        random_digits = random.randint(111, 999)
        random_user_email = f"a.kot07{random_digits}@yandex.ru"
        return random_user_email

def generate_name():
        first_names = ["Ян", "Оля", "Святозор"]
        first_name = random.choice(first_names)
        random_user_name = f"{first_name}"
        return random_user_name

def generate_invalid_password(length = 5):
        char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
        random_incorrect_password = ''.join(random.choice(char_pool) for _ in range(length))
        return random_incorrect_password