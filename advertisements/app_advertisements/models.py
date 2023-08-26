from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2) #IntegerField - целые числа .. DecimalField - плавающиеся
    auction = models.BooleanField("Торг", help_text="Уместен или нет")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    image = models.ImageField("Изображения", upload_to="advertisements/")
    
    class Meta:
        db_table = 'advertisements'

    # def __str__(self):
    #     return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weght: bold:">Сегодня в {}</span>', created_time)
        
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Дата изменения")
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weght: bold:">Сегодня в {}</span>', updated_time) #если нужен другой цвет надо поменять green на другой
        
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

  