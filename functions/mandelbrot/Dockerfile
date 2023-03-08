# Base image (specifying OS etc.)
FROM public.ecr.aws/lambda/python:3.9

# Lambda code
COPY lambda.py requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .

# What is actually run (entry point)
CMD ["lambda.handler"]