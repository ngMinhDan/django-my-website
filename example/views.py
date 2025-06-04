# example/views.py
from datetime import datetime
from pytz import timezone

from django.http import HttpResponse

def index(request):
    now = datetime.now(timezone('Asia/Ho_Chi_Minh'))
    html = f'''
    <html>
        <body>
            <h1>Hello world ! </h1>
            <h2> About Me</h2>
            <ul>
                <li> Name: Nguyen Minh Dan </li>
                <li> Age: 26 </li>
                <li> Gender: Male </li>
            </ul>
            <h2> I did not done anything i thought this is good so i dont show for you </h2>
            <p>The current time in Ho Chi Minh is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)