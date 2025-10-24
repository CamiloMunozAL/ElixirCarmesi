from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# Descripción base de productos Elixir Carmesí
descr_jabon = "Jabón artesanal elaborado con extracto de remolacha y aceites naturales. Proporciona hidratación profunda, limpieza suave y un aroma delicado. Ideal para todo tipo de piel."
descr_gel = "Gel corporal con extracto de remolacha que nutre y revitaliza tu piel. Fórmula natural que combina elegancia y cuidado en cada aplicación."

# Lista de productos con nombres de clave en español para coincidir con la plantilla
productos =[
  {"id":1, "nombre":"Jabón Remolacha Clásico", "precio": 15000,"imagen":"jabonRemolachaClasico.png", "descripcion": descr_jabon, "tipo": "jabón"},
  {"id":2, "nombre":"Jabón Remolacha & Lavanda", "precio": 18000,"imagen":"jabonRemolachaLavanda.png", "descripcion": "Jabón artesanal de remolacha con aceite esencial de lavanda. Calma y relaja mientras cuida tu piel con ingredientes 100% naturales.", "tipo": "jabón"},
  {"id":3, "nombre":"Gel Corporal Remolacha", "precio": 25000,"imagen":"gelCorporalRemolacha.png", "descripcion": descr_gel, "tipo": "gel"},
  {"id":4, "nombre":"Jabón Remolacha & Miel", "precio": 20000,"imagen":"jabonRemolachaMiel.png", "descripcion": "Combinación perfecta de extracto de remolacha y miel pura. Hidrata intensamente y deja tu piel suave y luminosa.", "tipo": "jabón"},
  {"id":5, "nombre":"Jabón Exfoliante Remolacha", "precio": 22000,"imagen":"jabonExfolianteRemolacha.png", "descripcion": "Jabón artesanal con extracto de remolacha y partículas exfoliantes naturales. Renueva y suaviza tu piel delicadamente.", "tipo": "jabón"},
  {"id":6, "nombre":"Gel Remolacha & Aloe Vera", "precio": 28000,"imagen":"gelRemolachaAloeVera.png", "descripcion": "Gel corporal que combina remolacha y aloe vera para una hidratación superior. Refresca y nutre tu piel naturalmente.", "tipo": "gel"}
]


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/productos')
def ver_productos():
  return render_template('productos.html', productos=productos)

@app.route('/producto/<int:id>')
def producto_detalle(id):
  producto = next((p for p in productos if p["id"] == id), None)
  if producto is None:
    return render_template('404_producto.html'), 404
  return render_template('producto_detalle.html', producto=producto)

@app.route('/planeacion')
def planeacion():
    return render_template('planeacion.html')

@app.route('/organizacion')
def organizacion():
    return render_template('organizacion.html')

@app.route('/costos')
def costos():
    return render_template('costos.html')

# Manejo del error 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
  app.run(debug=True)