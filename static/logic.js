const baseUrl = "http://localhost:3000"

const image = () => {

    // Definitions
    const real = document.getElementById("real").value;
    const imag = document.getElementById("imag").value;
    const size = document.getElementById("size").value;
    
    const url = baseUrl+"/mandelbrot";
    const params = {
        method: "POST", // Unless this is present it will default to "GET"
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
            size: size,
        })
    };

    // Fetch
    fetch(url, params)
        .then((response) => response.json()) // TODO: Use response.blob()
        .then((blob) => {
            console.log("Response blob received");
            console.log("Blob: "+blob);
            //console.log(blob);
            //const objectURL = blob.data;
            const data = blob.data;
            const image = "data:image/png;base64,"+data;
            //console.log("Image: "+image);
            document.getElementById("image").src = image; // To set image within html
            console.log("Image displayed")
        })
        //.then(document.getElementById("buttonId").disabled = true) // TODO: Disable button to prevent multiple requests
        .then("Hello!")
        .catch((error) => {
            console.log('Error:', error)
            console.log("Failed to sample image");
        });
}