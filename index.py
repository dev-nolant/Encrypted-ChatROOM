import sys
ver = sys.version_info.major
if ver == 3:
    from flask import Flask, request, render_template
    def ivk():
        try:
            key_check = open('tempkey.txt', 'w').read()
            print(key_check)
        except:
            return 'KEY FILE NOT GENERATED - GET IN CONTACT WITH KEY GIVER'
    def UID(UID_USER,UID_PASS):
        try:
            foo = open(UID_USER, 'r').read()
            uid_p = UID_PASS
            #decrypt uisng UID PASS
            temp_key = lambda x: uid_p / x 
            return (temp_key(1))
        except:
            return 'INVALID KEY'
    app = Flask(__name__)
    @app.route(('/'), methods=['GET'])
    def result(): # should display 'bar'
        try:
            reason = request.args.get('reason')
            if 'register' in reason:
                return 'INVALID REQUEST MADE = ?reg=+invite_key' #gives warning upon wrong request
            else:
                return ' ' # response to your request.'
        except:
            return "curl: (6) Could not resolve host "
    @app.route(('/'), methods=['POST'])
    def register():
        try:
            reg = request.args.get('reg')
            if ivk() in reg:
                return 'ok'
            else:
                return ivk()
        except:
            return "curl: (7) Could not resolve host "
    @app.route(('/keygen'), methods=['POST'])
    def keygenerator():
        uid = request.args.get('UID')
        if ":" in uid:
            fid = uid.split(':')
            uid_user = fid[0]
            uid_pass = fid[1]
            fidl = int(fid[0]) / int(fid[1])
            UID(str(uid_user), str(uid_pass))
            return 'ok'
            #if fidl in UID(fid[0],fid[1]):
            #    return 'ok'
            #else:
            #    return ivk()
        else:
            return "INVALID INPUT"
        

    @app.route('/')
    def main():
        return render_template('home.html')
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
else:
    print("Invalid PYTHON Version: "+str(ver)+" - Please upgrade to version 3+")