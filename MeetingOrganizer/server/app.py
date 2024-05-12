from flask import Flask,jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#Solution the cors problem
cors = CORS(app, resources={r'/api/*': {'origins': 'http://localhost:8000'}})

#Database connection: 
basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(instance_path, 'mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


# Meeting sınıfı veritabanındaki meetings tablosunu temsili
class Meeting(db.Model):
    __tablename__ = 'meetings'
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    participants = db.Column(db.String(255), nullable=False)
    
# Kök URL'yi işleyecek route tanımlama
@app.route("/")
def home():
    return "Hello, Flask"
#Toplantıları listeleme endpointi
@app.route('/api/meetings', methods=['GET'])
def get_meetings():
    meetings = Meeting.query.all()
    meeting_list = []
    for meeting in meetings:
        meeting_data ={
            'id': meeting.id,
            'topic': meeting.topic,
            'date': meeting.date,
            'start_time': meeting.start_time,
            'end_time': meeting.end_time,
            'participants': meeting.participants          
        }
        meeting_list.append(meeting_data) 
    return jsonify(meeting_list)

#Toplantı oluşturma endpointi
@app.route('/api/meetings', methods=['POST']) 
def create_meeting():
    meeting_data = request.json
    new_meeting = Meeting(
        topic=meeting_data['topic'],
        date=meeting_data['date'],
        start_time=meeting_data['startTime'],
        end_time=meeting_data['endTime'],
        participants=meeting_data['participants']
    )
    db.session.add(new_meeting)
    db.session.commit()
    return jsonify({'message': 'Meeting created successfully'}), 201

#Toplantı güncelleme endpointi
@app.route('/api/meetings/<int:meeting_id>', methods=['PUT'])
def update_meeting(meeting_id):
    meeting = Meeting.query.get_or_404(meeting_id)
    meeting_data = request.json
    meeting.topic = meeting_data.get('updateTopic', meeting.topic)
    meeting.date = meeting_data.get('updateDate',meeting.date)
    meeting.start_time = meeting_data.get('updateStartTime', meeting.start_time)
    meeting.end_time = meeting_data.get('updateEndTime',meeting.end_time) 
    meeting.participants = meeting_data.get('updateParticipants', meeting.participants)
    db.session.commit()
    return jsonify({'message': 'Meeting updated successfully'})

#Toplantı silme endpointi
@app.route('/api/meetings/<int:meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    meeting = Meeting.query.get_or_404(meeting_id)
    db.session.delete(meeting)
    db.session.commit()
    return jsonify({'message': 'Meeting deleted successfully'})
   
if __name__ == '__main__':
    app.run(debug=True)
