import json
import boto3, botocore
from flask import Flask,  request, g, jsonify
from config import S3_KEY, S3_SECRET, S3_BUCKET

s3 = boto3.resource(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)

app = Flask(__name__)
app.config.from_object("config")

@app.route("/", methods=["GET"])
def getData():
    obj = s3.Object("innovation-arts", "data.json")
    body = obj.get()['Body'].read()
    return body

@app.route("/", methods=["POST"])
def appendData():
    if hasattr(request,"data") & (request.headers['Content-Type'] == 'application/json'):
        obj = s3.Object("innovation-arts", "data.json")
        body = obj.get()['Body'].read()
        body = body.decode("utf8").replace("'", '"')
        body = json.loads(body)
        body.append(request.json.get("data"))
        with open("/tmp/temporary_file","wb") as fo:
            fo.write(json.dumps(body).encode("utf-8"))
        s3.meta.client.upload_file(
                        "/tmp/temporary_file",
                        "innovation-arts",
                        "data.json"
                    )
        return "updated"
    else:
        return "Invalid request"
    
if __name__ == "__main__":
    app.run()