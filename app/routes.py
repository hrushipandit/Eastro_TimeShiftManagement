from flask import Flask, render_template, url_for, flash, redirect,request
from app.models import einfo,TimeShift,P_Info
from app.forms import SignupForm, LoginForm,UpdateForm,AdminAssignForm,NewProjectForm,ReportAssignForm,ReportNonAssignForm,DateForm
from app import app,db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required
global date
date=1

def __repr__(self):
    return f"User('{self.username}' , '{self.email}')"


logo="static/images/logo.png"

@app.route("/",methods=['GET', 'POST'])
@app.route("/login",methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and current_user.admin==1:
        return redirect(url_for('admin_page'))
    elif current_user.is_authenticated and current_user.admin==0:
            return redirect(url_for('user_page'))

    form = LoginForm()
    if form.validate_on_submit():
        user=einfo.query.filter_by(email=form.email.data,visibility=True).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            if user.admin:
                login_user(user)
                next_page= request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('admin_page'))
            else:
                login_user(user)
                next_page= request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('user_page'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('new_login.html',logo=logo,form=form)

@app.route("/admin",methods=['GET', 'POST'])
def admin():
    return render_template('layout_admin_page.html',logo=logo)


@app.route("/signup",methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if len(einfo.query.all())==0:
            employee=einfo(E_Name=form.fullname.data,email=form.email.data,password=hashed_password,admin=1,visibility=True)
        else:
            employee=einfo(E_Name=form.fullname.data,email=form.email.data,password=hashed_password,admin=0,visibility=True)
        db.session.add(employee)
        db.session.commit()
        flash(f'Account created for {form.fullname.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html',logo=logo, form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/admin_page",methods=['GET', 'POST'])
@login_required
def admin_page():
    if current_user.admin:
        form=SignupForm()
        return render_template('admin_page.html',logo=logo, form=form)
    else:
        logout_user()
        return redirect(url_for('login'))


@app.route("/admin_page_project",methods=['GET', 'POST'])
@login_required
def admin_page_project():
    if current_user.admin:
        form=AdminAssignForm()
        list1=P_Info.query.filter_by(visibility=True).all()
        list=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method == 'POST':
            pnames = request.form.get('pnames')
            field=request.form.get('field')
            enames=request.form.get('enames')
            if pnames and enames:
                P_id=P_Info.query.filter_by(P_Name=pnames).first()
                E_id=einfo.query.filter_by(E_Name=enames).first()
                if P_id:
                    P_id=P_Info.query.filter_by(P_Name=pnames).first().P_id
                if E_id:
                    E_id=einfo.query.filter_by(E_Name=enames).first().id
                timeshift=TimeShift(id=E_id,Field=field,P_id=P_id,Verified=False)
                db.session.add(timeshift)
                db.session.commit()
        return render_template('admin_page_project.html',logo=logo, form=form,list=list,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_HR",methods=['GET', 'POST'])
@login_required
def admin_page_HR():
    if current_user.admin:
        form=AdminAssignForm()
        list1=P_Info.query.filter_by(visibility=True).all()
        list=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method == 'POST':
            pnames = request.form.get('pnames')
            field=request.form.get('field')
            enames=request.form.get('enames')
            if pnames and enames:
                P_id=P_Info.query.filter_by(P_Name=pnames,visibility=True).first()
                E_id=einfo.query.filter_by(E_Name=enames).first()
                if P_id:
                    P_id=P_Info.query.filter_by(P_Name=pnames).first().P_id
                if E_id:
                    E_id=einfo.query.filter_by(E_Name=enames).first().id
                timeshift=TimeShift(id=E_id,Field=field,P_id=P_id,Verified=False)
                db.session.add(timeshift)
                db.session.commit()
        return render_template('admin_page_HR.html',logo=logo, form=form,list=list,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_PS",methods=['GET', 'POST'])
@login_required
def admin_page_PS():
    if current_user.admin:
        form=AdminAssignForm()
        list1=P_Info.query.filter_by(visibility=True).all()
        list=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method == 'POST':
            pnames = request.form.get('pnames')
            field=request.form.get('field')
            enames=request.form.get('enames')
            if pnames and enames:
                P_id=P_Info.query.filter_by(P_Name=pnames).first()
                E_id=einfo.query.filter_by(E_Name=enames).first()
                if P_id:
                    P_id=P_Info.query.filter_by(P_Name=pnames).first().P_id
                if E_id:
                    E_id=einfo.query.filter_by(E_Name=enames).first().id
                timeshift=TimeShift(id=E_id,Field=field,P_id=P_id,Verified=False)
                db.session.add(timeshift)
                db.session.commit()
        return render_template('admin_page_PS.html',logo=logo, form=form,list=list,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_SM",methods=['GET', 'POST'])
@login_required
def admin_page_SM():
    if current_user.admin:
        form=AdminAssignForm()
        list1=P_Info.query.filter_by(visibility=True).all()
        list=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method == 'POST':
            pnames = request.form.get('pnames')
            field=request.form.get('field')
            enames=request.form.get('enames')
            if pnames and enames:
                P_id=P_Info.query.filter_by(P_Name=pnames).first()
                E_id=einfo.query.filter_by(E_Name=enames).first()
                if P_id:
                    P_id=P_Info.query.filter_by(P_Name=pnames).first().P_id
                if E_id:
                    E_id=einfo.query.filter_by(E_Name=enames).first().id
                timeshift=TimeShift(id=E_id,Field=field,P_id=P_id,Verified=False)
                db.session.add(timeshift)
                db.session.commit()
                return redirect(url_for('admin_page_SM'))
        return render_template('admin_page_SM.html',logo=logo, form=form,list=list,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_AC",methods=['GET', 'POST'])
@login_required
def admin_page_AC():
    if current_user.admin:
        form=AdminAssignForm()
        list1=P_Info.query.filter_by(visibility=True).all()
        list=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method == 'POST':
            pnames = request.form.get('pnames')
            field=request.form.get('field')
            enames=request.form.get('enames')
            if pnames and enames:
                P_id=P_Info.query.filter_by(P_Name=pnames).first()
                E_id=einfo.query.filter_by(E_Name=enames).first()
                if P_id:
                    P_id=P_Info.query.filter_by(P_Name=pnames).first().P_id
                if E_id:
                    E_id=einfo.query.filter_by(E_Name=enames).first().id
                timeshift=TimeShift(id=E_id,Field=field,P_id=P_id,Verified=False)
                db.session.add(timeshift)
                db.session.commit()
            return redirect(url_for('admin_page_AC'))
        return render_template('admin_page_AC.html',logo=logo, form=form,list=list,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_PL",methods=['GET', 'POST'])
@login_required
def admin_page_PL():
    if current_user.admin:
        listp=P_Info.query.filter_by(visibility=True).all()
        return render_template('admin_page_PL.html',logo=logo,listp=listp)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_PT",methods=['GET', 'POST'])
@login_required
def admin_page_PT():
    if current_user.admin:
        list1=P_Info.query.filter_by(visibility=True).all()
        if request.method == 'POST':
            pnames = request.form.get('pnames')
            pid=P_Info.query.filter_by(P_Name=pnames).first().P_id
            list2=TimeShift.query.filter_by(P_id=pid,Verified=True).all()
            elist=[]
            for item in list2:
                elist.append(einfo.query.filter_by(id=item.id).first())

            return render_template('admin_page_PT.html',logo=logo,list1=list1,list2=list2,elist=elist)
        return render_template('admin_page_PT.html',logo=logo,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_other",methods=['GET', 'POST'])
@login_required
def admin_page_other():
    if current_user.admin:
        form=AdminAssignForm()
        list1=P_Info.query.filter_by(visibility=True).all()
        list=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method == 'POST':
            pnames = request.form.get('pnames')
            field=request.form.get('field')
            enames=request.form.get('enames')
            if pnames and enames:
                P_id=P_Info.query.filter_by(P_Name=pnames,visibility=True).first()
                E_id=einfo.query.filter_by(E_Name=enames).first()
                if P_id:
                    P_id=P_Info.query.filter_by(P_Name=pnames).first().P_id
                if E_id:
                    E_id=einfo.query.filter_by(E_Name=enames).first().id
                timeshift=TimeShift(id=E_id,Field=field,P_id=P_id,Verified=False)
                db.session.add(timeshift)
                db.session.commit()
        return render_template('admin_page_other.html',logo=logo, form=form,list=list,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_pending",methods=['GET', 'POST'])
@login_required
def admin_page_pending():
    if current_user.admin:
        list2=TimeShift.query.filter_by(Verified=False).all()
        elist=[]
        plist=[]
        for item in list2:
            elist.append(einfo.query.filter_by(id=item.id).first())
            plist.append(P_Info.query.filter_by(P_id=item.P_id).first())
        if request.method=="POST":
            tid=request.form['tid']
            timeshift=TimeShift.query.filter_by(T_id=tid,Verified=0).first()
            db.session.delete(timeshift)
            db.session.commit()
            return redirect(url_for('admin_page_pending'))
        return render_template('admin_page_pending.html',logo=logo,list2=list2,elist=elist,plist=plist)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_EL",methods=['GET', 'POST'])
@login_required
def admin_page_EL():
    if current_user.admin:
        liste=einfo.query.filter_by(admin=0,visibility=True).all()
        return render_template('admin_page_EL.html',logo=logo,liste=liste)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_password_reset",methods=['GET', 'POST'])
@login_required
def admin_page_password_reset():
    if current_user.admin:
        liste=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method=="POST":
            password=request.form.get('password')
            hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
            id=request.form.get('id')
            ename=einfo.query.filter_by(id=id).first()
            print(ename.E_Name)
            ename.password=hashed_password
            db.session.commit()
            return redirect(url_for('admin_page_password_reset'))
        return render_template('admin_page_password_reset.html',logo=logo,liste=liste)
    else:
        logout_user()
        return redirect(url_for('login'))


@app.route("/admin_page_ET",methods=['GET', 'POST'])
@login_required
def admin_page_ET():
    form=DateForm()
    if current_user.admin:
        list1=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method == 'POST':
            enames = request.form.get('enames')
            date=form.date.data
            if date:
                date_str = date.strftime('%d-%m-%y')
                eid=einfo.query.filter_by(E_Name=enames).first().id
                list2=TimeShift.query.filter_by(id=eid,Date=date_str,Verified=True).all()
                plist=[]
                for item in list2:
                    plist.append(P_Info.query.filter_by(P_id=item.P_id).first())
            return render_template('admin_page_ET.html',logo=logo,list1=list1,list2=list2,plist=plist,form=form)
        return render_template('admin_page_ET.html',logo=logo,list1=list1,form=form)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_Tdate",methods=['GET', 'POST'])
@login_required
def admin_page_Tdate():
    form=DateForm()
    if current_user.admin:
        if request.method == 'POST':
            date=form.date.data
            if date:
                date_str = date.strftime('%d-%m-%y')
                list2=TimeShift.query.filter_by(Date=date_str,Verified=True).all()
                elist=[]
                plist=[]
                for item in list2:
                    elist.append(einfo.query.filter_by(id=item.id).first())
                    plist.append(P_Info.query.filter_by(P_id=item.P_id).first())
            return render_template('admin_page_Tdate.html',logo=logo,list2=list2,form=form,elist=elist,plist=plist)
        return render_template('admin_page_Tdate.html',logo=logo,form=form)
    else:
        logout_user()
        return redirect(url_for('login'))


@app.route("/admin_page_TDelete",methods=['GET', 'POST'])
@login_required
def admin_page_TDelete():
    form=DateForm()
    if current_user.admin:
        if request.method=='GET':
            global date
            if date!=1:
                date_str = date.strftime('%d-%m-%y')
                list2=TimeShift.query.filter_by(Date=date_str,Verified=True).all()
                elist=[]
                plist=[]
                for item in list2:
                    elist.append(einfo.query.filter_by(id=item.id).first())
                    plist.append(P_Info.query.filter_by(P_id=item.P_id).first())
                return render_template('admin_page_TDelete.html',logo=logo,list2=list2,form=form,elist=elist,plist=plist)

        if request.method == 'POST':
            search = request.form.get('action')
            if search=='search':
                date=form.date.data
                date_str = date.strftime('%d-%m-%y')
                list2=TimeShift.query.filter_by(Date=date_str,Verified=True).all()
                elist=[]
                plist=[]
                for item in list2:
                    elist.append(einfo.query.filter_by(id=item.id).first())
                    plist.append(P_Info.query.filter_by(P_id=item.P_id).first())
                return render_template('admin_page_TDelete.html',logo=logo,list2=list2,form=form,elist=elist,plist=plist)
            else:
                tid=request.form['tid']
                timeshift=TimeShift.query.filter_by(T_id=tid).first()
                db.session.delete(timeshift)
                db.session.commit()
                return redirect(url_for('admin_page_TDelete'))

        return render_template('admin_page_TDelete.html',logo=logo,form=form)
    else:
        logout_user()
        return redirect(url_for('login'))


@app.route("/admin_page_add_project",methods=['GET', 'POST'])
def admin_page_add_project():
    form=NewProjectForm()
    if current_user.admin:
        if form.validate_on_submit():
                pid_form=form.P_id.data
                list1=P_Info.query.all()
                list2=[]
                for item in list1:
                    list2.append(item.P_id)
                if pid_form in list2:
                    flash('Pid already taken','danger')
                else:
                    project=P_Info(P_id=form.P_id.data,P_Name=form.P_Name.data,visibility=True)
                    db.session.add(project)
                    db.session.commit()
                return redirect(url_for('admin_page_add_project'))

    return render_template('admin_page_add_project.html',logo=logo, form=form)

@app.route("/admin_page_delete_project",methods=['GET', 'POST'])
@login_required
def admin_page_delete_project():
    if current_user.admin:
        list1=P_Info.query.filter_by(visibility=True).all()
        if request.method=='POST':
            pnames = request.form.get('pnames')
            if pnames:
                pinfo=P_Info.query.filter_by(P_Name=pnames,visibility=True).first()
                pinfo.visibility=False
                db.session.commit()
            return redirect(url_for('admin_page_delete_project'))
        return render_template('admin_page_delete_project.html',logo=logo,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_restore_project",methods=['GET', 'POST'])
@login_required
def admin_page_restore_project():
    if current_user.admin:
        list1=P_Info.query.filter_by(visibility=False).all()
        if request.method=='POST':
            pnames = request.form.get('pnames')
            if pnames:
                pinfo=P_Info.query.filter_by(P_Name=pnames,visibility=False).first()
                pinfo.visibility=True
                db.session.commit()
            return redirect(url_for('admin_page_restore_project'))
        return render_template('admin_page_restore_project.html',logo=logo,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))


@app.route("/admin_page_delete_employee",methods=['GET', 'POST'])
@login_required
def admin_page_delete_employee():
    if current_user.admin:
        list1=einfo.query.filter_by(admin=0,visibility=True).all()
        if request.method=='POST':
            enames = request.form.get('ename')
            if enames:
                einfoentry=einfo.query.filter_by(E_Name=enames,visibility=True).first()
                einfoentry.visibility=False
                db.session.commit()
            return redirect(url_for('admin_page_delete_employee'))
        return render_template('admin_page_delete_employee.html',logo=logo,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/admin_page_restore_employee",methods=['GET', 'POST'])
@login_required
def admin_page_restore_employee():
    if current_user.admin:
        list1=einfo.query.filter_by(admin=0,visibility=False).all()
        if request.method=='POST':
            enames = request.form.get('ename')
            if enames:
                einfoentry=einfo.query.filter_by(E_Name=enames,visibility=False).first()
                einfoentry.visibility=True
                db.session.commit()
            return redirect(url_for('admin_page_restore_employee'))
        return render_template('admin_page_restore_employee.html',logo=logo,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))



@app.route("/user_page",methods=['GET', 'POST'])
@login_required
def user_page():
    if current_user.admin==0:
        return render_template('user_page.html',logo=logo)
    else:
        logout_user()
        return redirect(url_for('login'))
@app.route("/user_page_info",methods=['GET', 'POST'])
@login_required
def user_page_info():
    if current_user.admin==0:
        return render_template('user_page_info.html',logo=logo)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/user_page_update_info",methods=['GET', 'POST'])
@login_required
def user_page_update_info():
    if current_user.admin==0:
        form=UpdateForm()
        if form.validate_on_submit():
            current_user.E_Name=form.fullname.data
            current_user.email=form.email.data
            db.session.commit()
            return redirect(url_for('user_page_info'))
        elif request.method=='GET':
            form.email.data=current_user.email
            form.fullname.data=current_user.E_Name
        return render_template('user_page_update_info.html',logo=logo, form=form)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/user_page_RA",methods=['GET', 'POST'])
@login_required
def user_page_RA():
    if current_user.admin==0:
        liste=TimeShift.query.filter_by(id=current_user.id,Verified=False).all()
        listp_name=[]
        for items in liste:
            listp_name.append(P_Info.query.filter_by(P_id=items.P_id).first())
        form=ReportAssignForm()
        if request.method == 'POST':
            print('After Post')
            name=request.form['index']
            field=request.form['index1']
            tid=request.form['tid']
            date=form.date.data
            date_str = date.strftime('%d-%m-%y')
            head=form.Head.data
            house=form.House.data
            time_form=form.Time.data
            Description=form.Description.data
            time = TimeShift.query.filter_by(T_id=tid).first()
            time.Date=date_str
            time.Head=head
            time.House=house
            time.Time=time_form
            time.Description=Description
            time.Verified=True
            db.session.commit()
            return redirect(url_for('user_page_RA'))
        return render_template('user_page_RA.html',logo=logo, form=form,liste=liste,listp_name=listp_name)
    else:
        logout_user()
        return redirect(url_for('login'))

@app.route("/user_page_RNA",methods=['GET', 'POST'])
@login_required
def user_page_RNA():
    form=ReportNonAssignForm()
    if current_user.admin==0:
        list1=P_Info.query.filter_by(visibility=True).all()

        if form.validate_on_submit():
            pnames = request.form.get('pnames')
            P_id=P_Info.query.filter_by(P_Name=pnames).first()
            date=form.date.data
            date_str = date.strftime('%d-%m-%y')
            head=form.Head.data
            house=form.House.data
            time_form=form.Time.data
            Description=form.Description.data
            Field=form.Field.data
            timeshift=TimeShift(id=current_user.id,P_id=P_id.P_id,Date=date_str,Head=head,House=house,Time=time_form,Description=Description,Field=Field,Verified=True)
            db.session.add(timeshift)
            db.session.commit()

            return redirect(url_for('user_page_RNA'))

        return render_template('user_page_RNA.html',logo=logo, form=form,list1=list1)
    else:
        logout_user()
        return redirect(url_for('login'))


@app.route("/user_page_TS",methods=['GET', 'POST'])
@login_required
def user_page_TS():
    form=DateForm()
    if current_user.admin==0:
        if request.method=="POST":
            date=form.date.data
            if date:
                date_str = date.strftime('%d-%m-%y')
                liste=TimeShift.query.filter_by(Date=date_str,Verified=True).all()
                listp_name=[]
                for item in liste:
                    listp_name.append(P_Info.query.filter_by(P_id=item.P_id).first())
            return render_template('user_page_TS.html',logo=logo,liste=liste,listp_name=listp_name,form=form)
        return render_template('user_page_TS.html',logo=logo,form=form)
    else:
        logout_user()
        return redirect(url_for('login'))
