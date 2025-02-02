from django.db import models

class User(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    exercise_name = models.CharField(max_length=255)
    repetitions_per_set = models.IntegerField()
    number_of_sets = models.IntegerField()
    exercise_description = models.TextField()

    def __str__(self):
        return self.exercise_name

class SportProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='sport_programs/', null=True, blank=True)
    exercises = models.ManyToManyField(Exercise, related_name='sport_programs')
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, help_text="Comma-separated tags")
    fit_nutrient_program = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    time = models.TimeField(help_text="Recommended time to consume")
    volume = models.CharField(max_length=100, help_text="Volume or portion size")

    def __str__(self):
        return self.name
    
class NutrientProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='nutrient_programs/', null=True, blank=True)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, help_text="Comma-separated tags")
    foods = models.ManyToManyField(Food, related_name='nutrient_programs')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProgramRequest(models.Model):
    program_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    height = models.PositiveIntegerField()  
    weight = models.PositiveIntegerField()  
    disease_status = models.CharField(max_length=10, choices=[('ندارم', 'ندارم'), ('دارم', 'دارم')], default='ندارم')
    disease_description = models.CharField(max_length=255, blank=True, null=True) 
    waist = models.PositiveIntegerField()  
    comments = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='program_requests/photos/', null=True, blank=True)
    request_time = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Request {self.program_id} - {self.first_name} {self.last_name}"
    
    

class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    staff = models.ManyToManyField(Staff)

    def __str__(self):
        return f"Membership {self.membership_id} for {self.user.name}"

class Approval(models.Model):
    approval_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    approval_date = models.DateTimeField()

    def __str__(self):
        return f"Approval {self.approval_id} for {self.user.name}"

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    publication_time = models.DateTimeField()

    def __str__(self):
        return f"Comment {self.comment_id} by {self.user.name} on {self.blog.title}"
