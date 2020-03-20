 <!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</head>
<style>
body{
	padding: 20px;
	marging: 20px;
}
h4{
	margin: 0px;
	padding-bottom: 10px;
}
img {
	display: block;
	margin: auto;
}
h1 {
text-align: center;
	}
p.spec{
	margin: 10px, 0, 10px;
}
ul.author{
	font-size: 14px;
	margin: 0px, 0px, 0px, 0px;
	list-style-type: none;
	padding: 0px;
}
ul.obj
ul.bio{
	list-style-type: square;
}
.breadcrumb{
		width: 412px; 
	}
#main{
	margin: 0;
	padding: 30px, 0, 10px, 0;
}
.footer{
	text-align: center
}
</style>
<script>
	
</script>
<body>

<div class="d-flex flex-column">

<div class="p-2">
<img src="https://d2z6c3c3r6k4bx.cloudfront.net/uploads/event/logo/1061432/a991d937097e8176adf1ea7196beb80f.png">
<hr>
<h1>Backdoor Project</h1>
<hr>
<p>
This project consist in create a bind between two machines and take total control like a shadow. This program shows a connection Client / Server into a Network Enterprise. In any Network connection only needs an input door to scale until to get relevant information. However, a Backdoor can create multiple connections and it can take possession of assets more important of an enterprise and so the attacker can go and go out anytime.
</p>
<p>
But in this project, the connection will be only one to one (client / server) with a tcp protocol and introduces malware to get credentials.
</p>
<h2 class="obj">Objetive</h2>
<hr>
<ul>
<li>Take total cotrol of machine</li>
<li>Persisten on Reboot</li>
</ul>
</div>

<div id="main" class="p-2">
<h3>Specifer</h3>
<hr>
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item active" aria-current="page">Commands Shell</li>
  </ol>
</nav>

<div class="row">
  <div class="col-4">
    <div class="list-group" id="list-tab" role="tablist">
      <a class="list-group-item list-group-item-action active" id="list-home-list" data-toggle="list" href="#list-home" role="tab" aria-controls="home">cd</a>
      <a class="list-group-item list-group-item-action" id="list-profile-list" data-toggle="list" href="#list-profile" role="tab" aria-controls="profile">curr</a>
      <a class="list-group-item list-group-item-action" id="list-messages-list" data-toggle="list" href="#list-messages" role="tab" aria-controls="messages">run</a>
      <a class="list-group-item list-group-item-action" id="list-settings-list" data-toggle="list" href="#list-settings" role="tab" aria-controls="settings">upload</a>
      <a class="list-group-item list-group-item-action" id="list-settings-list" data-toggle="list" href="#list-settings" role="tab" aria-controls="settings">download</a>
      <a class="list-group-item list-group-item-action" id="list-settings-list" data-toggle="list" href="#list-settings" role="tab" aria-controls="settings">exit</a>
    </div>
  </div>
  <div class="col-8">
    <div class="tab-content" id="nav-tabContent">
      <div class="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list">Get current directory</div>
      <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">Current directory</div>
      <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">Execute a program</div>
      <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">Upload a File to Client</div>
      <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">Downlod a File to Server</div>
      <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">Finish shell</div>
    </div>
  </div>
</div>
<p class="spec">
* And basic commands of Linux and Windows terminal
</p>
</div>

<div class="p-2">
<h4 id="con">Contributors</h4>
<hr>
<ul class="author" >
<li>Giovanny Ortegon - 934@holbertonschool.com</li>
<li>Joseph Delgadillo</li>
</ul>
<h4>Bibligraphy</h4>
<hr>
<ul class="bio">
<li>Master Ethical Hacking with Python - Joseph Delgadillo</li>
<li>Hands-on Network programming with C - Lewis Van Winkle</li>
<li>Penetration testing with Shellcode - Hamza Megahed</li>
<li>Pentester Academy - Vivek Ramachandran</li>
</div>

<div class="p-2 footer">
<hr>
Copyright &copy;2020 - Giovanny Ortegon - twitter <a href="https://twitter.com/__sklgio__">@__sklgio__</a>
</div>
</div>
</body>
</html> 
