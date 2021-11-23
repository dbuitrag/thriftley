import cs304dbi as dbi

def get_post(conn, post_id_number):
    '''returns the detail page of a post with a particular id number'''
    curs = dbi.dict_cursor(conn)
    tmpl = 'select * from post where post_id = %s;'
    val = post_id_number
    curs.execute(tmpl, val)
    out = curs.fetchall()
    return out

def get_user(conn, user_id_number):
    '''returns the detail page of a user with a particular id number'''
    curs = dbi.dict_cursor(conn)
    tmpl = 'select * from user where uid = %s'
    val = user_id_number
    curs.execute(tmpl, val)
    out = curs.fetchall()
    return out


if __name__ == '__main__':
    dbi.cache_cnf()   # defaults to ~/.my.cnf
    dbi.use('thriftley_db')    # CHANGE TO CORRECT DB
    conn = dbi.connect()