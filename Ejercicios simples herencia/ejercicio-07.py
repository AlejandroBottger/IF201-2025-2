class Comprobante:
    def __init__(self, importe: str):
        self.importe = importe
    def calcular_pago(self):
        return self.importe
    
class Boleta(Comprobante):
    def __init__(self, importe:float, DNI: int):
        super().__init__(importe)
        self.DNI = DNI
    
class Factura(Comprobante):
    def __init__(self, importe, ruc: int):
        super().__init__(importe)
        self.ruc = ruc
        
    def calcular_igv(self, importe = None):
        if importe is None:
            self.importe = importe
        return importe * 0.18
    
    def calcular_pago(self, descuento = None):
        if descuento is None:
            return super().calcular_pago()
        else:
            importe_con_descuento = self.importe * (1 - descuento)
            return importe_con_descuento + self.calcular_igv(importe_con_descuento)

if __name__ == "__main__":
    b = Boleta(100, "12345678")
    print(f"Boleta- DNI: ", b.DNI, "| Pago:", b.calcular_pago())
    
    f1 = Factura(200, "20123456789")
    print("Factura sin descuento - RUC:", f1.ruc, "| Pago:", f1.calcular_pago())

    f2 = Factura(200, "20123456789")
    print("Factura con 10% descuento - RUC:", f2.ruc, "| Pago:", f2.calcular_pago(0.10))