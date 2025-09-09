from flask import Flask, render_template

app = Flask(__name__)


# Lista de productos con nombres de clave en español para coincidir con la plantilla
productos =[
  {"id":1, "nombre":"Producto A", "precio": 100000,"imagen":"producto_a.jpg"},
  {"id":2, "nombre":"Producto B", "precio": 150000,"imagen":"producto_b.jpg"},
  {"id":3, "nombre":"Producto C", "precio": 200000,"imagen":"producto_c.jpg"},
  {"id":4, "nombre":"Producto D", "precio": 250000,"imagen":"producto_c.jpg"}
]


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/productos')
def ver_productos():
  return render_template('productos.html', productos=productos)

if __name__ == '__main__':
  app.run(debug=True)