$(document).ready(function(){
  $(".dropdown-button").dropdown({hover: false});
  $('.dropdown-content').click(function(e) {
    if(!(this.getAttribute("data-closeonclick")=="true")){
      e.stopPropagation();
    }
  });


  $(".button-collapse").sideNav();

  $('.parallax').parallax();
  $('select').material_select();
  $('.datepicker').pickadate({
    selectMonths: true,
    selectYears: 130,
    startDate:'1 January 1950',
  });
  
  $('.modal-trigger').leanModal();

  $('.bxslider').bxSlider({
    minSlides: 9,
    maxSlides: 9,
    slideWidth: 220,
    slideMargin: 20,
    ticker: true,
    tickerHover: true,
    speed: 1000 * 20,
    caption: true,
    autoHover:true,
  });

  $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });

  $('.slider').slider({
    full_width: true,
    height:350,
    transition:400,
    interval:3500
  });

});
