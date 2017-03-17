$(document).ready(function(){
	console.log("Document ready");
	$("#tweet").on("submit", function(event)) {
		event.preventDefault();
		data = $("#tweet").serialize();
		$.ajax({
			method:"POST",
			url: "/tweet",
			data: data,
			success: function(response) {
				console.log(response);
			}
		});
	});
});

// form = html tag id
// url = html action