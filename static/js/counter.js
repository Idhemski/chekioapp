const textArea = document.querySelector('textarea');
const counterDivision = document.querySelector('#the-count');

const current = document.querySelector('#current');      // how many letters were typed
const maximum = 10000;                                  // the maximum of letters typed 

textArea.addEventListener("keydown", (event) => {
  const typedCharacters = textArea.value.length;
  if (typedCharacters > maximum) {
    return false;
  }
  current.textContent = typedCharacters;

}, false);




