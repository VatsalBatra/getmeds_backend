var module =(function(){
	var el = null;
	var box = null;
	
	function change_it(){
		
		console.log($(this).siblings('div.content').value);
		console.log("uouououou")
		
		
	

	}
	function search_function(e){
		box.innerHTML = "";
		
		var searched = search.value;
		console.log(searched);
		if(searched === ''){
			return
		}
		$.ajax({
			url: 'search/',
			method:'GET',
			data :{
				'searched':searched,
			},
			success:function(context){
				var list = context.output;
				for( var i = 0;i<list.length;i++){
					$(box).append( '<p>' + list[i] + '</p>');
				}

			},
			error:function(){
				console.log("blunder")
			}
		})



	}
	function init(config){
		box = document.getElementById(config['search_box']);
		search = document.getElementById(config['search']);
		$("#search").on('input',search_function);
	}
	return {
		init:init
	}
}())



