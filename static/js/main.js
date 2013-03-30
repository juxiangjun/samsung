function do_query(){
	form = $("#frmQuery").serialize();
	$.post('/do_query',form, function(a) {
		$("#div_query_result").html(a);
	})
}

$(function() {
	$("#qry_start_date").datepicker({dateFormat:"yy-mm-dd"});
	$("#qry_end_date").datepicker({dateFormat:"yy-mm-dd"});
});

function show_edit_form(id){
	var url = '/show_edit_form'
	$.post(url,{'id':id},function(a){
		$("#dlgEditForm").html(a);
	});
	$("#dlgEditForm").dialog({width:700,height:350,modal:true});
}

function delete_sale_item(id) {
	var url = "/delete_sale_item?id="+id
	window.location.href  = url
}

function save_sale_item(close){
	var form = $('#frmSale')
	$.post('/save_sale_item',form.serialize(), function(a) {
		if (a=='success') {
			if (close == 0) {
				var url = '/show_edit_form'
				$.post(url,{'id':'-1'},function(a){
					$("#dlgEditForm").html(a);
				});
			} else {
				window.location.href = "/show_main_page";
			}
		} else {
			$("#dlg_errors").html(a);
			$("#dlg_errors").dialog({width:700,height:350,modal:true});
		}
	})
}

function set_filter(id,  value, target){
	$('a[name=lbl_'+target+']').each(
		function(){
			$(this).removeClass('lbl_selected');
		}
	);
	if (value == '0') {
		value = ''
	}
	$('#qry_'+target).attr('value', value);
	$('#'+id).addClass('lbl_selected');
	do_query()
}
