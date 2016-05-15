import factory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user-{0}'.format(n))
    email = factory.Sequence(lambda n: 'user-{0}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')
    about_me = 'I am geek'
    # avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    my_project_experience = 'www.example.com'
    phone = '123456789'


    class Meta:
        model = 'users.User'
        django_get_or_create = ('username', )
