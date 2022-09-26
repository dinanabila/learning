let json = '{ "age": 20 }';
// ini harusnya let json = '{ "name": "Yoda", "age": 20 }';
// Secara sintaksis, kode di atas tidak menimbulkan eror, sehingga blok catch akan diabaikan. Namun, tidak adanya properti name pada json sebenarnya sama saja dengan eror karena akan berdampak pada jalannya program kita.
// Untuk mengatasinya, kita bisa menggunakan throw. Operator ini akan “melemparkan” eror pada program, sehingga eksekusi kode akan masuk pada blok catch. Berikut ini adalah contoh mengimplementasikan throw untuk menimbulkan eror kita sendiri 
try {
    let user = JSON.parse(json);
    //JSON.parse akan melakukan parsing atau konversi dari variabel json (string) menjadi sebuah object.
    
    //ini throw nya
    if (!user.name) {
        throw new SyntaxError("'name' is required.");
    }

    // variabel yg belum terdefinisi, biar eror ceritanya
    errorCode;

    console.log(user.name);
    console.log(user.age);
} catch (error) {
    if (error instanceof SyntaxError) {
        console.log(`JSON Error: ${error.message}`);
    } else if (error instanceof ReferenceError) {
        console.log(error.message);
    } else {
        console.log(error.stack);
    }
}

// Dengan operator instanceOf, kita bisa mendapatkan tipe dari eror yang terjadi. Dari sana kita bisa membuat percabangan bagaimana cara menangani erornya.