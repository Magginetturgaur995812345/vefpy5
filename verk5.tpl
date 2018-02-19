<!DOCTYPE html>
<html>
<head>
	<title>Verk5</title>
</head>
<body>
	%for i in data["results"]:
		<h2>{{i["eventDateName"]}}</h2>
		<img src="{{i['imageSource']}}">
		<h2>{{i["eventHallName"]}}</h2>
		<h2>{{i["dateOfShow"]}}</h2>
		<br>
	%end
</body>
</html>