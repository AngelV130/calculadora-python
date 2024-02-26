## Archivo de Arranque API

from config.Route import Router
from routes.router import setup_routes
import os
from config.Configure import Configure

carpetas = Configure(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    route = Router()
    setup_routes(route)
    route.run()
    


