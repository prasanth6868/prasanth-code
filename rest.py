from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
 
stuDB=[
{
"name": "apple",
"age": 17,
"course": "Computer Science",
"dept": "Computer"
}
]
'''@app.route('/studb/student',methods=['GET'])

def getAllstu():

    return jsonify({'stu':stuDB})'''

@app.route('/studb/student/<stdId>',methods=['GET'])

def getStu(stuId):

     usr=[stu for stu in stuDB if (stu['id']==stuId)] 

     return jsonify({'stu':usr})

@app.route('/studb/student/<stdId>', methods=['PUT'])

def updateStu(stuId):

     st=[stu for stu in stuDB  if (stu['id']==stuId)]

     if 'name' in request.josn :

@app.route('/studb/student',methods=['POST'])

def createStu():

    data = {

    'id':request.json['id'],

    'name':request.json['name'],

    'course':request.json['title']
    
    'age':request.json['age']

    }

    stuDB.append(dat)

    return jsonify(dat)




@app.route('/studb/student/<stuId>',methods=['DELETE'])

def deleteStu(stuId):

    st = [ st for st in stuDB if (stu['id'] == stuId) ]

    if len(st) == 0:

       abort(404)

    stuDB.remove(st[0])

    return jsonify({'response':'Success'})



if __name__ == '__main__':

 app.run() 
