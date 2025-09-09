from flask import Flask, render_template

app = Flask(__name__)

descr_producto = "Este es un producto increible que te encantará, tiene muchas características asombrosas y está hecho con los mejores materiales."

# Lista de productos con nombres de clave en español para coincidir con la plantilla
productos =[
  {"id":1, "nombre":"Producto A", "precio": 100000,"imagen":"producto_a.jpg", "descripcion": descr_producto},
  {"id":2, "nombre":"Producto B", "precio": 150000,"imagen":"producto_b.jpg", "descripcion": descr_producto},
  {"id":3, "nombre":"Producto C", "precio": 200000,"imagen":"producto_c.jpg", "descripcion": descr_producto},
  {"id":4, "nombre":"Producto D", "precio": 250000,"imagen":"producto_c.jpg", "descripcion": descr_producto},
  {"id":5, "nombre":"Producto E", "precio": 300000,"imagen":"producto_c.jpg", "descripcion": descr_producto},
  {"id":6, "nombre":"Producto F", "precio": 350000,"imagen":"producto_c.jpg", "descripcion": descr_producto},
  {"id":7, "nombre":"Producto G", "precio": 400000,"imagen":"producto_c.jpg", "descripcion": descr_producto},
  {"id":8, "nombre":"Producto H", "precio": 450000,"imagen":"producto_c.jpg", "descripcion": descr_producto},
  {"id":9, "nombre":"Producto I", "precio": 500000,"imagen":"producto_c.jpg", "descripcion": descr_producto},
  {"id":10, "nombre":"Producto J", "precio": 550000,"imagen":"producto_c.jpg", "descripcion": descr_producto}
]


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/productos')
def ver_productos():
  return render_template('productos.html', productos=productos)

if __name__ == '__main__':
  app.run(debug=True)