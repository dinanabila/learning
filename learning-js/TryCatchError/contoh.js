// Bikin class ValidationError yang merupakan turunan dari class Error
class ValidationError extends Error {
    constructor(message) {
        super(message);
        this.name = "ValidationError";
    }
}

// Bikin fungsi validateNumberInput yang memvalidasi 3 buah input (argumen)
function validateNumberInput(a, b, c){
    if(typeof(a) !== "number") {
        throw new ValidationError("Argumen pertama harus number");    
    }
    if(typeof(b) !== "number") {
        throw new ValidationError("Argumen kedua harus number");    
    }
    if(typeof(c) !== "number") {
        throw new ValidationError("Argumen ketiga harus number");    
    }
}

// - Panggil fungsi validateNumberInput di dalam fungsi detectTriangle untuk memvalidasi nilai argumen a, b, dan c.
// - pastikan Anda memanggil validateNumberInput menggunakan try .. catch.
// - bila block catch terpanggil, kembalikan fungsi detectTriangle dengan pesan error yang dibawa fungsi validateNumberInput.

const detectTriangle = (a, b, c) => {

    try {
        validateNumberInput(a, b, c);
        if (a === b && b === c) {
            return 'Segitiga sama sisi';
          }
        
          if (a === b || a === c || b === c) {
            return 'Segitiga sama kaki';
          }
        
          return 'Segitiga sembarang';
    } catch (error) {
        if (error instanceof ValidationError) {
           return error.message;
        }
    }
  };

  console.log(detectTriangle(2, 3, null));
