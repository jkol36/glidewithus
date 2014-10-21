var jumboHeight = $('.jumbotron').outerHeight();
function parallax(){
    var scrolled = $(window).scrollTop();
    $('.bg').css('height', (jumboHeight-scrolled) + 'px');
    $('.bg').css('background-size',(''));
}
$(window).scroll(function(e){
    parallax();
});