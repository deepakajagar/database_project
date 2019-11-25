from flask import Flask,redirect,url_for,render_template,request
import pymysql
import pymysql.cursors
app = Flask(__name__)
  
 
# Connect to the database.
def connect():
	connection = pymysql.connect(host='localhost',
                             user='root',
                             password='deepanjali@2000',                             
                             db='technieks',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

	cursor = connection.cursor()
	return connection,cursor


#storing signup details in database
@app.route('/signup/',methods = ['GET','POST'])
def signup():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		name = inp['fullname']
		usn = inp['usn']
		# branch = inp['branch']
		branchname = request.form.get("Branch",None)
		if branchname == None:
			return redirect(url_for('signup'))
		# inp = request.form
		num = (inp['phnum'])
		# yea = int(inp['passyear'])
		pas = inp['psw']
		cursor = connection.cursor()
		cursor.execute("select usn from users where usn=%s",(str(name,)))
		data = cursor.fetchall()
		if data:
			return(redirect(url_for('exist_user_signup')))
		else:
			querry = "insert into users values(%s,%s,%s,%s,%s)"
			cursor.execute(querry,(name,usn,branchname,num,pas))
			connection.commit()
			connection.close()	
			return(redirect(url_for('login')))
	return render_template('Signup.html')


@app.route('/exist_user_signup/',methods=['GET','POST'])
def exist_user_signup():
	return render_template('exist_user_signup.html')



@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')
	if request.method=='POST':
		if request.form['Login']:
			return redirect(url_for('login'))
		if request.form['Sign Up']:
			return redirect(url_for('signup'))
		if request.form['Admin?']:
			return redirect(url_for('admin_login'))
		else:
			if request.method == 'GET':
				return render_template('home.html')


@app.route('/admin_login/',methods = ['GET','POST'])
def admin_login():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		name = inp['uname']
		pas = inp['psw']
		cursor = connection.cursor()
		querry = "select password from admin where usn=%s"
		cursor.execute(querry,(name,))
		result = cursor.fetchall()
		if result: 
			tempp = str(result[0]['password'])
			if tempp == str(pas):
				return redirect(url_for('admin_firstpage'))
			else:
				return redirect(url_for('admin_wrong_password'))
		else:
			return render_template('Login.html')
	return render_template('admin_login.html')	
	connection.close()


@app.route('/admin_wrong_password/',methods=['GET','POST'])
def admin_wrong_password():
	return render_template('admin_wrong_password.html')



@app.route('/admin_firstpage/',methods=['GET','POST'])
def admin_firstpage():
	return render_template('admin_firstpage.html')
	if request.method=='POST':
		if request.form['Go to Committees']:
			return redirect(url_for('admin_committee'))
		if request.form['Go to Championship Table']:
			return redirect(url_for('admin_championship'))
		# if request.form['Go to Cultural Events']:
		# 	return redirect(url_for('view_cultural_table')) 
		else:
			if request.method == 'GET':
				return render_template('admin_firstpage.html')


@app.route('/admin_committee/',methods = ['GET','POST'])
def admin_committee():
	return render_template('admin_committee.html')
	if request.method=='POST':
		if request.form['Office Bearers']:
			return redirect(url_for('top_3'))
		if request.form['Cultural Committee']:
			return redirect(url_for('admin_cultural'))
		if request.form['Design Committee']:
			return redirect(url_for('admin_design')) 
		# if request.form['Sponsorship Committee']:
		# 	return redirect(url_for('admin_sponsorship'))
		if request.form['Marketing Committee']:
		   	return redirect(url_for('admin_marketing'))
		if request.form['ALL']:
			return redirect(url_for('create_usingjoin'))
		# if request.form['Hospitality Committee']:
		# 	return redirect(url_for('admin_hospitality'))
		else:
			if request.method == 'GET':
				return render_template('admin_committee.html')




@app.route('/admin_championship/',methods=['GET','POST'])
def admin_championship():
	return render_template('admin_championship.html')
	if method.request=='POST':
		if request.form['Girls']:
			return(redirect(url_for('gupdate')))
		if request.form['Boys']:
			return(redirect(url_for('bupdate')))
		# if request.form['Overall']:
		# 	return redirect(url_for('overall')) 
		else:
			if request.method == 'GET':
				return render_template('admin_championship.html')	


@app.route('/gupdate/',methods=['GET','POST'])
def gupdate():
	return render_template('updateview.html')



@app.route('/bupdate/',methods=['GET','POST'])
def bupdate():
	return render_template('updateview.html')

#when cultural button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/admin_cultural/',methods=['GET','POST'])
def admin_cultural():
	return render_template('cadd_delete.html')



#when design button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/admin_design/',methods=['GET','POST'])
def admin_design():
	return render_template('dadd_delete.html')



#when marketing button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/admin_marketing/',methods=['GET','POST'])
def admin_marketing():
	return render_template('madd_delete.html')



#when sponsorship button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
# @app.route('/admin_sponsorship/',methods=['GET','POST'])
# def admin_sponsorship():
# 	return render_template('add_delete.html')



#checking if usn matched from database else return signup page
@app.route('/login/',methods = ['GET','POST'])
def login():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		name = inp['uname']
		pas = inp['psw']
		cursor = connection.cursor()
		querry = "select password from users where usn=%s"
		cursor.execute(querry,(name,))
		result = cursor.fetchall()
		if result: 
			tempp = str(result[0]['password'])
			if tempp == str(pas):
				return redirect(url_for('firstpage'))
			else:
				return redirect(url_for('wrong_password'))
		else:
			return render_template('signup_when_no_user.html')
	return render_template('login.html')	
	connection.close()
	




@app.route('/wrong_password/',methods=['GET','POST'])
def wrong_password():
	return render_template('wrong_password.html')



@app.route('/signup_when_no_user/',methods=['GET','POST'])
def sec_signup():
	return render_template('signup_when_no_user.html')
	if request.method=='POST':
		if request.form['Sign Up']:
			return redirect(url_for('signup'))
		if request.form['Home']:
			return redirect(url_for('home'))
		else:
			if request.method == 'GET':
				return render_template('signup_when_no_user.html')




@app.route('/committee/',methods = ['GET','POST'])
def committee():
	return render_template('committee.html')
	if request.method=='POST':
		if request.form['Office Bearers']:
			return redirect(url_for('top_3'))
		if request.form['Cultural Committee']:
			return redirect(url_for('cultural'))
		if request.form['Design Committee']:
			return redirect(url_for('design')) 
		# if request.form['Sponsorship Committee']:
		# 	return redirect(url_for('sponsorship'))
		if request.form['Marketing Committee']:
		   	return redirect(url_for('marketing'))
		# if request.form['Reception Committee']:
		# 	return redirect(url_for('reception'))
		# if request.form['Hospitality Committee']:
		# 	return redirect(url_for('hospitality'))
		else:
			if request.method == 'GET':
				return render_template('committee.html')






#when top_3 button pressed;return the details of the top_3 holders with their details(READ ONLY)
@app.route('/top_3/',methods=['GET','POST'])
def top_3():
	connection,cursor=connect()
	cursor.execute("select name,usn,position,tele from admin")
	result = cursor.fetchall()
	connection.close()
	return render_template('table.html',data = result)




#when cultural button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/cultural/',methods=['GET','POST'])
def cultural():
	return render_template('cul_core_volunteers.html')



#when design button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/design/',methods=['GET','POST'])
def design():
	return render_template('des_core_volunteers.html')






#when marketing button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/marketing/',methods=['GET','POST'])
def marketing():
	return render_template('mar_core_volunteers.html')



#when sponsorship button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
# @app.route('/sponsorship/',methods=['GET','POST'])
# def sponsorship():
# 	return render_template('spo_core_volunteers.html')




#when cultural button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/c_cultural/',methods=['GET','POST'])
def c_cultural():
	connection,cursor=connect()
	cursor.execute("select name,usn,position,tele from committee_data where cno = %s and (position = %s or position = %s)",(1,"core","convenor"))
	result = cursor.fetchall()
	connection.close()
	return render_template('table.html',data = result)



#when design button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/c_design/',methods=['GET','POST'])
def c_design():
	connection,cursor=connect()
	cursor.execute("select name,usn,position,tele from committee_data where cno = %s and (position = %s or position = %s)",(2,"core","convenor"))
	result = cursor.fetchall()
	connection.close()
	return render_template('table.html',data = result)





#when marketing button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/c_marketing/',methods=['GET','POST'])
def c_marketing():
	connection,cursor=connect()
	cursor.execute("select name,usn,position,tele from committee_data where cno = %s and (position = %s or position = %s)",(5,"core","convenor"))
	result = cursor.fetchall()
	connection.close()
	return render_template('table.html',data = result)



#when sponsorship button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
# @app.route('/c_sponsorship/',methods=['GET','POST'])
# def c_sponsorship():
# 	connection,cursor=connect()
# 	cursor.execute("select name,usn,position,tele from committee_data where cno = %s and (position = %s or position = %s)",(6,"core","convenor"))
# 	result = cursor.fetchall()
# 	connection.close()
# 	return render_template('table.html',data = result)


#when volunteer in cultural button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/v_cultural/')
def v_cultural():
	connection,cursor=connect()
	# cursor = connection.cursor()
	cursor.execute("select name,usn,position,tele from committee_data where cno = %s and position = %s",(1,"volunteer"))
	result = cursor.fetchall()
	connection.close()
	return render_template('table.html',data = result)



#when volunteer in design button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/v_design/')
def v_design():
	connection,cursor=connect()
	cursor.execute("select name,usn,position from committee_data where cno = %s and position = %s",(2,"volunteer"))
	result = cursor.fetchall()
	connection.close()
	return render_template('table.html',data = result)





#when marketing button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
@app.route('/v_marketing/')
def v_marketing():
	connection,cursor=connect()
	cursor.execute("select name,usn,position from committee_data where cno = %s and position = %s",(5,"volunteer"))
	result = cursor.fetchall()
	connection.close()
	return render_template('table.html',data = result)



#when sponsorship button is pressed;return cultural core and convenor with their ddetails(READ ONLY)
# @app.route('/v_sponsorship/')
# def v_sponsorship():
# 	connection,cursor=connect()
# 	cursor.execute("select name,usn,position from committee_data where cno = %s and position = %s",(6,"volunteer"))
# 	result = cursor.fetchall()
# 	connection.close()
# 	return render_template('table.html',data = result)




@app.route('/firstpage/',methods=['GET','POST'])
def firstpage():
	return render_template('firstpage.html')
	if request.method=='POST':
		if request.form['Go to Committees']:
			return redirect(url_for('committee'))
		if request.form['Go to Championship Table']:
			return redirect(url_for('championship'))
		# if request.form['Go to Cultural Events']:
		# 	return redirect(url_for('view_cultural_table')) 
		else:
			if request.method == 'GET':
				return render_template('firstpage.html')
	
		



@app.route('/champtable/',methods=['GET','POST'])
def champ_table():
	return render_template('view_champtable.html')





@app.route('/championship/',methods=['GET','POST'])
def championship():
	return render_template('championship.html')
	if method.request=='POST':
		if request.form['Girls']:
			return redirect(url_for('girls'))
		if request.form['Boys']:
			return redirect(url_for('boys'))
		# if request.form['Overall']:
		# 	return redirect(url_for('overall')) 
		else:
			if request.method == 'GET':
				return render_template('championship.html')		
	# return render_template('championship.html')		

@app.route('/girls/',methods=['GET','POST'])
def girls():
	connection,cursor=connect()
	cursor.execute("select * from girls")
	result = cursor.fetchall()
	connection.close()
	return render_template('champtable.html',data = result)

@app.route('/boys/',methods=['GET','POST'])
def boys():
	connection,cursor=connect()
	cursor.execute("select * from boys")
	result = cursor.fetchall()
	connection.close()
	return render_template('champtable.html',data = result)







# @app.route('/overall/',methods=['GET','POST'])
# def overall():
# 	connection,cursor=connect()
# 	cursor.execute("select branch from champions_girls join champions_boys where total=max(champions_girls.total+champions_boys.total)")
# 	result = cursor.fetchall()
# 	connection.close()
# 	return render_template('display_winner.html',data = result)


@app.route('/cadd/',methods=['GET','POST'])
def cadd():
	return(redirect(url_for('caddmember')))



@app.route('/caddmember/',methods=['GET','POST'])
def caddmember():
	connection,cursor=connect()
	# print("hello")
	if request.method=='POST':
		inp = request.form
		name = inp['fullname']
		usn = inp['usn']
		branch = inp['branch']
		num = inp['phnum']
		pos = inp['Position']
		cursor.execute("select usn from users where usn=%s",(str(usn),))
		data = cursor.fetchall()
		if data:
			# print(data)
			querry = "insert into committee_data values(%s,%s,%s,%s,%s,%s)"
			cursor.execute(querry,(name,usn,branch,num,pos,1))
			connection.commit()
			connection.close()	
			# print("Member added successfully!")
			return "member added succesfully to cultural committee"
		else:
			return "Sorry usn not a user of techNIEks.Please ask usn to sign up!!"
	return render_template('member_login.html')



@app.route('/dadd/',methods=['GET','POST'])
def dadd():
	return(redirect(url_for('daddmember')))



@app.route('/daddmember/',methods=['GET','POST'])
def daddmember():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		name = inp['fullname']
		usn = inp['usn']
		branch = inp['branch']
		num = inp['phnum']
		pos = inp['Position']
		cursor.execute("select usn from users where usn=%s",(str(usn),))
		data = cursor.fetchall()
		if data:
			# print(data)
			querry = "insert into committee_data values(%s,%s,%s,%s,%s,%s)"
			cursor.execute(querry,(name,usn,branch,num,pos,2))
			connection.commit()
			connection.close()	
			# print("Member added successfully!")
			return "member added succesfully to design committee"
		else:
			return "Sorry usn not a user of techNIEks.Please ask usn to sign up!!"
	return render_template('member_login.html')


@app.route('/madd/',methods=['GET','POST'])
def madd():
	return(redirect(url_for('maddmember')))



@app.route('/maddmember/',methods=['GET','POST'])
def maddmember():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		name = inp['fullname']
		usn = inp['usn']
		branch = inp['branch']
		num = inp['phnum']
		pos = inp['Position']
		cursor.execute("select usn from users where usn=%s",(str(usn),))
		data = cursor.fetchall()
		if data:
			querry = "insert into committee_data values(%s,%s,%s,%s,%s,%s)"
			cursor.execute(querry,(name,usn,branch,num,pos,5))
			connection.commit()
			connection.close()	
			# print("Member added successfully!")
			return "member added succesfully to marketing committee"
		else:
			return "Sorry usn not a user of techNIEks.Please ask usn to sign up!!"
	return render_template('member_login.html')



@app.route('/cdel/',methods=['GET','POST'])
def cdel():
	return(redirect(url_for('cdelmember')))



@app.route('/cdelmember/',methods=['GET','POST'])
def cdelmember():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		usn = inp['usn']
		cursor.execute("select usn from committee_data where (usn=%s and cno = 1)",(str(usn),))
		data = cursor.fetchall()
		if data:
			cursor.execute("delete from committee_data where usn=%s",(str(usn),))
			connection.commit()
			connection.close()
			return "deletion successfull"
		else:
			return "Sorry the usn does not belong to this committee!"
	return render_template('cdel.html')


@app.route('/ddel/',methods=['GET','POST'])
def ddel():
	return(redirect(url_for('ddelmember')))



@app.route('/ddelmember/',methods=['GET','POST'])
def ddelmember():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		usn = inp['usn']
		cursor.execute("select usn from committee_data where (usn=%s and cno = 2)",(str(usn),))
		data = cursor.fetchall()
		if data:
			cursor.execute("delete from committee_data where usn=%s",(str(usn),))
			connection.commit()
			connection.close()
			return "deletion successfull"
		else:
			return "Sorry the usn does not belong to this committee!"
	return render_template('ddel.html')



@app.route('/mdel/',methods=['GET','POST'])
def mdel():
	return(redirect(url_for('mdelmember')))



@app.route('/mdelmember/',methods=['GET','POST'])
def mdelmember():
	connection,cursor=connect()
	if request.method=='POST':
		inp = request.form
		usn = inp['usn']
		cursor.execute("select usn from committee_data where (usn=%s and cno = 5)",(str(usn),))
		data = cursor.fetchall()
		if data:
			cursor.execute("delete from committee_data where usn=%s",(str(usn),))
			connection.commit()
			connection.close()
			return "deletion successfull"
		else:
			return "Sorry the usn does not belong to this committee!"
	return render_template('mdel.html')






#using join in admin committee page
@app.route('/create_usingjoin/',methods=['GET','POST'])
def create_usingjoin():
	connection,cursor=connect()
	cursor.execute("drop view vi")
	cursor.execute('create view vi as select name,usn,position,cname from committee_data c,committee_info d where c.cno=d.cno')
	x = view_event()
	connection.commit()
	connection.close()
	return render_template('jointable.html',data = x)


# view the view created
@app.route('/view_event/')
def view_event():
	connection,cursor=connect()
	cursor.execute("select * from vi")
	data = cursor.fetchall()
	connection.close()
	return data


@app.route('/update/',methods=['GET','POST'])
def update():
	return(redirect(url_for('gupmember')))


@app.route('/gupmember/',methods=['GET','POST'])
def gupmember():
	connection,cursor=connect()
	if request.method=='POST':
		branchname = request.form.get("Branch",None)
		if branchname == None:
			return redirect(url_for('gupmember'))
		# inp = request.form
		# branch = inp['Branch']
		# spo = inp['Sport']
		sponame = request.form.get("Sport",None)
		if sponame == None:
			return redirect(url_for('gupmember'))
		inp = request.form
		poi = inp['points']
		print(poi)
		print(branchname)
		print(sponame)
		cursor.execute("update girls set {} = '{}' where Sports='{}'".format(branchname,poi,sponame))
		connection.commit()
		connection.close()	
		return "Score Board updated succesfully!!!"
	return render_template('updatepage.html')





@app.route('/bupmember/',methods=['GET','POST'])
def bupmember():
	connection,cursor=connect()
	cursor.execute("update ")
	data = cursor.fetchall()
	connection.close()
	return data




# @app.route('/updatefunction/',methods=['GET','POST'])
# def updatefunction():
# 	return "update member"


if __name__ == '__main__':
	app.run(debug=True)