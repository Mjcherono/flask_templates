class Config:
       #General configuration parent class
   #Used in both production & development stages
    pass



class ProdConfig(Config):
    #Production  configuration child class
    # contains configurations that are used in production stages & inherits from parent
    pass


class DevConfig(Config):
   # Development  configuration child class
   # Config: The parent configuration class with General configuration settings

    DEBUG = True