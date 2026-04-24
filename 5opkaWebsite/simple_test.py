import unittest
from myform import is_valid_email


class TestEmailValidation(unittest.TestCase):
    def test_invalid_emails(self):
        """Тест с assertFalse для некорректных email (не менее 12 случаев)"""
        list_mail_uncor = [
            "",                             # пустая строка
            "1",                            # одно число
            "m1@",                          # нет домена
            "@mail.ru",                     # нет локальной части
            "m1@mail",                      # нет точки в домене
            "m1@.ru",                       # пустое доменное имя
            "m1@mail.c",                    # домен верхнего уровня из 1 символа
            "m1@@mail.ru",                  # две собаки
            "m 1@mail.ru",                  # пробел в локальной части
            ".m1@mail.ru",                  # точка в начале локальной части
            "m1@mail..ru",                  # две точки подряд в домене
            "m1@mail.ru.",                  # 12. точка в конце домена
            "m1@-mail.ru",                  # 13. дефис в начале домена
            "m1@mail.ru ",                  # 14. пробел в конце
            "m1@mail .ru",                  # 15. пробел в домене
            "m1..test@mail.ru",             # 16. две точки в локальной части
            "m1.@mail.ru",                  # 17. точка перед собакой
            "m1@yandex.com",                # домен не из списка
            "оченьдлиннаялокальнаячастьболеесорокасимволов1234567890@gmail.com",  # 19. > 40 символов
        ]

        for email in list_mail_uncor:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email),
                                 f"Email '{email}' должен быть невалидным")

    def test_valid_emails(self):
        """Тест с assertTrue для корректных email"""
        list_mail_cor = [
            "m.m@mail.ru",
            "m1@gmail.com",
            "user_name@yandex.ru",
            "user-name@ya.ru",
            "user123@outlook.com",
            "u@rambler.ru",
            "very.common@mail.ru",
            "disposable.style.email+symbol@gmail.com",
            "fully-qualified-domain@yandex.ru",
            "user%example@mail.ru"
        ]

        for email in list_mail_cor:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email),
                                f"Email '{email}' должен быть валидным")


if __name__ == '__main__':
    unittest.main()