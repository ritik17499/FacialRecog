from flask import Flask, render_template, Response , request
from camera import VideoCamera
import time
import bkc2
import webbrowser
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

a=1
ha=0
sa=0
an=0
ne=0
fe=0
ra=0
def gen(camera):
    global a
    global ha
    global sa
    global an
    global ne
    global fe
    global ra
    while a<50:
        #time.sleep(2.4)
        pred=camera.predi_send()
        if pred=='Happy':
            ha+=1
        elif pred=='Sad':
            sa+=1
        elif pred=='Angry':
            an+=1
        elif pred=='Fear':
            fe+=1
        elif pred=='Neutral':
            ne+=1
        else:
            ra+=1
        a+=1
        print(pred)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +frame+ b'\r\n\r\n')
    return
    """
    List = [-1]
    List.append(ha)
    List.append(sa)
    List.append(an)
    List.append(fe)
    List.append(ne)
    print(ha)
    print(sa)
    print(an)
    print(fe)
    print(ne)
    m=0
    m=max(List)
    n=0
    if ha==m:
        dict=bkc2.list_names('Happy')
        n=len(dict)
        for i in range(0,n):
            print(i+1)
            print(dict[i]['title'])
        return dict
        id=int(input("enter choice "))
        link='http://www.youtube.com'+bkc2.list('Happy',id)
        webbrowser.open(link)  # Go to example.com
    elif sa==m:
            dict=bkc2.list_names('Sad')

            n=len(dict)
            for i in range(0,n):
                print(i+1)
                print(dict[i]['title'])
            return dict
            id=int(input("enter choice "))
            link='http://www.youtube.com'+bkc2.list('Sad',id)
            webbrowser.open(link)
    elif an==m:
            dict=bkc2.list_names('Angry')
            n=len(dict)
            return dict
            for i in range(0,n):
                print(i+1)
                print(dict[i]['title'])
            id=int(input("enter choice "))
            link='http://www.youtube.com'+bkc2.list('Angry',id)
            webbrowser.open(link)
    elif fe==m:
            dict=bkc2.list_names('Fear')
            n=len(dict)
            return dict
            for i in range(0,n):
                print(i+1)
                print(dict[i]['title'])
            id=int(input("enter choice "))
            link='http://www.youtube.com'+bkc2.list('Fear',id)
            webbrowser.open(link)
    else:
        dict=bkc2.list_names('Neutral')
        n=len(dict)
        return dict
        for i in range(0,n):
            print(i+1)
            print(dict[i]['title'])
        id=int(input("enter choice "))
        link='http://www.youtube.com'+bkc2.list('Neutral',id)
        webbrowser.open(link)
    """
List = [-1]
List.append(ha)
List.append(sa)
List.append(an)
List.append(fe)
List.append(ne)
print(ha)
print(sa)
print(an)
print(fe)
print(ne)
m=0
m=max(List)



print(ha)
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


print(ha)
user_list = ['maateen', 'nabin', 'shadd']
my_list = ['https://www.facebook.com', 'google.com', 'twitter.com']

@app.route('/users/')
def users():
    name_list=[]
    link_list=[]
    n=0;
    if(ha==m):
        dict=bkc2.list_names('Happy')
        n=len(dict)
        for i in range(0,n):
            link_list.append('https://www.youtube.com'+dict[i]['url_suffix'])
            name_list.append(dict[i]['title'])

    elif(sa==m):

        dict=bkc2.list_names('Sad')
        n=len(dict)
        for i in range(0,n):
            link_list.append('https://www.youtube.com'+dict[i]['url_suffix'])
            name_list.append(dict[i]['title'])

    elif(an==m):
        dict=bkc2.list_names('Angry')
        n=len(dict)
        for i in range(0,n):
            link_list.append('https://www.youtube.com'+dict[i]['url_suffix'])
            name_list.append(dict[i]['title'])

    elif(fe==m):
        dict=bkc2.list_names('Fear')
        n=len(dict)
        for i in range(0,n):
            link_list.append('https://www.youtube.com'+dict[i]['url_suffix'])
            name_list.append(dict[i]['title'])

    else:
        dict=bkc2.list_names('Neutral')
        n=len(dict)
        for i in range(0,n):
            link_list.append('https://www.youtube.com'+dict[i]['url_suffix'])
            name_list.append(dict[i]['title'])



    return render_template('users.html', users=name_list ,link=link_list,len=n)



"""
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       result=gen()
       #result = request.form
       #print(result)
       return result
      #return render_template("result.html",result = result)
"""


if __name__ == '__main__':
    app.run( use_reloader=True,debug=True)
