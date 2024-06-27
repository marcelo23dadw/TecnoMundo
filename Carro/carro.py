class Carro:
    def __init__(self, request=None):
        if request:
            self.request = request
            self.session = request.session
            carro = self.session.get("carro")
            if not carro:
                self.carro = self.session["carro"] = {}
            else:
                self.carro = carro
        else:
            self.carro = {}

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro.keys():
            self.carro[producto_id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            self.carro[producto_id]["cantidad"] += 1
            self.carro[producto_id]["precio"] = float(self.carro[producto_id]["precio"]) + producto.precio

        self.guardar_carro()

    def restar_producto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            self.carro[producto_id]["cantidad"] -= 1
            self.carro[producto_id]["precio"] = float(self.carro[producto_id]["precio"]) - producto.precio
            if self.carro[producto_id]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar_carro()

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
