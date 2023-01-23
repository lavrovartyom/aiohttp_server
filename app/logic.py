from passlib.hash import pbkdf2_sha256

# result1 = pbkdf2_sha256.verify('lavr432d2', hash_1)


def hash_password(password: str):
	""" Функция для хэширования пароля """
	result = pbkdf2_sha256.hash(password)
	return result


def verifying_password(password: str):
	""" Функция для проверки пароля """
	result = pbkdf2_sha256.verify(password)
	return result
