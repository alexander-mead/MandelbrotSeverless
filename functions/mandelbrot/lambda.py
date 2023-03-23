import json
import base64

# TODO: Check on relative import vs. ... import
# from . import mandelbrot
import mandelbrot


def unwrap_payload(event):
    if "body" not in event:  # Get body
        raise Exception("No body in request")
    else:
        body = event["body"]
    if "isBase64Encoded" in event:  # Decode
        if event["isBase64Encoded"]:
            body = base64.b64decode(body)
    try:  # Parse
        payload = json.loads(body)
    except:
        raise Exception("Could not parse body as JSON")
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
    real_centre = float(body["real"])
    imag_centre = float(body["imag"])
    patch_size = float(body["size"])
    rmin, rmax = real_centre-patch_size/2., real_centre+patch_size/2.
    imin, imax = imag_centre-patch_size/2., imag_centre+patch_size/2.
    max_iters = 64
    width, height = 1000, 1000
    data = mandelbrot.create_image(
        rmin, rmax, imin, imax, max_iters, width, height)
    data = base64.b64encode(data)  # Encode to base64 bytes
    data = data.decode()           # Convert bytes to string

    # Construct the response
    status = 200  # 200 = OK
    headers = {  # Headers are necessary for CORS
        # "Access-Control-Allow-Headers": "Origin, Content-Type, Accept",
        # "Access-Control-Allow-Origin": "*",  # NOTE: Necessary
        # "Access-Control-Allow-Methods": "OPTIONS, POST, GET",
        # "Access-Control-Allow-Credentials": "true",
        # "Access-Control-Expose-Headers": "x-api-id",
        # "Access-Control-Max-Age": "300",
        # "Access-Control-Allow-Methods": "*",
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "*",
        "Access-Control-Expose-Headers": "x-api-id",
        "Access-Control-Max-Age": "300",
        "Access-Control-Allow-Methods": "*",
    }
    response = {
        "message": "Request received.",
        "data": data,
    }

    # Return the response
    result = {
        "statusCode": status,
        "headers": headers,
        "body": json.dumps(response),  # NOTE: This json.dumps is necessary!
    }
    return result
