var module =(function(){
	var el = null;
	var box = null;
	var error_box = null;
	//ADD TO CART FUNCTION
	function add_to_cart(){
			//WHY SIBLINGS ,PREV, NEXT FUNCTION NOT WORKING ?????????????/
		var name = $(this).closest('li').find('p.name').text();
		var rate = $(this).closest('li').find('p.rate').text();
		var quantity = $(this).closest('li').find("select option:selected").val();
		console.log(quantity)

		$.ajax({
			url:'cart/',
			method:'GET',
			data:{
				'name':name,
				'rate':rate,
				'quantity':quantity
			},
			success:function(content){

			},
			error:function(){
				console.log("add_To_cart_prob");
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
				// 'rate':rate
			},
			success:function(content){
				window.location.href = ' '
			},
			error:function(){
				console.log("remove_from_cart_prob");

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
					$(box).append( '<p><a>' + list[i] + '</a></p>');
				}

			},
			error:function(){
				console.log("search_prob")
			}
		})



	}
	//ADD QUANTITY

	function up_quantity(){
		error_box.innerHTML = " ";


		//HOW TO GET TEXT AFTER USING SIBLINGS???????????????
		var quantity = parseInt($(this).prev().text());
		var new_quantity = quantity+1;
		if (quantity>= 10) {
			error_box.innerHTML = "max quantity you can order is  10"
			return

		}
		var name = $(this).closest('li').find('p.name').text();
		var rate = $(this).closest('li').find('p.rate').text();

		$.ajax({
			url: 'increase/',
			method:'GET',
			data:{
				'name':name,
				'quantity':new_quantity
			},
			success:function(context){

		

		

			},
			error:function(){
				console.log("up_quantity_prob")

			}
	
		
		})
		//THIS NOT WORKS IF WRITTEN IN SUCCESS FUNCTION HWY???
				if(new_quantity<=10){
				$(this).prev().text(new_quantity);
			}
		//HOW TO GET TEXT AFTER USING SIBLINGS???????????????
		
		
		

	}
	// DOWN QUANTITY
	function down_quantity(){
		error_box.innerHTML =" "
		var quantity = parseInt($(this).next().text());
		var new_quantity = quantity-1;

		var name = $(this).closest('li').find('p.name').text();
		var rate = $(this).closest('li').find('p.rate').text();
		if(new_quantity<=0){
			error_box.innerHTML = "min quantity 0 is reached"
			//CALL remove_from_cart FUNCTION HERE	
			return

				}

			$.ajax({
			url:'decrease/' ,
			method:'GET',
			data:{
				'name':name,
				'quantity':new_quantity

			},
			success:function(){


			},
			error:function(){
				
			}
		})
		$(this).next().text(new_quantity);
		console.log($(this).next().text(new_quantity));
	

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


		 //DECREASE and INCREASE QUANTITY
		error_box =document.getElementById(config['error_box']);
		$('.up').click(up_quantity);
		$('.down').click(down_quantity);




		
	}
	return {
		init:init
	}
}())



