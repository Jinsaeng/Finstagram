#View visible photos:: Finstagram shows the user the photoID and photoPoster of each
#photo that is visible to her, arranged in reverse chronological order.

@app.route('/show_photos')
def show_photos();
    user = ['username']
    cursor = conn.cursor()
    query = 'SEELCT ID, username FROM Photo JOIN Person USING (username) WHERE AllFollowers IN %s AND followStatus = TRUE ORDER BY DESC'
    cursor.execute(query, user)
    photos = cursor.fetchall()
    cursor.close()
    return render_template('photos.html', username = user, posts = photos)
