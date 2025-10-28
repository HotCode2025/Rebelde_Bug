/**
 Función que valida si una contraseña cumple con los requisitos mínimos.
  Requisitos:
   Mínimo 8 caracteres.
   Al menos una letra mayúscula.
   Al menos un número.
 
 */
function validatePassword(password) {
  // Expresión regular que define las reglas de validación:
  // (?=.*[A-Z]) debe contener al menos una letra mayúscula
  // (?=.*\d)    debe contener al menos un número
  // .{8,}        debe tener mínimo 8 caracteres
  const regex = /^(?=.*[A-Z])(?=.*\d).{8,}$/;

  // El método test() verifica si la contraseña cumple con la expresión regular
  return regex.test(password);
}

// Ejemplos de uso:
console.log(validatePassword("Abc12345")); // true → cumple con todas las condiciones
console.log(validatePassword("weak")); // false → no tiene mayúscula ni número y es muy corta
