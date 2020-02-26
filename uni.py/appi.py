import web # pip install web.py
#https://localhost:8080/alumnos?action=getRtoken=1234

urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
