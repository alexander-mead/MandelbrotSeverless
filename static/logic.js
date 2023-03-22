// const baseURL = "http://127.0.0.1:3000";
const baseURL = "https://0hku56rtzd.execute-api.eu-west-1.amazonaws.com/Prod";

const image = () => {
  // Definitions
  const real = document.getElementById("real").value;
  const imag = document.getElementById("imag").value;
  const size = document.getElementById("size").value;
  const url = baseURL + "/mandelbrot";
  const params = {
    method: "POST", // Unless this is present it will default to "GET"
    headers: {
      "Content-Type": "application/json",
      // Uncommenting the below makes this fail
      // TODO: Figure out CORS headers
      // "Access-Control-Allow-Headers": "Content-Type",
      // "Access-Control-Allow-Origin": "*",
      // "Access-Control-Allow-Credentials": "true",
      // "Access-Control-Expose-Headers": "x-api-id",
      // "Access-Control-Max-Age": "300",
      // "Access-Control-Allow-Methods": "*",
    },
    body: JSON.stringify({
      real: real,
      imag: imag,
      size: size,
    }),
  };

  // Fetch
  console.log("Request sent");
  fetch(url, params)
    .then((response) => response.json()) // TODO: Not blob; maybe use response.blob()?
    .then((blob) => {
      console.log("Response blob received");
      console.log("Blob: " + blob);
      //console.log(blob);
      //const objectURL = blob.data;
      const data = blob.data;
      const image = "data:image/png;base64," + data;
      //console.log("Image: "+image);
      document.getElementById("image").src = image; // To set image within html
      console.log("Image displayed");
    })
    // TODO: Disable button to prevent multiple requests
    //.then(document.getElementById("buttonId").disabled = true)
    .catch((error) => {
      console.log("Error:", error);
      console.log("Failed to sample image");
    });
};
