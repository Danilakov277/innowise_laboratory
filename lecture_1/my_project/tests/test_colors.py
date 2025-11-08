import pytest
from colorama import Fore, Back, Style
from main import get_colored_text, print_colored_text
from io import StringIO
import sys

class TestColoramaOutput:
    """Тесты для цветного вывода с colorama"""
    
    def test_get_colored_text_returns_list(self):
        """Тест, что функция возвращает список строк"""
        result = get_colored_text()
        assert isinstance(result, list)
        assert len(result) == 4
    
    def test_colored_text_contains_hello_world(self):
        """Тест, что каждая строка содержит 'Hello World'"""
        result = get_colored_text()
        for text in result:
            assert "Hello World" in text
    
    def test_colored_text_contains_color_codes(self):
        """Тест, что текст содержит коды цветов"""
        result = get_colored_text()
        
        # Проверяем наличие цветовых кодов
        assert any(Fore.RED in text for text in result)
        assert any(Fore.GREEN in text for text in result)
        assert any(Fore.BLUE in text for text in result)
        assert any(Fore.MAGENTA in text for text in result)
        assert any(Back.YELLOW in text for text in result)
        assert any(Back.CYAN in text for text in result)
        assert any(Style.BRIGHT in text for text in result)
    
    def test_specific_color_combinations(self):
        """Тест конкретных комбинаций цветов"""
        result = get_colored_text()
        
        # Красный текст на желтом фоне
        assert Fore.RED in result[0] and Back.YELLOW in result[0]
        
        # Зеленый текст
        assert Fore.GREEN in result[1]
        
        # Яркий синий текст
        assert Fore.BLUE in result[2] and Style.BRIGHT in result[2]
        
        # Пурпурный текст на голубом фоне
        assert Fore.MAGENTA in result[3] and Back.CYAN in result[3]

    def test_print_colored_text_output(self, capsys):
        """Тест функции печати с использованием capsys"""
        print_colored_text()
        captured = capsys.readouterr()
        
        # Проверяем, что вывод содержит ожидаемый текст
        assert "Hello World" in captured.out
        assert captured.out.count("Hello World") == 4

    def test_colorama_initialization(self):
        """Тест инициализации colorama"""
        from colorama import init
        # Просто проверяем, что функция существует и может быть вызвана
        assert callable(init)


class TestColoramaConstants:
    """Тесты констант colorama"""
    
    def test_fore_colors_exist(self):
        """Тест существования цветов переднего плана"""
        assert hasattr(Fore, 'RED')
        assert hasattr(Fore, 'GREEN')
        assert hasattr(Fore, 'BLUE')
        assert hasattr(Fore, 'MAGENTA')
        assert hasattr(Fore, 'YELLOW')
        assert hasattr(Fore, 'CYAN')
        assert hasattr(Fore, 'WHITE')
        assert hasattr(Fore, 'BLACK')
    
    def test_back_colors_exist(self):
        """Тест существования цветов фона"""
        assert hasattr(Back, 'YELLOW')
        assert hasattr(Back, 'CYAN')
        assert hasattr(Back, 'RED')
        assert hasattr(Back, 'GREEN')
        assert hasattr(Back, 'BLUE')
        assert hasattr(Back, 'MAGENTA')
    
    def test_styles_exist(self):
        """Тест существования стилей"""
        assert hasattr(Style, 'BRIGHT')
        assert hasattr(Style, 'DIM')
        assert hasattr(Style, 'NORMAL')
        assert hasattr(Style, 'RESET_ALL')