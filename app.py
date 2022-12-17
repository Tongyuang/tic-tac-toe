from flask import Flask,url_for,request,render_template

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
@app.route("/game",methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        # request.
        user1 = request.form["name1"]
        user2 = request.form["name2"]
        mode = request.form["radio"]
        if mode == "pvb":
            return render_template("pvbgame.html",username1=user1)
        if mode == "pvp":
            return render_template("pvpgame.html",username1=user1,username2=user2)
        
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True, port=8080)
    