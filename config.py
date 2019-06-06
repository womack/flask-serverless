import os
S3_BUCKET                 = os.environ["S3_BUCKET_NAME"]
S3_KEY                    = os.environ["S3_ACCESS_KEY"]
S3_SECRET                 = os.environ["S3_SECRET_ACCESS_KEY"]
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000


print(S3_BUCKET)
print(S3_KEY)
print(S3_SECRET)