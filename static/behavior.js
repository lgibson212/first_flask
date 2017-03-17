$(document).ready(function(){
	console.log("Document ready");
	$("button").on("submit", function(click)) {
		event.preventDefault();
		$.ajax({
			method:"POST",
			url: "/check-credentials-login",
			data: data,
			success: function(response) {
				console.log(response);
			}
		});
	});
});
