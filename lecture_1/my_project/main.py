from colorama import init, Fore, Back, Style

def print_colored_text():
    """Функция для печати разноцветного текста"""
    # Initialize colorama for cross-platform colored terminal output
    init()
    
    # Print colored Hello World
    print(f"{Fore.RED}{Back.YELLOW}Hello World! {Style.RESET_ALL}")
    print(f"{Fore.GREEN}Hello World in Green! {Style.RESET_ALL}")
    print(f"{Fore.BLUE}{Style.BRIGHT}Hello World in Bright Blue! {Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{Back.CYAN}Hello World with Magenta text and Cyan background! {Style.RESET_ALL}")

def get_colored_text():
    """Функция возвращает цветной текст без печати"""
    init(autoreset=True)
    
    return [
        f"{Fore.RED}{Back.YELLOW}Hello World!",
        f"{Fore.GREEN}Hello World in Green!",
        f"{Fore.BLUE}{Style.BRIGHT}Hello World in Bright Blue!",
        f"{Fore.MAGENTA}{Back.CYAN}Hello World with Magenta text and Cyan background!"
    ]

if __name__ == "__main__":
    print_colored_text()