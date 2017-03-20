import requests

r = requests

r.post('https://fcm.googleapis.com/fcm/send',headers={'Content-Type':'application/json',
'Authorization':'key=AAAACvyg6Nk:APA91bG8vwp2p4kQ1cA9OQ-UsIGsz5FK5wR7RPrXTOf0K8i3B_6tlBmEBivqIWOQWf-Su22DYjlj5iJVKU9I4QGbJMTsobHi5cLP3LQVjD9_DWJ7yoEuvyy1amJQBcepghsg5Gq_ttvLl6QTaisxO8455EF0XJjGGw'},
    data='''{ "data": {
    "score": "5x1",
    "time": "15:10"
  },
  "to" : "dhyXK1cr5kY:APA91bFbhpGRr9mXqTnJ1JEHEeKMvlkrH8BQnE_m1oCzz0_zfoNUkSOp1Hj_MjvOgKWfrP_r2a3rJr-R9cFliHDXln4tLkzmH-xAhFuuW3omJCstL0H_PMpk2CJr73TYmAq9V8oE3UaX"
}
''')

