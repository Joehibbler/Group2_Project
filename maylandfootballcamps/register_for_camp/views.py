from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required
from maylandfootballcamps import db
from maylandfootballcamps.models import RegisterForCamp
from maylandfootballcamps.register_for_camp.forms import BlogPostForm

blog_posts = Blueprint('register_for_camp',__name__)

@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def register_for_camp():
    form = RegisterForCampForm()

    if form.validate_on_submit():

        register_for_camp = RegisterForCamp(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id
                             )
        db.session.add(register_for_camp)
        db.session.commit()
        flash("Successfully Registered for Camp")
        return redirect(url_for('core.index'))

    return render_template('register_for_camp.html',form=form)


# int: makes sure that the blog_post_id gets passed as in integer
# instead of a string so we can look it up later.
@blog_posts.route('/<int:register_for_camp_id>')
def register_for_camp(register_for_camp_id):
    # grab the requested blog post by id number or return 404
    register_for_camp = RegisterForCamp.query.get_or_404(register_for_camp_id)
    return render_template('register_for_camp.html',title=register_for_camp.title,
                            date=register_for_camp.date,post=register_for_camp
    )
