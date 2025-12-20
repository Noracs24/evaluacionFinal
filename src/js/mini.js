// mini framework
// Wrapper personalizado sobre Jasmine
// Reduce código repetitivo en las pruebas de integración
// Automatiza la creación y limpieza del contexto entre pruebas
// Sin este framework tendríamos que repetir beforeEach y afterEach
// en cada archivo de pruebas, lo cual es propenso a errores y tedioso

function suiteIntegracion(nombre, crearContexto, definirPruebas) {
  describe(nombre, () => {
    let contexto;

    beforeEach(() => {
      contexto = crearContexto();
    });

    afterEach(() => {
      // Limpieza opcional si el contexto expone limpiar()
      if (contexto && typeof contexto.limpiar === "function") {
        contexto.limpiar();
      }
    });

    // Pasamos un getter para evitar usar variables globales
    definirPruebas(() => contexto);
  });
}

module.exports = { suiteIntegracion };