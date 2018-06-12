from django.db import models

class Type(models.Model): # 18种属性模型
	name = models.CharField(max_length=10)
	color = models.CharField(max_length=20)
	pgl_typeid = models.IntegerField(blank=True) # 对应pgl 的typeid
	def __str__(self):
		return self.name

class Ability(models.Model):
	name = models.CharField(max_length=50)
	detail = models.TextField()
	def __str__(self):
		return self.name

class Cate(models.Model):
	name = models.CharField(max_length=10)
	color = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class MoveRange(models.Model):
	name = models.CharField(max_length=30)
	d1 = models.CharField(max_length=10, default='#f4481d')
	d2 = models.CharField(max_length=10, default='#f4481d')
	d3 = models.CharField(max_length=10, default='#f4481d')
	z = models.CharField(max_length=10, default='#f4481d')
	t1 = models.CharField(max_length=10, default='#f4481d')
	t2 = models.CharField(max_length=10, default='#769ad0')
	def __str__(self):
		return self.name

class Item(models.Model):
	itemid = models.IntegerField()
	name = models.CharField(max_length=20)
	name_en = models.CharField(max_length=20)
	detail = models.TextField()
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=10)
	class Meta:
		ordering = ['id']
	def __str__(self):
		return self.name



class Pokemon(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=10)
    name1 = models.CharField(max_length=20, blank=True)
    name_en = models.CharField(max_length=30, blank=True)
    hp = models.PositiveSmallIntegerField()
    atk = models.PositiveSmallIntegerField()
    defen = models.PositiveSmallIntegerField()
    satk = models.PositiveSmallIntegerField()
    sdef = models.PositiveSmallIntegerField()
    sp = models.PositiveSmallIntegerField()
    type1 = models.ForeignKey(Type, blank=True, related_name='type1', on_delete=models.CASCADE)
    type2 = models.ForeignKey(Type, blank=True, related_name='type2', on_delete=models.CASCADE)
    ability1 = models.ForeignKey(Ability, blank=True, related_name='ability1', on_delete=models.CASCADE)
    ability2 = models.ForeignKey(Ability, blank=True, related_name='ability2', on_delete=models.CASCADE)
    ability3 = models.ForeignKey(Ability, blank=True, related_name='ability3', on_delete=models.CASCADE)
    pic = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(Category, blank=True, related_name='cate_poke', on_delete=models.CASCADE)
    # icon = models.ImageField(upload_to='icon', blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']


	# def get_absolute_url(self):
	# 	return reverse('poke:index', kwargs={'pk':self.pk})
class Move(models.Model):
	name = models.CharField(max_length=20)
	power = models.CharField(max_length=10)
	z_power = models.CharField(max_length=10, blank=True)
	accuracy = models.CharField(max_length=10)
	pp = models.CharField(max_length=10)
	priority = models.CharField(max_length=10)
	detail = models.TextField()
	types = models.ForeignKey(Type, blank=True, on_delete=models.CASCADE)
	cate = models.ForeignKey(Cate, blank=True, on_delete=models.CASCADE)
	move_range = models.ForeignKey(MoveRange, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['id']
    
