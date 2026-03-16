class SpaceSection:
    def __init__(self, name, oxygen, temperature, access_code):
        self.name = name
        self.__oxygen_level = oxygen      # 0–100
        self.__temperature = temperature  # -50 до +50
        self.__access_code = access_code  # 4 цифры
        self.__captain_password = "admin123"  # секретный пароль

    # Геттеры
    def get_oxygen(self):
        return f"Уровень кислорода в {self.name}: {self.__oxygen_level}%"

    def get_temperature(self):
        return f"Температура в {self.name}: {self.__temperature}°C"

    def get_access_code(self, password):
        if password == self.__captain_password:
            return f"Код доступа к {self.name}: {self.__access_code}"
        else:
            return "❌ Доступ запрещён! Неверный пароль капитана!"

    # Сеттеры
    def set_oxygen(self, level):
        if 0 <= level <= 100:
            self.__oxygen_level = level
            print(f"✓ Уровень кислорода в {self.name} изменён на {level}%")
        else:
            print("⚠ Ошибка! Уровень кислорода должен быть от 0 до 100")

    def set_temperature(self, temp):
        if -50 <= temp <= 50:
            self.__temperature = temp
            print(f"✓ Температура в {self.name} изменена на {temp}°C")
        else:
            print("⚠ Ошибка! Температура должна быть от -50 до +50")

    def set_access_code(self, old_code, new_code):
        if old_code == self.__access_code:
            if len(str(new_code)) == 4 and str(new_code).isdigit():
                self.__access_code = str(new_code)
                print(f"✓ Код доступа к {self.name} успешно изменён")
            else:
                print("⚠ Новый код должен состоять из 4 цифр!")
        else:
            print("⚠ Неверный текущий код доступа!")

    # Аварийный отчёт (только при правильном пароле)
    def emergency_report(self, password):
        if password == self.__captain_password:
            print("\n" + "="*40)
            print(f"🚨 АВАРИЙНЫЙ ОТЧЁТ: {self.name}")
            print(f"Кислород: {self.__oxygen_level}%")
            print(f"Температура: {self.__temperature}°C")
            print(f"Код доступа: {self.__access_code}")
            print("="*40)
        else:
            print("❌ Доступ к аварийному отчёту запрещён!")