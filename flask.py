from flask import Flask,request,jsonify
import pymysql

app = Flask(__name__)

db_config = {
    'user':'root',
    'password': '',
    'host': 'localhost',
    'database':'voting_db'
}
def get_db_connection():
    return pymysql.connect(
        user=db_config['root'],
        password=db_config['password'],
        host=db_config['localhost'],
        database=db_config['voting_db'],
        cursorclass=pymysql.cursors.DictCursor
    )
@app.route('/vote',methods=['POST'])
def vote():
    candidate = request.json.get('candidate')
    if not candidate:
        return jsonify({'error': 'Candidate not specified'}), 400
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
         cursor.execute("INSERT INTO votes1 (candidate) VALUES (%S)"),
        ((candidate,))
        conn.commit()
        cursor.close()
        return jsonify({'message': 'Vote recorded successfully'}),200
    except pymysql.MySQLError as err:print(f"Error:{err}") 
    return jsonify({'error':str(err)}),500

@app.route('results',methods=['GET'])
def result():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
         cursor.execute("SELECT candidate,COUNT(*) as votes1 FROM votes1 GROUP BY candidate")
        results = cursor.fetchall()
        conn.close()
        return jsonify(results),200
    except pymysql.MySQLError as err: print(f"Error: {err}")
    return jsonify({'error':str(err)}),500
    if __name__ == '__main__':
        app.run(debug=True)
               
           
        
        
