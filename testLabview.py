import fastapi

def uvi():
    u = fastapi.__version__
    print(u)

uvi()