class LinkShortener:
    def __init__(self):
        self.links = {}
        self.clicks = {}
    
    def add(self, url, code=None):
        for k, v in self.links.items():
            if v == url:
                return k
        
        if not code:
            code = f"a{len(self.links) + 1}"
        
        if code in self.links:
            return None
        
        self.links[code] = url
        self.clicks[code] = 0
        return code
    
    def get(self, code):
        if code in self.links:
            self.clicks[code] += 1
            return self.links[code]
        return None
    
    def exists(self, code):
        return code in self.links
    
    def show_all(self):
        if not self.links:
            print("Пусто!")
            return
        for code, url in self.links.items():
            print(f"{code} -> {url} ({self.clicks[code]})")
    
    def popular(self):
        if not self.links:
            return None
        best = max(map(lambda c: (self.clicks[c], c), self.links.keys()))
        return best[1] if best[0] > 0 else None


def main():
    s = LinkShortener()
    
    while True:
        print("\n1.Добавить 2.Найти 3.Проверить 4.Все 5.Популярная 6.Выход")
        choice = input("> ").strip()
        
        if choice == "1":
            url = input("Ссылка: ").strip()
            if not url:
                print("Ошибка!")
                continue
            
            ans = input("Свой код? (да/нет): ").strip().lower()
            if ans == "да":
                code = input("Код: ").strip()
                result = s.add(url, code)
                if not result:
                    print("Код занят!")
                    continue
            else:
                result = s.add(url)
            
            print(f"Готово! Код: {result}")
        
        elif choice == "2":
            code = input("Код: ").strip()
            url = s.get(code)
            print(f"{code} -> {url}" if url else "Не найдено!")
        
        elif choice == "3":
            code = input("Код: ").strip()
            print("Да!" if s.exists(code) else "Нет!")
        
        elif choice == "4":
            s.show_all()
        
        elif choice == "5":
            pop = s.popular()
            if pop:
                print(f"Популярная: {pop} -> {s.links[pop]} ({s.clicks[pop]})")
            else:
                print("Нет переходов!")
        
        elif choice == "6":
            print("Пока!")
            break

if __name__ == "__main__":
    main()
