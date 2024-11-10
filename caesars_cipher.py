import string


class CaesarsCipher:
    """
    Класс для шифрования и дешифрования сообщений с использованием шифра
    Цезаря.
    """
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + " !?."
        self.alphabet_len = len(self.alphabet)

    def encrypt(self, message: str, key: int) -> str:
        """
        Шифрует сообщение с заданным ключом.

        :param message: Исходное сообщение для шифрования.
        :param key: Ключ для шифрования.
        :return: Зашифрованное сообщение.
        """
        return ''.join(self._shift_char(char, key) for char in message)

    def decrypt(self, message: str, key: int) -> str:
        """
        Дешифрует сообщение с заданным ключом.

        :param message: Зашифрованное сообщение для дешифровки.
        :param key: Ключ для дешифровки.
        :return: Дешифрованное сообщение.
        """
        return ''.join(self._shift_char(char, -key) for char in message)

    def _shift_char(self, char: str, key: int) -> str:
        """
        Смещает символ на заданное количество позиций в алфавите.

        :param char: Символ для сдвига.
        :param key: Ключ (количество позиций для сдвига).
        :return: Смещенный символ.
        """
        if char in self.alphabet:
            new_index = (self.alphabet.index(char) + key) % self.alphabet_len
            return self.alphabet[new_index]
        return char


# Получение зашифрованного сообщения от пользователя
encrypted_message = input("Введите зашифрованное сообщение: ")

# Поиск ключа и расшифровка сообщения
cipher = CaesarsCipher()
for key in range(1, cipher.alphabet_len):
    decrypted_message = cipher.decrypt(encrypted_message, key)
    print(f"{key}: {decrypted_message}")
