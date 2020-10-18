    from django.db import models
    from django.contrib.auth.models import User



    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        image = models.ImageField(default='defualt.jpg', upload_to='profile_pic')
        product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True)
        sender = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="sender")
        receiver = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="receiver")
        text = models.TextField(max_length=350)
        message_creatoion_time = models.DateTimeField(auto_now=True) 
        is_readed = models.BooleanField(default=Flase)

        def __str__(self):
            return f'{self.user.username} Profile'

