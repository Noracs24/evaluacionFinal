
// jasmine-spec-reporter
// Este paquete proporciona una salida más legible 
// Facilita la identificación rápida de pruebas exitosas, fallidas o pendientes

const SpecReporter = require('jasmine-spec-reporter').SpecReporter;

jasmine.getEnv().clearReporters();

jasmine.getEnv().addReporter(new SpecReporter({
  spec: {
    displayPending: true,
    displayDuration: true,
    displaySuccessful: true,
    displayFailed: true,
    displayErrorMessages: true,
    displayStacktrace: 'pretty'
  },
  summary: {
    displayDuration: true,
    displaySuccessful: true,
    displayFailed: true,
    displayPending: true,
    displayStacktrace: 'pretty'
  },
  colors: {
    enabled: true,
    successful: 'green',
    failed: 'red',
    pending: 'yellow'
  },
  prefixes: {
    successful: '[Exito] ',
    failed: '[Fallo] ',
    pending: '[Pendiente] '
  }
}));