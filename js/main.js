/* ==========================================================================================
  Theme Name: Musiziya
  Author: VS_THEMES
  Description: Musician & Band HTML Template
  Version: 1.0
========================================================================================== */

/* =============== JS Index

01. Preloader fade out
02. Owl Sliders
03. Magnific pop up
04. Mobile menu integration
05. Nice Selector
06. Wow animation 
07. Light slider
08. Other js

=============== */
(function($) {
    "use strict";

    /*------------------------------------------------------------------------------*/
    /*01. Preloader fade out
/*------------------------------------------------------------------------------*/
    $(window).on('load', function() {
        $('.loader-out').delay('300').fadeOut(1000);
    });

    /*------------------------------------------------------------------------------*/
    /*02. Owl Sliders
/*------------------------------------------------------------------------------*/

    // Banner slider 1
    var banner1 = $('.main-slider');
    banner1.owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        autoplayTimeout: 6000,
        autoplayHoverPause: true,
        smartSpeed: 450,
        margin: 0,
        nav: true,
        navText: ["<img src='img/icons/che-le.png' />", "<img src='img/icons/che-ri.png' />"],
        dots: true
    });

    banner1.on('change.owl.carousel', function(event) {
        var el = event.target;
        $('.banner-text-left', el).addClass('wow fadeInLeft animated')
            .one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
                $('.banner-text-left', el).removeClass('wow fadeInLeft animated');
            });
    });

    // Blog listing slider 
    $('.slider-type-blog').owlCarousel({
        loop: true,
        margin: 0,
        autoplay: true,
        nav: true,
        dots: false,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        navText: ["<i class='fas fa-chevron-left'></i>", "<i class='fas fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1,
                margin: 0
            },
            1200: {
                items: 1
            }
        }
    });

    // portfolio slider
    var teamSlide = $('.team-slider');
    teamSlide.owlCarousel({
        loop: true,
        margin: 50,
        autoplay: true,
        nav: false,
        dots: false,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            400: {
                items: 1
            },
            550: {
                items: 2
            },
            768: {
                items: 2
            },
            830: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    });

    // testimonial slider
    var testimonialSlide = $('.testi-slider');
    testimonialSlide.owlCarousel({
        loop: true,
        margin: 0,
        autoplay: true,
        nav: false,
        dots: false,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            }
        }
    });

    // Relative product slider
    var reprdtSlider = $('.relative-prdt-slider');
    reprdtSlider.owlCarousel({
        loop: true,
        margin: 30,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimeout: 4000,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    });
    // Custom blog nav buttons
    $('.prdt-nav-left').on('click', function() {
        event.preventDefault();
        reprdtSlider.trigger('prev.owl.carousel');
    });
    $('.prdt-nav-right').on('click', function() {
        event.preventDefault();
        reprdtSlider.trigger('next.owl.carousel');
    });

    /*------------------------------------------------------------------------------*/
    /*03. Magnific pop up
/*------------------------------------------------------------------------------*/
    $('.popup-video').magnificPopup({
        type: 'iframe'
    });

    $('.gallery-links').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        }
    });

    /*------------------------------------------------------------------------------*/
    /*04. Mobile menu integration
/*------------------------------------------------------------------------------*/
    // Mobile menu integration index 1
    $('.main-menu-1').meanmenu({
        meanMenuContainer: '.mobile-menu1',
        meanScreenWidth: "991"
    });

    /*------------------------------------------------------------------------------*/
    /*05. Nice Selector
/*------------------------------------------------------------------------------*/
    //nice select
    $('select').niceSelect(); // changing all select input style

    /*------------------------------------------------------------------------------*/
    /*06. Wow animation 
/*------------------------------------------------------------------------------*/
    new WOW().init();

    /*------------------------------------------------------------------------------*/
    /* 07. Light slider
    /*------------------------------------------------------------------------------*/

    // product detail image slider
    $('#image-gallery').lightSlider({
        gallery: true,
        item: 1,
        thumbItem: 5,
        slideMargin: 15,
        speed: 500,
        auto: false,
        loop: true,
        onSliderLoad: function() {
            $('#image-gallery').removeClass('cS-hidden');
        }
    });

    /*------------------------------------------------------------------------------*/
    /*08. Other js
/*------------------------------------------------------------------------------*/
    $(window).on('scroll', function() {
        ////fade in  footer button on scroll
        if ($(this).scrollTop() > 800) {
            $(".scrol-tp").addClass("opacity-10"); //showing scroll up button
        } else {
            $(".scrol-tp").removeClass("opacity-10"); //hiding scroll up button
        }

    });

    //scroll to top on cllick footer button
    $(".scrol-tp").on('click', function(event) {
        event.preventDefault();
        $("html, body").animate({
            scrollTop: 0
        }, 800);
    });

    // color switch
    $(".each-color.co1").on('click', function(e) {
        var data1 = $(this).data('color');
        $(".color-changing").attr('href', data1);
    });

    $(".each-color.co2").on('click', function(e) {
        var data1 = $(this).data('color');
        $(".color-changing").attr('href', data1);
    });

    $(".each-color.co3").on('click', function(e) {
        var data1 = $(this).data('color');
        $(".color-changing").attr('href', data1);
    });

    $(".each-color.co4").on('click', function(e) {
        var data1 = $(this).data('color');
        $(".color-changing").attr('href', data1);
    });

    $(".each-color.co5").on('click', function(e) {
        var data1 = $(this).data('color');
        $(".color-changing").attr('href', data1);
    });

    $(".each-color.co6").on('click', function(e) {
        var data1 = $(this).data('color');
        $(".color-changing").attr('href', data1);
    });

})(jQuery); // End jQuery