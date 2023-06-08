from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save


User = get_user_model()


class Post(models.Model):

    title = models.CharField(max_length=128, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Статья')
    draft = models.BooleanField(default=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


# Обработчик сигнала post_save
def post_save_dispatcher(sender, **kwargs):
    inst = kwargs['instance']  # instance, created, raw, update_fields
    if kwargs['created']:
        print(f'+++ Была создана запись {inst.title}\n+++ содержащая следующий текст: {inst.body[:40]}...')
    elif not kwargs['created']:
        print(f'+++ Запись "{inst.title}"\n+++ содержащая следующий текст: "{inst.body[:40]}", была обновлена.')


post_save.connect(post_save_dispatcher, sender=Post)
