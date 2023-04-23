RhysConfig = {'host':"localhost", 'user':"root", 'password':"ROOT"}
SamuelConfig = {'host':"localhost", 'user':"abstract-programmer", 'password':"example-password"}
SmitaConfig = {'host':"localhost", 'user':"root", 'password':"ROOT"}
CollegeConfig = {'host':"localhost", 'user':"root", 'password':"ROOT"}


ConfigKey='Rhys'

if ConfigKey=='Rhys':
    Config=RhysConfig
if ConfigKey=='Samuel':
    Config=SamuelConfig
if ConfigKey=='Smita':
    Config=SmitaConfig
if ConfigKey=='College':
    Config=CollegeConfig
    
    
print(Config['user'])