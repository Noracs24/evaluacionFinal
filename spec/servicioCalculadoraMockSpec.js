// Jasmine Spies 
// funciones especiales de Jasmine que "espían" el comportamiento
// Permiten rastrear cuántas veces se llamó una función
// Permiten verificar con qué argumentos fue llamada
// Permiten simular valores de retorno sin ejecutar la función real

const { ServicioCalculadora } = require("../src/js/servicios/servicioCalculadora");

describe(' Mocking Avanzado ', function() {
  let servicio;
  let clienteImpuestosFake;
  let crearClienteImpuestosSpy;

  beforeEach(function() {
    // Crear objeto espía para el cliente externo
    clienteImpuestosFake = {
      getTaxRate: jasmine.createSpy('getTaxRate')
                        .and.returnValue(Promise.resolve(0.21))
    };

    // Crear espía-fábrica
    crearClienteImpuestosSpy = jasmine.createSpy('crearClienteImpuestos')
                                     .and.returnValue(clienteImpuestosFake);

    // Inyectar dependencias
    servicio = new ServicioCalculadora({
      crearClienteImpuestos: crearClienteImpuestosSpy
    });
  });

  it('debe calcular con impuestos usando espías personalizados', async function() {
    // Ejecutar el método
    const resultado = await servicio.calcularConImpuestos(100, 'IVA');

    // Verificaciones
    expect(crearClienteImpuestosSpy).toHaveBeenCalled();
    expect(clienteImpuestosFake.getTaxRate).toHaveBeenCalledWith('IVA');
    expect(resultado).toBeCloseTo(121); 

    // Verificar historial
    const historial = servicio.obtenerHistorial();
    expect(historial.length).toBe(1);
    expect(historial[0].operacion).toBe('multiplicar');
    expect(historial[0].operandos).toEqual([100, 1.21]);
    expect(historial[0].resultado).toBeCloseTo(121); 
  });

  it('debe manejar diferentes tipos de impuesto', async function() {
    // Configurar diferente tasa para este test
    clienteImpuestosFake.getTaxRate.and.returnValue(Promise.resolve(0.16));

    const resultado = await servicio.calcularConImpuestos(200, 'REDUCIDO');
    
    expect(resultado).toBeCloseTo(232); 
    expect(clienteImpuestosFake.getTaxRate).toHaveBeenCalledWith('REDUCIDO');
  });
});