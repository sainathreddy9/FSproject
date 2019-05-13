
        {% load staticfiles %}
        <link rel='stylesheet' href="{% static 'css/HomePage.css' %}" type='text/css' />
        <link rel="stylesheet" href="{% static 'css/TrackStatus.css' %}" type='text/css'/>
        <hr/>
		<div class="Head1" style="height:30">
		    <h1 class="welcomeH1">iTechnological University</h1>
	    </div>

        <div class="mainContent">
            <hr/>

            <div class="slideShow">
                <img src="{% static 'images/1.jpg' %}" width="700" height="300" id="slide" />
            </div>

            <div class="bodyHere"><hr/>
                <h3>Welcome to ITU:</h3>
                <p>&emsp;&emsp;&emsp;&emsp;&emsp;Welcome to Police fines </p><hr/>

                <h3>Campus Life: </h3>
                <img alt="campus life" src="{% static 'images/life.jpg' %}"><br/><br/>
                <hr/>

            </div>
            <br />
            <br />
        </div>

        <div class="footMain">
		<div class="leftMenu">
			<h3 style="border-bottom: 1px dotted white;">About ITU</h3>
			<ul>
				<li><a class="finalAnchor" href="home">History</a><br />
				<br /></li>
				<li><a class="finalAnchor" href="home">Affiliated Colleges</a><br />
				<br /></li>
				<li><a class="finalAnchor" href="home">Syllabus</a><br />
				<br /></li>
			</ul>
		</div>

		<div class="middleMenu" class="bottomMenu">
			<h3 style="border-bottom: 1px dotted white;">Admissions</h3>
			<ul>
				<li><a class="finalAnchor" href="home">Eligibility</a><br />
				<br /></li>
				<li><a class="finalAnchor" href="home">Fee Structure</a><br />
				<br /></li>
				<li><a class="finalAnchor" href="home">Courses Offered</a><br />
				<br /></li>
			</ul>
		</div>

		<div class="rightMenu" class="bottomMenu">
			<h3 style="border-bottom: 1px dotted white;">Contact Us</h3>
			<ul>
				<li><a class="finalAnchor" href="contact.htm#contact">Contact Number</a><br />
				<br /></li>
				<li><a class="finalAnchor" href="contact.htm#routeMap">Route Map</a><br />
				<br /></li>
				<li><a class="finalAnchor" href="contact.htm#address">Address</a><br />
				<br /></li>
			</ul>
		</div>



		<div class="footSub">
			<div class="lastMenu">
				<p class="inlineClass">Powered By:</p>
				<p class="inlineClass" style="color: orange; padding-right: 100px;">DJango</p>
				<p class="inlineClass" style="padding-right: 100px;">©2014: All
					Rights Reserved</p>
				<a href="#" class="head1">Page Top</a>| <a href="#" class="head1">Feed
					Back</a>| <a href="#" class="head1">Contact Us</a>
			</div>
		</div>
	</div>
