
$( function() {
	// jquery-ui绑定tab
	$( "#tabs" ).tabs();
	//生成tabs内list的内容
	var item_json={name:"program name"};
	add_item('#tabs-1', item_json);
} );

function add_item(dom_id, item_json){
	var $item = $("<p></p>").text(item_json.name);
	$item.click(item_json, show_info);
	$(dom_id).append($item);
}

function show_info(e){
　　alert(e.data.name);
}
