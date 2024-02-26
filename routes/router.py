from app.Controllers.Calculate import index, documentacion, euler_mejorado, newton_raphson, runge_kutta_4th_order, view

def setup_routes(router):
    # my_controller = MyController()
    router.get('/', view, 'Pagina de inicio1')
    router.get('/api', index, 'Pagina de inicio')
    router.get('/api/documentacion', documentacion, 'Documentacion de la API')
    router.post('/api/euler-mejorado', euler_mejorado, 'Euler Mejorado')
    router.post('/api/newton-raphson', newton_raphson, 'Newton Raphson')
    router.post('/api/runge-kutta', runge_kutta_4th_order, 'Runge Kutta de Cuarto 4to Orden')