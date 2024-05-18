from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Video


class VideoModelTest(TestCase):
    def setUp(self):
        self.video = Video.objects.create(
            title='Test Video',
            message='This is a test message.',
            file=SimpleUploadedFile("test_video.mp4", b"file_content"),
        )

    def test_video_creation(self):
        # Проверяем, что объект был создан и сохранен в базу данных
        self.assertIsInstance(self.video, Video)
        self.assertEqual(self.video.title, 'Test Video')
        self.assertEqual(self.video.message, 'This is a test message.')
        self.assertTrue(self.video.file.name.endswith('.mp4'))
        self.assertIn('test_video', self.video.file.name)

    def test_video_str(self):
        # Проверяем, что метод __str__ возвращает правильное значение
        self.assertEqual(str(self.video), 'Test Video')

    def test_verbose_name_plural(self):
        # Проверяем verbose_name_plural
        self.assertEqual(str(Video._meta.verbose_name_plural), 'Видео')

    def test_verbose_name(self):
        # Проверяем verbose_name
        self.assertEqual(str(Video._meta.verbose_name), 'Видео')
