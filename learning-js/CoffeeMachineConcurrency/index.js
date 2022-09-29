console.log("Selamat datang");
setTimeout(() => {
    console.log("Terima kasih sudah berkunjung, silakan datang kembali")
}, 4000);
console.log("Ada yang bisa dibantu?");

/* const orderCoffee = () => {
    let coffee = null;
    console.log("Sedang membuat kopi, silakan tunggu..");
    setTimeout(() => {
        coffee = "Kopi sudah jadi";
    }, 3000);
    return coffee;
}
console.log(orderCoffee()); */

// tapi kalau kayak gini, kopinya tidak akan pernah jadi, 
// sebab fungsi itu cuma mengembalikan satu return aja. 
// dan setelah udah ngerjain return, fungsi nya juga sepenuhnya berhenti dan gak bekerja lagi. 
// solusinya gimnaa? caranya pakai callback function:

const orderCoffee = callback => {
    let coffee = null;
    console.log("Sedang membuat kopi, silakan tunggu.");
    setTimeout(() => {
        coffee = "Kopi sudah jadi";
        callback(coffee);
    }, 3000);
    return coffee;
}

/* const coffee = orderCoffee();
console.log(coffee); ini nggak bisa dipakai, pakainya ini ya:*/

orderCoffee(coffee => {
    console.log(coffee);
});

const executorFunction = (resolve, reject) => {
    const isCoffeeMakerReady = true;
    if (isCoffeeMakerReady) {
        resolve("Kopi bisa dibuat");
    }
    else {
        reject("Mesin kopi tidak bisa digunakan");
    }
}

const makeCoffee = () => {
    return new Promise(executorFunction);
}

const coffeePromise = makeCoffee();
console.log(coffeePromise);
