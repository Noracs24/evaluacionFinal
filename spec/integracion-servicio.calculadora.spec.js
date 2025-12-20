// PRUEBAS DE INTEGRACIÓN 
// Jasmine + Mini Framework personalizado
// Verificar que múltiples componentes funcionen correctamente juntos
// Se prueba el servicio completo
// Incluye interacciones con dependencias (como el cliente de impuestos)


// se importa la función suiteIntegracion desde el mini framework 
// Esta función facilita la creación de suites de pruebas con contexto compartido

const { suiteIntegracion } = require("../src/js/mini");
const { ServicioCalculadora } = require("../src/js/servicios/servicioCalculadora");

suiteIntegracion(
  "Integración",
  () => {
    // Cliente de impuestos falso
    const clienteImpuestosFalso = {
      getTaxRate: async () => 0.18,
    };

    const servicio = new ServicioCalculadora({
      crearClienteImpuestos: () => clienteImpuestosFalso,
    });

    return {
      servicio,
      limpiar: () => servicio.limpiarHistorial(),
    };
  },
  (ctx) => {
    //Comprobar que la operación de suma funciona Y que se registra
    it("sumar() guarda operación en el historial", () => {
      const { servicio } = ctx();

      const resultado = servicio.sumar(2, 3);

      expect(resultado).toBe(5);
      const historial = servicio.obtenerHistorial();
      expect(historial.length).toBe(1);
      expect(historial[0].operacion).toBe("sumar");
      expect(historial[0].resultado).toBe(5);
    });
    // Comprobar que el servicio maneja correctamente el caso de
    it("dividir() lanza error si el divisor es 0", () => {
      const { servicio } = ctx();
      expect(() => servicio.dividir(10, 0)).toThrowError("No se permite dividir entre cero");
    });
     // Comprobar integración con cliente de impuestos
    it("calcularConImpuestos() usa el cliente de impuestos", async () => {
      const { servicio } = ctx();
      const resultado = await servicio.calcularConImpuestos(100, "iva");
      expect(resultado).toBe(118); // 100 * (1 + 0.18)
    });
  }
);