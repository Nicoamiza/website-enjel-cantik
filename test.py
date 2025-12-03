from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "kunci_rahasia_nico"

# LOGIN PAGE
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']

        if user == "nico" and pw == "123":
            session['user'] = user
            return redirect(url_for('home'))
        else:
            error = "Username atau password salah!"

    return render_template("login.html", error=error)


# HOME PAGE
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("home.html")


# HALAMAN AWAL KENAL
@app.route('/awal')
def awal():
    return render_template("awal.html")


# HALAMAN PERJALANAN
@app.route('/perjalanan')
def perjalanan():
    return render_template("perjalanan.html")


# HALAMAN TENTANG NICO
@app.route('/tentang')
def tentang():
    return render_template("tentang.html")


# LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
