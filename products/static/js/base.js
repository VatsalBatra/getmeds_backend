var module =(function(){
	var el = null;
	var box = null;
	//ADD TO CART FUNCTION
	function add_to_cart(){
			//WHY SIBLINGS ,PREV, NEXT FUNCTION NOT WORKING
		var name = $(this).closest('li').find('p.name').text();
		var rate = $(this).closest('li').find('p.rate').text();
		console.log(rate)

		$.ajax({
			url:'cart/',
			method:'GET',
			data:{
				'name':name,
				'rate':rate
			},
			success:function(content){
				console.log('ok');
			},
			error:function(){
				console.log("ohoh");
			}
		})	
	
		
	

	}
	//REMOVE FROM CART FUNCTION
	function remove_from_cart(){
		var name = $(this).closest('li').find('p.name').text();
		var rate = $(this).closest('li').find('p.rate').text();
		console.log(name)
		console.log(rate)
		$.ajax({
			url:'remove/',
			method:'GET',
			data:{
				'name':name,
				'rate':rate
			},
			success:function(content){
				window.location.href = ' '
			},
			error:function(){
				console.log("ohoh");

			}

		})

	}
	//SEARCH FUNCTION
	function search_function(e){
		box.innerHTML = "";
		
		var searched = search.value;

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
		//SEARCH REQ.
		box = document.getElementById(config['suggestions_box']);
		search = document.getElementById(config['search']);
		$("#search").on('input',search_function);

		//ADD TO CART REQ.
		content = document.getElementsByClassName(config['content'])
		 $('.add_button').click(add_to_cart);
		 //REMOVE FROM CART REQ.
		 $('.remove_button').click(remove_from_cart)


		
	}
	return {
		init:init
	}
}())



