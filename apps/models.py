from django.db import models

class Server(models.Model):
    server_name = models.CharField(max_length=50)
    server_purpose = models.CharField('server purpose', max_length=200)
    server_ip = models.GenericIPAddressField('ip address')
    
    added = models.DateTimeField('date added')
    
    
    PRODUCTION = 'PROD'
    STAGE = 'STAGE'
    TEST = 'TEST'
    DEVELOPMENT = 'DEV'
    SERVER_LEVEL = (
        (PRODUCTION, 'Production'),
        (STAGE, 'Staging'),
        (TEST, 'Test'),
        (DEVELOPMENT, 'Development'),
    )
    server_level= models.CharField(max_length=4,
                                      choices=SERVER_LEVEL,
                                      default=PRODUCTION)    

    def is_production(self):
        return self.server_level in (self.PRODUCTION)

    DATABASE = 'DB'
    WEB = 'WEB'
    SERVER_TYPE = (
        (DATABASE, 'Database'),
        (WEB, 'Web'),
    )
    server_type= models.CharField(max_length=3,
                                      choices=SERVER_TYPE,
                                      default=WEB)    
                                      
    WINDOWS = 'WIN'
    LINUX = 'LINUX'
    SERVER_OS = (
        (WINDOWS, 'Windows'),
        (LINUX, 'Linux'),
    )
    server_os= models.CharField(max_length=5,
                                      choices=SERVER_OS,
                                      default=WINDOWS)                                   

    def is_database(self):
        return self.server_type in (self.DATABASE)
        
    def __str__(self):  
        return self.server_name
        
class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.skill_name

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_purpose = models.CharField('server purpose', max_length=200)   
    added = models.DateTimeField('date added')
    servers = models.ManyToManyField(Server)
    skills = models.ManyToManyField(Skill)
    
    def __str__(self):  
        return self.service_name
        
class App(models.Model):
    app_name = models.CharField(max_length=50)
    services = models.ManyToManyField(Service)
    
    def __str__(self):
        return self.app_name