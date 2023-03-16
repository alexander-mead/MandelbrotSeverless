# Mandelbrot serverless

This repository acts as an example of how to build serverless applications for Amazon Web Services (AWS).
This is done using the [Serverless Framework](https://serverless.com/) to build the application. This is also
known as the serverless application model (SAM).

## Quick-start

1. You need an `AWS Account` and these dependencies:
   - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions)
   - [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
   - [Docker](https://www.docker.com/)
   - [Python](https://www.python.org/)
   - [Poetry](https://python-poetry.org/docs/#installation)

2. Log into AWS through the command line interface (CLI). 
You need to find your `Access Key ID` and `Secret Access Key` using Identity and Access Management (IAM) after logging on to your AWS account:
```bash
aws configure
> AWS Access Key ID: <your access key>
> AWS Secret Access Key: <your secret key>
> Default region name: eu-west-1
> Default output format: json
```

3. Clone this repository and `cd` to the top-level directory.

4. Build and package the architecture:
```bash
sam build
```

5. Deploy the architecture to AWS. You will need to input the required parameters in the [template.yml](template.yml) file:
```bash
sam deploy
```
will deploy to the AWS cloud using information in the included `samconfig.toml` file. After you're done, you can delete the architecture:
```bash
aws cloudformation delete-stack --stack-name mandelbrot
```

Alternatively, you can run the api locally with:
```bash
sam local start-api
```

After either local or remote deployment, you can trigger the `lambda` function in any of three ways:

1. After which you can perform a `POST` request to `localhost`. For example (for local deployment):
```bash
curl -i -X POST http://127.0.0.1:3000/mandelbrot \
    -H 'Content-Type: application/json' \
    --output mandelbrot.json \
    --data-binary @- << EOF
{ 
    "real": "-0.5", 
    "imag": "0.", 
    "size": "2." 
}
EOF
```
which can also be found in `events/trigger.sh`. The output of the request is then in `mandelbrot.json`

1. Otherwise, you can run the `python` code in `events/trigger.py`:
```bash
python events/trigger.py -0.5 0. 2.
```
which takes arguments for the real, imaginary and size parameters, respectively. This will create `test.html`, where the Mandelbrot set can then be viewed in a browser.

1. Finally, the `lambda` can be invoked via the webpage in `static/index.html`, which will automatically update once the lambda has generated a new Mandelbrot set image.