import os

if 'AWS_LAMBDA_EXEC_WRAPPER' in os.environ:
    del os.environ['AWS_LAMBDA_EXEC_WRAPPER']
