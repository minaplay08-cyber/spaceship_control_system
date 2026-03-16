from space_section import SpaceSection

class Spaceship:
    def __init__(self):
        self.sections = [
            SpaceSection("Жилой отсек", 75, 22, "1234"),
            SpaceSection("Двигательный отсек", 85, 15, "5678"),
            SpaceSection("Научный отсек", 70, 18, "9012")
        ]

    def check_all_systems(self):
        print("\n" + "="*50)
        print("ПРОВЕРКА ВСЕХ СИСТЕМ КОРАБЛЯ")
        print("="*50)
        for section in self.sections:
            print(section.get_oxygen())
            print(section.get_temperature())
            print("-" * 30)