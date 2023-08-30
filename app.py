from flask import Flask,render_template,url_for,request,session
from markupsafe import escape
from database import Bollo





db=Bollo()
app= Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        departement=escape(request.form['departement'])
        if departement=='':
            return render_template('home.html')
        if db.DepartementExists(departement)==False:
            return render_template('home.html',lst="departement dosesn't exist")
        if db.DepartementExists(departement)==True:
            lst=db.seePlateNoAndRemark(departement)
            return render_template('home.html',lst=lst)
    return render_template('home.html')



@app.route('/new_plate',methods=['GET','POST'])
def new_plate():
    if request.method=='POST':
        departement=escape(request.form['departement'])
        new_plate=escape(request.form['new_plate'])
        remark=escape(request.form['remark'])
        done=db.insertIntoTableNew(new_plate,departement,remark)
        if done=="Added":
            return render_template('sucess.html',mesg=done)
    return render_template('new_plate.html')


@app.route('/update_remark',methods=['GET','POST'])
def update_remark():
    if request.method=='POST':
        plate_no=escape(request.form['plate_no'])
        remark=escape(request.form['remark'])
        update=db.UpdateRemark(remark,plate_no)
        if update=="Updated":
            return render_template('sucess.html',mesg=update)
    
    return render_template('update_remark.html')


@app.route('/date',methods=['GET','POST'])
def date():
    if request.method=='POST':
        plate_no=escape(request.form['plate_no'])
        remark=db.getRemarkDate(plate_no)
        return render_template('remark_date.html',date=remark)


    return render_template('remark_date.html')




if __name__=="__main__":
    app.run(debug=True)