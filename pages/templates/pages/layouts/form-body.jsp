{% load staticfiles %}
{% block content %}
	<link rel='stylesheet' href="{% static 'css/HomePage.css' %}" type='text/css' />
    <link rel="stylesheet" href="{% static 'css/TrackStatus.css' %}" type='text/css'/>
	<title>I T University</title>

	<link rel="stylesheet" href="{% static 'css/HomePage.css' %}" />
	<link rel="stylesheet" href="{% static 'css/TrackStatus.css' %}" />

	</head>
	<body class="verticalLine">

	<div class="Head1">
		<img id="logo" alt="Logo" src="{% static 'images/logo2.png' %}" height="40px" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<h1 class="welcomeH1">Traffic Fines</h1>
	</div>


	<div class="mainContent">
	<hr/>
{% endblock %}