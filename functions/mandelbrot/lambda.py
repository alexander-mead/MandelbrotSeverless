import json
import base64

# TODO: Check on relative import vs. ... import
# from . import mandelbrot
import mandelbrot


def unwrap_payload(event):
    if "body" not in event:  # Get body
        raise Exception("No body in request.")
    body = event["body"]
    if "isBase64Encoded" in event:  # Decode
        if event["isBase64Encoded"]:
            body = base64.b64decode(body)
    try:  # Parse
        payload = json.loads(body)
    except:
        raise Exception("Could not parse body as JSON.")
    return payload


def handler(event, context, verbose=True):
    # Necessary for lambda.py

    # See what the handler receives
    if verbose:
        print()
        print("Event:", type(event), event, "\n")
        print("Event body:", type(event["body"]), event["body"], "\n")
        print("Context:", type(context), context, "\n")

    # Generate image
    body = unwrap_payload(event)
    real_centre, imag_centre, patch_size = float(  # TODO: This is ugly as fuck
        body["real"]), float(body["imag"]), float(body["size"])
    rmin, rmax = real_centre-patch_size/2., real_centre+patch_size/2.
    imin, imax = imag_centre-patch_size/2., imag_centre+patch_size/2.
    max_iters = 50
    width, height = 200, 200
    data = mandelbrot.create_image(
        rmin, rmax, imin, imax, max_iters, width, height)

    # Return the response
    response = {
        "message": "Request received.",
        # "data": json.dump(data.encode("base64")),
        "data": str(data),
    }
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*", 
            "Access-Control-Allow-Methods": "GET, POST", 
        },
        "body": json.dumps(response),
    }
