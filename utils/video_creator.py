"""
    Short video creator
    Creates a 3-second video based on text
"""

import cv2
import numpy as np

OUTPUT_FILENAME = "my_video.mp4"


def create_running_text_video(message: str) -> dict:
    """
    :param message: Text of the ticker
    :return: Function returns nothing
    """

    # Параметры видео
    width, height = 100, 100  # Размеры кадра видео
    fps = 24  # Количество кадров в секунду
    x = width  # Начальная позиция текста по оси X
    y = height // 2  # Позиция текста по оси Y
    duration = 3  # Длительность видео в секундах

    # Параметры шрифта
    font_scale = 1  # Масштаб шрифта
    font_thickness = 1  # Толщина шрифта
    font_color = (255, 255, 255)  # Цвет шрифта (белый)
    font = cv2.FONT_HERSHEY_COMPLEX  # Шрифт

    # Создание объекта видеозаписи
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f"media/videos/{OUTPUT_FILENAME}", fourcc, fps, (width, height))

    # Создание массива для кадра
    frame = np.zeros((height, width, duration), dtype=np.uint8)

    # Проверка на то, что символов в строке не больше 100
    if len(message) > 100:
        message = message[:100]

    # Вычисление размера текста и скорости бегущей строки
    message_size = cv2.getTextSize(message, font, font_scale, font_thickness)
    running_speed = (message_size[0][0] + width) // (fps * duration)

    # Цикл для создания каждого кадра видео
    for text_position in range(fps * duration):
        frame.fill(0)
        x -= running_speed
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)

    # Закрытие объекта видеозаписи
    out.release()
    return {'title': OUTPUT_FILENAME, 'message': message, 'path': f"videos/{OUTPUT_FILENAME}"}
