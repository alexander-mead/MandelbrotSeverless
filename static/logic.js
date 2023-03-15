const baseUrl = "http://localhost:3000"

const image = () => {

    // Definitions
    const real = document.getElementById("real").value;
    const imag = document.getElementById("imag").value;
    
    const url = baseUrl+"/plot";
    const params = {
        method: "POST", // Unless this is present it will default to "GET"
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
        })
    };

    // Fetch
    fetch(url, params)
        .then((response) => response.blob())
        .then((blob) => {
            console.log("Response blob received");
            const objectURL = URL.createObjectURL(blob);
            document.getElementById("image").src = objectURL; // To set image within html
        })
        //.then(document.getElementById("buttonId").disabled = true) // TODO: Disable button to prevent multiple requests
        .then(console.log("Image displayed"))
        .catch((error) => {
            console.log('Error:', error)
            console.log("Failed to sample image");
        });
}