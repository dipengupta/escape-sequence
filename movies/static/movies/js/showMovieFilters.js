$(document).ready(function(){

    //user defined function to hide all reviews
    function onPageStartHideReviews() {
        $(".genres").hide();
        $(".moods").hide();
        $(".ratings").hide();
        $(".all_movies").hide();
        $(".placeholder").show();
    }
    

    //this will be called only once
    onPageStartHideReviews();


    $(".genres_button").click(function(){
        $(".genres").show();
        $(".moods").hide();
        $(".ratings").hide();
        $(".all_movies").hide();
        $(".placeholder").hide();
    });



    $(".moods_button").click(function(){
        $(".genres").hide();
        $(".moods").show();
        $(".ratings").hide();
        $(".all_movies").hide();
        $(".placeholder").hide();
    });



    $(".ratings_button").click(function(){
        $(".genres").hide();
        $(".moods").hide();
        $(".ratings").show();
        $(".all_movies").hide();
        $(".placeholder").hide();
    });



    $(".all_movies_button").click(function(){
        $(".genres").hide();
        $(".moods").hide();
        $(".ratings").hide();
        $(".all_movies").show();
        $(".placeholder").hide();
    });




});


