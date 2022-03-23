function generate_HTML(cupcake){
    return`
    <div data-id=${cupcake.id}>
    <li>${cupcake.flavor}</li>
    <li><button class='delete'>X</button></li>
    
    </div>`
    
}

const BASE_URL = "http://localhost:5000/api";

async function showCupcakes() {
    let response = await axios.get(`${BASE_URL}/cupcakes`);

    for (let data of response.data.cupcakes) {
        let newCupcake =$(generate_HTML(data));
        $("#cupcakes-list").append(newCupcake);
    }
}

// handle cupcake submit

$("#cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();
  
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-img").val();
  
    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });
  
    let newCupcake = $(generateHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#cupcake-form").trigger("reset");
  });
  



$(showCupcakes)