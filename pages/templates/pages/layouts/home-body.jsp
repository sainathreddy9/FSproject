{% load staticfiles %}
        <link rel='stylesheet' href="{% static 'css/HomePage.css' %}" type='text/css' />
        <link rel="stylesheet" href="{% static 'css/TrackStatus.css' %}" type='text/css'/>
        <hr/>
        <div class="Head1" style="height:30">
		    <h1 class="welcomeH1">Traffic Fines</h1>
	    </div>

        <div class="mainContent">
            <hr/>

            <div class="slideShow">
                <img src="{% static 'images/1.jpg' %}" width="700" height="300" id="slide" />
            </div>

            <div class="bodyHere"><hr/>
                <h3>Welcome to ITU:</h3>
                <p>&emsp;&emsp;&emsp;&emsp;&emsp;.</p><hr/>

                <h3>Campus Life: </h3>
                <img alt="campus life" src="{% static 'images/life.jpg' %}"><br/><br/>
                <hr/>

            </div>
            <br />
        </div>