// calculadora con operaciones básicas 
// incluye cálculo de impuestos usando un servicio externo
// Mantiene un historial de todas las operaciones realizadas

class ServicioCalculadora {
  /**
   * @param {Object} dependencias
   * @param {Function} dependencias.crearClienteImpuestos 
   */
  constructor(dependencias = {}) {
    this.historial = [];

    // Inyección de dependencia para facilitar mocks/espías en Jasmine
    this.crearClienteImpuestos =
      dependencias.crearClienteImpuestos || (() => {
        throw new Error(
          "No se configuró crearClienteImpuestos. Inyéctalo en el constructor para usar calcularConImpuestos."
        );
      });
  }

  // Operaciones básicas
  sumar(a, b) {
    const resultado = a + b;
    this.agregarAlHistorial("sumar", a, b, resultado);
    return resultado;
  }

  restar(a, b) {
    const resultado = a - b;
    this.agregarAlHistorial("restar", a, b, resultado);
    return resultado;
  }

  multiplicar(a, b) {
    const resultado = a * b;
    this.agregarAlHistorial("multiplicar", a, b, resultado);
    return resultado;
  }

  dividir(a, b) {
    if (b === 0) {
      throw new Error("No se permite dividir entre cero");
    }
    const resultado = a / b;
    this.agregarAlHistorial("dividir", a, b, resultado);
    return resultado;
  }

  async calcularConImpuestos(montoBase, tipoImpuesto) {
    const clienteImpuestos = this.crearClienteImpuestos();
    const impuesto = await clienteImpuestos.getTaxRate(tipoImpuesto);
    return this.multiplicar(montoBase, 1 + impuesto);
  }

  // Historial de operaciones
  agregarAlHistorial(operacion, a, b, resultado) {
    this.historial.push({
      operacion,
      operandos: [a, b],
      resultado,
      timestamp: new Date(),
    });
  }

  obtenerHistorial() {
    return [...this.historial];
  }

  limpiarHistorial() {
    this.historial = [];
  }

  // Validación de entrada
  validarNumeros(...numeros) {
    return numeros.every((n) => typeof n === "number" && !Number.isNaN(n));
  }
}

module.exports = { ServicioCalculadora };