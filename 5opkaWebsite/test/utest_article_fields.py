import unittest
import sys, os
from utils.article_storage import validate_article_fields

class TestArticleValidation(unittest.TestCase):
    
    def test_valid_all_fields(self):
        errors = validate_article_fields(
            author="Иван Петров",
            title="Заголовок статьи",
            content="Текст статьи длиной более десяти символов.",
            phone="+79161234567"
        )
        self.assertEqual(errors, {})
    
    def test_author_errors(self):
        # Пустой автор
        errors = validate_article_fields("", "Title", "Content ten chars", "+79161234567")
        self.assertIn('author', errors)
        # Слишком длинный автор
        errors = validate_article_fields("A" * 60, "Title", "Content ten chars", "+79161234567")
        self.assertIn('author', errors)
        # Спецсимволы в авторе
        errors = validate_article_fields("Иван <script>", "Title", "Content ten chars", "+79161234567")
        self.assertIn('author', errors)
    
    def test_title_errors(self):
        # Пустой заголовок
        errors = validate_article_fields("Author", "", "Content ten chars", "+79161234567")
        self.assertIn('title', errors)
        # Короткий заголовок
        errors = validate_article_fields("Author", "ab", "Content ten chars", "+79161234567")
        self.assertIn('title', errors)
        # Длинный заголовок
        errors = validate_article_fields("Author", "A" * 120, "Content ten chars", "+79161234567")
        self.assertIn('title', errors)
    
    def test_content_errors(self):
        # Пустой текст
        errors = validate_article_fields("Author", "Title", "", "+79161234567")
        self.assertIn('content', errors)
        # Короткий текст (меньше 10 символов)
        errors = validate_article_fields("Author", "Title", "short", "+79161234567")
        self.assertIn('content', errors)
        # Текст из пробелов
        errors = validate_article_fields("Author", "Title", "   \n   ", "+79161234567")
        self.assertIn('content', errors)
    
    def test_phone_errors(self):
        # Пустой телефон
        errors = validate_article_fields("Author", "Title", "Content enough long", "")
        self.assertIn('phone', errors)
        # Неправильный формат (без +7 или 8)
        errors = validate_article_fields("Author", "Title", "Content enough long", "12345678901")
        self.assertIn('phone', errors)
        # Слишком короткий
        errors = validate_article_fields("Author", "Title", "Content enough long", "+7916123456")
        self.assertIn('phone', errors)
        # Слишком длинный
        errors = validate_article_fields("Author", "Title", "Content enough long", "+791612345678")
        self.assertIn('phone', errors)
        # Номер из одинаковых цифр
        errors = validate_article_fields("Author", "Title", "Content enough long", "+70000000000")
        self.assertIn('phone', errors)
        errors = validate_article_fields("Author", "Title", "Content enough long", "81111111111")
        self.assertIn('phone', errors)

if __name__ == '__main__':
    unittest.main()
