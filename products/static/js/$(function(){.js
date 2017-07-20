var module =(function(){
	var el = null;
	var box = null;
	function change_it(){
		console.log($(this).previosSibling.innerHTML)
		
	

	}
	function init(config){
		box = document.getElementById(config['diver'])
		$('.yoy').click(change_it);
	}
	return {
		init:init
	}
}())



