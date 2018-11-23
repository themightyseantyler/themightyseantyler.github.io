$(".parent").each(function(index){
    var group = $(this).data("group");
    var parent = $(this);

    parent.change(function(){  
         $(group).prop('checked', parent.prop("checked"));
    });
    $(group).change(function(){ 
        parent.prop('checked', false);
        if ($(group+':checked').length == $(group).length ){
            parent.prop('checked', true);
        }
    });
});

/* 
Source: https://www.sanwebe.com/question/multiple-lists
User: Saran 
Date: 29th Aug 2016
*/






$(".checkAll").on("click", function() {
    $(".parent").prop("checked", !clicked);
    $(".group1").prop("checked", !clicked);
    $(".group2").prop("checked", !clicked);
    $(".group3").prop("checked", !clicked);
    $(".group4").prop("checked", !clicked);
    $(".group5").prop("checked", !clicked);
    $(".group6").prop("checked", !clicked);
    clicked = !clicked;
});
