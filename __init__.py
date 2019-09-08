# -*- encoding: utf-8 -*-
import qrcode
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL

qr = qrcode.make('https://qr.id.vin/hook?url=http://210.211.99.9:8889/api&method=GET')
qr.save('test.png')

qr1 = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

data = 'https://www.facebook.com/danh.nguyencong.73'
qr1.add_data(data)
qr1.make(fit=True)
img = qr1.make_image(fill='black', back_color='white')
img.save('test1.png')

app = Flask(__name__)

app.config["DEBUG"] = True
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = '210.211.99.9'
app.config['MYSQL_USER'] = 'cuongdm9'
app.config['MYSQL_PASSWORD'] = '123456c@'
app.config['MYSQL_DB'] = 'coding_house'
mysql = MySQL(app)

form_data_tr1 = {
    "data": {
        "metadata": {
            "app_name": "Congratulation Wedding",
            "app_id": 123456,
            "title": "𝓦𝓮𝓭𝓭𝓲𝓷𝓰 𝓐𝓷𝓷𝓲𝓿𝓮𝓻𝓼𝓪𝓻𝔂",
            "submit_button": {
                "label": "Gửi thông tin",
                "background_color": "#6666ff",
                "cta": "request",
                "url": "http://210.211.99.9:8889/add_data",
            },
            "elements": [
                {
                    "type": "web",
                    "content": "<img src='http://210.211.99.9:8889/static/images/a2.png' alt='Smiley face'>",
                },
                {
                    "label": "Tên người mừng tiền?",
                    "type": "input",
                    "input_type": "textarea",
                    "display_type": "inline",
                    "required": True,
                    "name": "name_joiner"
                },
                {
                    "label": "Bạn có tham gia vào tiệc cưới không?",
                    "type": "radio",
                    "display_type": "inline",
                    "required": True,
                    "name": "joined",
                    "options": [{
                        "label": "Chấp Nhận",
                        "value": "accept"
                    }, {
                        "label": "Từ Chối",
                        "value": "refuse"
                    }
                    ]
                },
                {
                    "label": "Bạn muốn mừng bao nhiêu tiền?",
                    "type": "radio",
                    "display_type": "inline",
                    "required": True,
                    "name": "money",
                    "options": [{
                        "label": "200.000 vnd",
                        "value": 200000
                    }, {
                        "label": "300.000 vnd",
                        "value": 300000
                    }, {
                        "label": "500.000 vnd",
                        "value": 500000
                    }, {
                            "label": "9999999 vnd",
                            "value": 999999
                        }
                    ]
                },
                {
                    "label": "Lời chúc!",
                    "type": "input",
                    "input_type": "textarea",
                    "display_type": "inline",
                    "required": True,
                    "name": "message"
                },
            ]
        }
    }
}

form_data_tr2 = {
    "data": {
        "metadata": {
            "app_name": "Congratulation Wedding",
            "app_id": 123456,
            "title": "Gia đình chúng tôi rắt cảm ơn!",
            "submit_button": {
                "label": "Thêm thông tin",
                "background_color": "#6666ff",
                "cta": "url",
                "url": "http://210.211.99.9:8889",
            },
            "elements": [
                {
                    "type": "web",
                    "content": "<img src='http://210.211.99.9:8889/static/images/a2.png' alt='Smiley face'>",
                },
                {
                    "label": "",
                    "type": "input",
                    "input_type": "textarea",
                    "display_type": "inline",
                    "required": True,
                    "name": "message"
                }
            ]
        }
    }
}


@app.route('/start', methods=['GET'])
def api_all():
    user_id = request.headers.get("user_id")
    print(user_id)
    device_id = request.headers.get("device_id")
    print(device_id)
    scanner_version = request.headers.get("scanner_version")
    print(scanner_version)
    os_version = request.headers.get("os_version")
    print(os_version)
    timestamp = request.headers.get("timestamp")
    print(timestamp)
    session = request.headers.get("session")
    print(session)
    return jsonify(form_data_tr1)


@app.route('/admin')  # admin
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students WHERE id=3")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', students=data)


@app.route('/')  # index /
def new():
    return render_template('index.html')


@app.route('/add_data', methods=['POST'])
def insert1():
    if request.method == "POST":
        tiengui = int(request.json['money'])
        loichuc = request.json['message']
        tennguoigui = request.json['name_joiner']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO history_gift (name, monney_gift, comment ) VALUES (%s, %s, %s)",
                    (tennguoigui, tiengui, loichuc))
        mysql.connection.commit()
        flash("Data Inserted Successfully")
        return jsonify(form_data_tr2)


@app.route('/admin/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name1']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        cur1 = mysql.connection.cursor()
        cur1.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/admin/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/admin/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8889')
