from orm import Model, IntegerField, StringField
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='text@orm.org', password='mydds')
u.save()