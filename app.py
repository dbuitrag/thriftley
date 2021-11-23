from flask import (Flask, render_template, request, redirect, flash, url_for)
import cs304dbi as dbi
import command
app = Flask(__name__)

# this route displays the search form
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('form.html')  

# this route executes a query
@app.route('/query/')
def query(): 
    print('we are in just query')
    conn = dbi.connect()
    _query = request.args.get('query')
    _kind = request.args.get('kind')
    out = f"query is: {_query}\nkind is: {_kind}" # kind is: {kind}
    print(out)
    if _kind == 'post_id':
        return redirect(url_for('post_detail', post_id_number = _query))
    elif _kind == 'user_id':
        return redirect(url_for('user_detail', user_id_number = _query))
    else:
        return '''<p>Sorry, that query could not be accepted.</p>'''

# this route shows the detail page for a post
@app.route('/pid/<post_id_number>')
def post_detail(post_id_number):
    conn = dbi.connect()
    post = command.get_post(conn, post_id_number)
    if len(post) == 0:
        return '''<p>Sorry, no post with that post id is in our database.</p>'''
    return render_template('postPage.html', posts = post)

# this route shows the detail page for each user
@app.route('/uid/<user_id_number>')
def user_detail(user_id_number):
    conn = dbi.connect()
    user = command.get_user(conn, user_id_number)
    if len(user) == 0:
        return '''<p>Sorry, a user with that id is not in our database.</p>'''
    return render_template('userPage.html', users = user)

@app.before_first_request
def startup():
    dbi.conf('thriftley_db') #CHANGE TO CORRECT DB WHEN UPLOADING

if __name__ == '__main__':
    import os
    uid = os.getuid()
    app.debug = True
    app.run('0.0.0.0',uid)