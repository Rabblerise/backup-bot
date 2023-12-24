# Импортируем модуль исполнителя из модуля айограммы
from actions.messages import startBot # импорт диспетчера бота
import asyncio

# Запуск бота
if __name__ == "__main__":
    asyncio.run(startBot())