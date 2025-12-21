// Pruebas Jasmine con generación automática basada en tipos
// Verificación de tipos con typeof y Array.isArray()

const { ServicioCalculadora } = require("../src/js/servicios/servicioCalculadora");

describe('ServicioCalculadora - Pruebas basadas en tipos', function() {
  let servicio;

  beforeEach(function() {
    servicio = new ServicioCalculadora();
  });

  // ============================================
  // PRUEBAS PARA FUNCIONES NUMÉRICAS
  // ============================================

  describe('sumar', function() {
    it('debe sumar enteros positivos correctamente', function() {
      const resultado = servicio.sumar(5, 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(8);
    });

    it('debe sumar enteros negativos correctamente', function() {
      const resultado = servicio.sumar(-5, -3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(-8);
    });

    it('debe sumar números mixtos (positivo y negativo)', function() {
      const resultado = servicio.sumar(10, -3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(7);
    });

    it('debe sumar decimales correctamente', function() {
      const resultado = servicio.sumar(2.5, 3.7);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBeCloseTo(6.2);
    });

    it('debe sumar con cero correctamente', function() {
      const resultado = servicio.sumar(5, 0);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(5);
    });

    it('debe manejar strings inválidos (concatenación de strings)', function() {
      const resultado = servicio.sumar('5', 3);
      // Con el operador +, JavaScript concatena strings en lugar de sumar
      expect(typeof resultado).toBe('string');
      expect(resultado).toBe('53'); // '5' + 3 = '53' (concatenación)
    });

    it('debe manejar null como parámetro (null se convierte a 0)', function() {
      const resultado = servicio.sumar(null, 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(3); // null se convierte a 0
    });

    it('debe manejar undefined como parámetro (devuelve NaN)', function() {
      const resultado = servicio.sumar(undefined, 3);
      expect(typeof resultado).toBe('number');
      expect(Number.isNaN(resultado)).toBe(true);
    });
  });

  describe('restar', function() {
    it('debe restar enteros positivos correctamente', function() {
      const resultado = servicio.restar(10, 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(7);
    });

    it('debe restar enteros negativos correctamente', function() {
      const resultado = servicio.restar(-5, -3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(-2);
    });

    it('debe restar números mixtos (positivo y negativo)', function() {
      const resultado = servicio.restar(5, -3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(8);
    });

    it('debe restar decimales correctamente', function() {
      const resultado = servicio.restar(5.5, 2.3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBeCloseTo(3.2);
    });

    it('debe restar con cero correctamente', function() {
      const resultado = servicio.restar(5, 0);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(5);
    });

    it('debe manejar strings inválidos (conversión implícita)', function() {
      const resultado = servicio.restar('10', 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(7); // '10' se convierte a 10
    });

    it('debe manejar null como parámetro (null se convierte a 0)', function() {
      const resultado = servicio.restar(null, 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(-3); // null se convierte a 0
    });

    it('debe manejar undefined como parámetro (devuelve NaN)', function() {
      const resultado = servicio.restar(undefined, 3);
      expect(typeof resultado).toBe('number');
      expect(Number.isNaN(resultado)).toBe(true);
    });
  });

  describe('multiplicar', function() {
    it('debe multiplicar enteros positivos correctamente', function() {
      const resultado = servicio.multiplicar(4, 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(12);
    });

    it('debe multiplicar enteros negativos correctamente', function() {
      const resultado = servicio.multiplicar(-4, -3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(12);
    });

    it('debe multiplicar números mixtos (positivo y negativo)', function() {
      const resultado = servicio.multiplicar(4, -3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(-12);
    });

    it('debe multiplicar decimales correctamente', function() {
      const resultado = servicio.multiplicar(2.5, 4);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(10);
    });

    it('debe multiplicar con cero correctamente', function() {
      const resultado = servicio.multiplicar(5, 0);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(0);
    });

    it('debe manejar strings inválidos (conversión implícita)', function() {
      const resultado = servicio.multiplicar('4', 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(12); // '4' se convierte a 4
    });

    it('debe manejar null como parámetro (null se convierte a 0)', function() {
      const resultado = servicio.multiplicar(null, 3);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(0); // null se convierte a 0
    });

    it('debe manejar undefined como parámetro (devuelve NaN)', function() {
      const resultado = servicio.multiplicar(undefined, 3);
      expect(typeof resultado).toBe('number');
      expect(Number.isNaN(resultado)).toBe(true);
    });
  });

  describe('dividir', function() {
    it('debe dividir enteros positivos correctamente', function() {
      const resultado = servicio.dividir(10, 2);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(5);
    });

    it('debe dividir enteros negativos correctamente', function() {
      const resultado = servicio.dividir(-10, -2);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(5);
    });

    it('debe dividir números mixtos (positivo y negativo)', function() {
      const resultado = servicio.dividir(10, -2);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(-5);
    });

    it('debe dividir decimales correctamente', function() {
      const resultado = servicio.dividir(7.5, 2.5);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(3);
    });

    it('debe dividir con cero como dividendo', function() {
      const resultado = servicio.dividir(0, 5);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(0);
    });

    it('debe lanzar error cuando b es cero', function() {
      expect(function() {
        servicio.dividir(10, 0);
      }).toThrow(new Error('No se permite dividir entre cero'));
    });

    it('debe manejar strings inválidos (conversión implícita)', function() {
      const resultado = servicio.dividir('10', 2);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(5); // '10' se convierte a 10
    });

    it('debe manejar null como parámetro (null se convierte a 0)', function() {
      const resultado = servicio.dividir(null, 2);
      expect(typeof resultado).toBe('number');
      expect(resultado).toBe(0); // null se convierte a 0
    });

    it('debe manejar undefined como parámetro (devuelve NaN)', function() {
      const resultado = servicio.dividir(undefined, 2);
      expect(typeof resultado).toBe('number');
      expect(Number.isNaN(resultado)).toBe(true);
    });
  });

  // ============================================
  // PRUEBAS PARA FUNCIÓN ASYNC calcularConImpuestos
  // ============================================

  describe('calcularConImpuestos', function() {
    let mockCliente;
    let crearClienteImpuestosSpy;

    beforeEach(function() {
      mockCliente = {
        getTaxRate: jasmine.createSpy('getTaxRate').and.returnValue(Promise.resolve(0.21))
      };

      crearClienteImpuestosSpy = jasmine.createSpy('crearClienteImpuestos')
        .and.returnValue(mockCliente);

      servicio = new ServicioCalculadora({
        crearClienteImpuestos: crearClienteImpuestosSpy
      });
    });

    it('debe calcular con impuestos usando mock correctamente', async function() {
      const resultado = await servicio.calcularConImpuestos(100, 'IVA');
      
      expect(typeof resultado).toBe('number');
      expect(resultado).toBeCloseTo(121);
      expect(crearClienteImpuestosSpy).toHaveBeenCalled();
      expect(mockCliente.getTaxRate).toHaveBeenCalledWith('IVA');
    });

    it('debe manejar diferentes tipos de impuesto', async function() {
      mockCliente.getTaxRate.and.returnValue(Promise.resolve(0.16));
      
      const resultado = await servicio.calcularConImpuestos(200, 'REDUCIDO');
      
      expect(typeof resultado).toBe('number');
      expect(resultado).toBeCloseTo(232);
      expect(mockCliente.getTaxRate).toHaveBeenCalledWith('REDUCIDO');
    });

    it('debe agregar la operación al historial', async function() {
      await servicio.calcularConImpuestos(100, 'IVA');
      const historial = servicio.obtenerHistorial();
      
      expect(Array.isArray(historial)).toBe(true);
      expect(historial.length).toBe(1);
      expect(historial[0].operacion).toBe('multiplicar');
    });
  });

  // ============================================
  // PRUEBAS PARA FUNCIONES DE HISTORIAL
  // ============================================

  describe('agregarAlHistorial', function() {
    it('debe agregar una operación al historial', function() {
      servicio.agregarAlHistorial('sumar', 5, 3, 8);
      const historial = servicio.obtenerHistorial();
      
      expect(Array.isArray(historial)).toBe(true);
      expect(historial.length).toBe(1);
      expect(typeof historial[0]).toBe('object');
      expect(historial[0].operacion).toBe('sumar');
      expect(Array.isArray(historial[0].operandos)).toBe(true);
      expect(historial[0].operandos).toEqual([5, 3]);
      expect(typeof historial[0].resultado).toBe('number');
      expect(historial[0].resultado).toBe(8);
      expect(historial[0].timestamp instanceof Date).toBe(true);
    });

    it('debe agregar múltiples operaciones al historial', function() {
      servicio.agregarAlHistorial('sumar', 1, 2, 3);
      servicio.agregarAlHistorial('restar', 5, 2, 3);
      servicio.agregarAlHistorial('multiplicar', 2, 3, 6);
      
      const historial = servicio.obtenerHistorial();
      expect(Array.isArray(historial)).toBe(true);
      expect(historial.length).toBe(3);
    });
  });

  describe('obtenerHistorial', function() {
    it('debe retornar un array vacío cuando no hay historial', function() {
      const historial = servicio.obtenerHistorial();
      
      expect(Array.isArray(historial)).toBe(true);
      expect(historial.length).toBe(0);
    });

    it('debe retornar un array con las operaciones realizadas', function() {
      servicio.sumar(1, 2);
      servicio.restar(5, 2);
      
      const historial = servicio.obtenerHistorial();
      
      expect(Array.isArray(historial)).toBe(true);
      expect(historial.length).toBe(2);
      expect(typeof historial[0]).toBe('object');
      expect(typeof historial[1]).toBe('object');
    });

    it('debe retornar una copia del historial, no la referencia', function() {
      servicio.sumar(1, 2);
      const historial1 = servicio.obtenerHistorial();
      const historial2 = servicio.obtenerHistorial();
      
      expect(Array.isArray(historial1)).toBe(true);
      expect(Array.isArray(historial2)).toBe(true);
      expect(historial1).not.toBe(historial2); // Diferentes referencias
      expect(historial1).toEqual(historial2); // Mismo contenido
    });
  });

  describe('limpiarHistorial', function() {
    it('debe limpiar el historial correctamente', function() {
      servicio.sumar(1, 2);
      servicio.restar(5, 2);
      
      expect(Array.isArray(servicio.obtenerHistorial())).toBe(true);
      expect(servicio.obtenerHistorial().length).toBe(2);
      
      servicio.limpiarHistorial();
      
      const historial = servicio.obtenerHistorial();
      expect(Array.isArray(historial)).toBe(true);
      expect(historial.length).toBe(0);
    });

    it('debe limpiar el historial sin afectar nuevas operaciones', function() {
      servicio.sumar(1, 2);
      servicio.limpiarHistorial();
      servicio.restar(5, 2);
      
      const historial = servicio.obtenerHistorial();
      expect(Array.isArray(historial)).toBe(true);
      expect(historial.length).toBe(1);
      expect(historial[0].operacion).toBe('restar');
    });
  });

  // ============================================
  // PRUEBAS PARA validarNumeros
  // ============================================

  describe('validarNumeros', function() {
    it('debe retornar boolean true para números válidos', function() {
      const resultado = servicio.validarNumeros(1, 2, 3);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(true);
    });

    it('debe retornar boolean true para números negativos', function() {
      const resultado = servicio.validarNumeros(-1, -2, -3);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(true);
    });

    it('debe retornar boolean true para decimales', function() {
      const resultado = servicio.validarNumeros(1.5, 2.7, 3.9);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(true);
    });

    it('debe retornar boolean true para cero', function() {
      const resultado = servicio.validarNumeros(0, 0, 0);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(true);
    });

    it('debe retornar boolean false para strings', function() {
      const resultado = servicio.validarNumeros('1', '2', '3');
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(false);
    });

    it('debe retornar boolean false para null', function() {
      const resultado = servicio.validarNumeros(null, 2, 3);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(false);
    });

    it('debe retornar boolean false para undefined', function() {
      const resultado = servicio.validarNumeros(undefined, 2, 3);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(false);
    });

    it('debe retornar boolean false para NaN', function() {
      const resultado = servicio.validarNumeros(NaN, 2, 3);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(false);
    });

    it('debe retornar boolean false cuando hay mezcla de válidos e inválidos', function() {
      const resultado = servicio.validarNumeros(1, '2', 3);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(false);
    });

    it('debe retornar boolean true para un solo número válido', function() {
      const resultado = servicio.validarNumeros(5);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(true);
    });

    it('debe retornar boolean true para múltiples números válidos', function() {
      const resultado = servicio.validarNumeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
      expect(typeof resultado).toBe('boolean');
      expect(resultado).toBe(true);
    });
  });
});
