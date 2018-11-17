from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/send', methods=['GET','POST'])
def send():
    if(request.method=='POST'):

        def grade(percent):
            if(percent>=90):
                return 'S'
            elif(percent>=80):
                return 'A'
            elif(percent>=70):
                return 'B'
            elif(percent>=60):
                return 'C'
            elif(percent>=50):
                return 'D'
            else:
                return 'F'

        
    

        stuName = request.form['name']
        regNum = request.form['regNum']
        sem = request.form.get('sem')
        collName = request.form['collName']

        name = [0,0,0,0]
        mark = [0,0,0,0]
        total = [0,0,0,0]
        per = [0,0,0,0]
        gra = [0,0,0,0]
        name[0] = request.form['name1']
        mark[0] = int(request.form['mark1'])
        total[0] = int(request.form['total1'])

        name[1] = request.form['name2']
        mark[1] = int(request.form['mark2'])
        total[1] = int(request.form['total2'])

        name[2] = request.form['name3']
        mark[2] = int(request.form['mark3'])
        total[2] = int(request.form['total3'])

        name[3] = request.form['name4']
        mark[3]= int(request.form['mark4'])
        total[3]= int(request.form['total4'])

        for i in range(0,3):
            per[i] = ( mark[i]/total[i] ) * 100
            
        for i in range(0,3):
            gra[i] = grade(per[i])
        status = 'Pass' 
        for i in range(0,3):
            if(gra[i] == 'F'):
                status='Fail'
    

    return render_template('marklist.html', stuName=stuName, regNum=regNum,sem=sem,collName=collName, name=name, mark=mark, total=total, gra=gra, status=status)


if(__name__ == '__main__'):
    app.run(debug='True')