from spaceship import Spaceship
from space_section import SpaceSection

def main_menu():
    spaceship = Spaceship()
    command_section = SpaceSection("Командный отсек", 80, 21, "4321")

    while True:
        print("\n" + "="*40)
        print("ГЛАВНОЕ МЕНЮ УПРАВЛЕНИЯ КОРАБЛЁМ")
        print("="*40)
        print("1. Проверить все системы")
        print("2. Изменить параметры командного отсека")
        print("3. Получить аварийный отчёт")
        print("4. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            spaceship.check_all_systems()

        elif choice == '2':
            print("\n--- ИЗМЕНЕНИЕ ПАРАМЕТРОВ КОМАНДНОГО ОТСЕКА ---")
            try:
                oxygen = int(input("Уровень кислорода (0–100): "))
                temp = int(input("Температура (-50 до +50): "))
                old_code = input("Текущий код доступа: ")
                new_code = input("Новый код доступа (4 цифры): ")

                command_section.set_oxygen(oxygen)
                command_section.set_temperature(temp)
                command_section.set_access_code(old_code, new_code)

            except ValueError:
                print("⚠ Неверный формат числа!")

        elif choice == '3':
            pwd = input("Введите пароль капитана: ")
            command_section.emergency_report(pwd)

        elif choice == '4':
            print("Выход из системы управления...")
            break

        else:
            print("⚠ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()