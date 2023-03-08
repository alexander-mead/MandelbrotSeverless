# Mandelbrot serverless

This repository acts as an example of how we can build serverless applications for AWS.
Here we will be using the [Serverless Framework](https://serverless.com/) to build our application.

## Quick-start

1. You will need an `AWS Account` and these dependencies:

    1. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions)
    2. [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
    3. [Docker](https://www.docker.com/)
    4. [Python](https://www.python.org/)
    5. [Poetry](https://python-poetry.org/docs/#installation)

2. Log into AWS through the CLI. Freddy can find your `Access Key ID` and `Secret Access Key` using root:

```bash
aws configure
> AWS Access Key ID: <your access key>
> AWS Secret Access Key: <your secret key>
> Default region name: eu-west-1
> Default output format: json
```

2. Download this repository and change to the top-level directory:

```bash
git clone https://github.com/digiLab-ai/aws.git
cd aws
```

3. Build package the architecture:

```bash
sam build
```

4. Deploy the architecture to AWS. You will need to input the required parameters in the [template.yml](template.yml) file:

```bash
sam deploy --guided
> Stack Name: twinlab
```

5. After you're done, you can delete the architecture:

```bash
aws cloudformation delete-stack --stack-name twinlab
```

## Local Development

You can run the application locally with:

```bash
sam local start-api
```

After which you can perform a `GET` request to `localhost`:

```bash
curl http://localhost:3000/preprocess
```

## Usage

### Creating a new campaign

You can create a new campaign entry for a given user by performing a `POST` request to the `/campaign` endpoint:

```shell
curl -i -X POST http://127.0.0.1:3000/campaign/new -H 'Content-Type: application/json' -d '{"id":"test", "userId": "freddy", "data": "x1,x2,y1\n1,2,3\n4,5,6\n7,8,9" }'
```

Note that you will have to send a dictionary containing all of the required fields. The response will be a HTTP response with `200` status code indicating success, and anything else for a failure.
