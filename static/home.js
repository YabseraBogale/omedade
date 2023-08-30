const data=['Arada Branch','Awassa Branch', 'Axum Branch', 'Bahirdar Branch', 'Board'
            ,'Bole Branch' ,'Commercial Division' ,'Diredawa Branch', 'Finance'
            ,'GM OPERATIONS' ,'GM SUPPORT' ,'Gonder Branch' ,'HRGS' ,'HRGS Olympia site'
            ,'IT & FCR', 'Jimma Branch', 'Mekelle Branch', 'Meshualekia No 2 Branch'
            ,'Nazreth Branch', 'Olympia Branch', 'Procurment Division', 'Product manager'       
            ,'Special Sales & Pricing' ,'Technical Division']


const input=document.getElementById("departement")
const autocomplete=document.getElementById("autocomplete")


const d=document.getElementsByTagName("body")
d.style.color="red"

input.oninput= ()=> {
    let results = [];
    const userInput = this.value;
    autocomplete.innerHTML = "";
    if (userInput.length > 0) {
        results = getResults(userInput);
        autocomplete.style.display = "block";
        for (i = 0; i < results.length; i++) {
            autocomplete.innerHTML += "<li>" + results[i] + "</li>";
        }
    }
}

function getResults(input) {
    const results = [];
    for (i = 0; i < data.length; i++) {
      if (input === data[i].slice(0, input.length)) {
        results.push(data[i]);
      }
    }
    return results;
  }

  autocomplete.onclick = function (event) {
    const setValue = event.target.innerText;
    autocomplete.value = setValue;
    this.innerHTML = "";
  };