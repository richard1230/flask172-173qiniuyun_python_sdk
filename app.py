from flask import Flask,jsonify,render_template
import qiniu

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/uptoken/')
def uptoken():#这个需要自己申请一个
    access_key = '6C0-gZV-pWuDoRiRU1tq14P5gW1wFbq0GEtq_zeP'
    secret_key = 'AgPOGPd3MLamYt4U-5rhl8LRcxRxEf_ljrotu0Gn'
    q = qiniu.Auth(access_key,secret_key)

    bucket = 'richard1230'#存储空间名字
    token = q.upload_token(bucket)
    return jsonify({'uptoken':token})


if __name__ == '__main__':
    app.run()
