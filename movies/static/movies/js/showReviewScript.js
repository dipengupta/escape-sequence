$(document).ready(function(){


    //user defined function to hide all reviews
    function onPageStartHideReviews() {
        $(".review_ankur").hide();
        $(".review_dipen").hide();
        $(".review_shantnu").hide();
        $(".review_ashesh").hide();
        $(".review_jayant").hide();
        $(".review_placeholder").show();
    }
    

    //this will be called only once
    onPageStartHideReviews();


    $(".review_ankur_button").click(function(){
        $(".review_ankur").show();
        $(".review_dipen").hide();
        $(".review_shantnu").hide();
        $(".review_ashesh").hide();
        $(".review_jayant").hide();
        $(".review_placeholder").hide();
    });



    $(".review_dipen_button").click(function(){
        $(".review_ankur").hide();
        $(".review_dipen").show();
        $(".review_shantnu").hide();
        $(".review_ashesh").hide();
        $(".review_jayant").hide();
        $(".review_placeholder").hide();
    });



    $(".review_shantnu_button").click(function(){
        $(".review_ankur").hide();
        $(".review_dipen").hide();
        $(".review_shantnu").show();
        $(".review_ashesh").hide();
        $(".review_jayant").hide();
        $(".review_placeholder").hide();
    });



    $(".review_ashesh_button").click(function(){
        $(".review_ankur").hide();
        $(".review_dipen").hide();
        $(".review_shantnu").hide();
        $(".review_ashesh").show();
        $(".review_jayant").hide();
        $(".review_placeholder").hide();
    });



    $(".review_jayant_button").click(function(){
        $(".review_ankur").hide();
        $(".review_dipen").hide();
        $(".review_shantnu").hide();
        $(".review_ashesh").hide();
        $(".review_jayant").show();
        $(".review_placeholder").hide();
    });


});


