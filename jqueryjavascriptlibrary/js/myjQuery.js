{/* for big code thane write inside document ready use for problem se bachne ke liye */ }
// document.ready start
$(document).ready(function () {
    // Your jQuery code here:-

    //console.log($);
    //console.log(jQuery);
    console.log("We are using jQuery");
    //This is jquery syntax
    //$('selector').action();

    // Element selector example like p
    // $('p').click();
    // $('p').click(function () {
    //     console.log('you clicked on p', this);
    //     //$('p').hide();
    //     //$('p').show();
    //     //$(this).hide()
    //     //for id and class selector
    //     //$('#id').hide();
    //     //$('.class').hide()
    // });//do this when click on p

    // events:-
    // $('p').dblclick(function () {
    //     console.log('you double clicked on p', this);
    // });
    // $('p').mouseenter(function () {
    //     console.log('you entered: ', this);
    // });
    // $('p').hover(function () {
    //     console.log('you hovered on: ', this);
    // },
    //     function () {
    //         console.log("Thanks for coming")
    //     });


    // there are three main type of selector in jQuery
    //1.Element Selector
    //2.Id Selector
    //3.Class Selector

    // Id Selector example:-
    //$('#second').click();

    //Class Secector:-
    //$('.odd').click();

    // other selectors
    //$('*').click() // click on all element
    //$('p.odd').click() // p jiska class odd hai
    //$('p:first').click() // first paragraph of p
    console.log("My new javaScripts Code")

    // Event in jQuery 
    // Mouse events = click, dbclick, mouseenter, mouseleave
    // KeyboardEvent = keypress, keydown, MediakeyStatusMap
    // from events = submit, change, focus, blur
    // document/window events = load, raise, scroll,uniload

    // demoing the "on method as multiple element add":-
    $('p').on(
        {
            click: function () {
                console.log("Thanks for clicking", this);
            },
            mouseleave: function () {
                console.log("mouseleave")
            }
        })

    // $('#wiki').hide(1000)
    // function call when hide than print hidden
    // $('#wiki').hide(1000, function () {
    //     console.log("hidden")
    // })
    // function call when show than print show
    // $('#wiki').show(1000, function () {
    //     console.log("show")
    // })
    // $('#wiki').show()

    // For button toggle
    // $('#but').click(function () {
    //     $('#wiki').toggle(1000)
    // })

    // for slide method- argument speed and callbacke(another func has parameter after end execution than start other function)
    // call back parameter optional
    // $('#wiki').slideUp(1000);
    // $('#wiki').slideDown(1000)
    // $('#wiki').slideToggle(1000)
    // $('#wiki').click(function(){
    //     $('#wiki').slideToggle(1000);
    // })

    // for animation
    // $('#wiki').animate({
    //     opacity: 0.3,
    //     height: '15px',
    //     width: '35px'
    // }, 2000)
    // }, 'slow') // same as 2000 second use slow/fast

    // custom animation
    // $('#wiki').animate({ opacity: 0.3 }, 4000);
    // $('#wiki').animate({ opacity: 0.9 }, 1000);
    // $('#wiki').animate({ width: '350px' }, 1000);

    // for text area use .val
    // console.log($('#ta').val());
    // change value inside textarea
    // console.log($('#ta').val("my namne is prabhash"));
    // change html inside any tags
    // console.log($('#ta').html('setting it to prabhash'));
    // remove  or content kahali
    // console.log($('#wiki').empty());
    // added text inside tags
    // console.log($('#wiki').text("you are intelligent"));
    // remove element thorogh dom
    // console.log($('#wiki').remove());
    // console.log($('#wiki').addClass('myclass'));
    // console.log($('#wiki').addClass('myclass2'));
    // console.log($('#wiki').removeClass('myclass'));
    // console.log($('#wiki').toggleClass('myclass'));

    // for css
    $('#wiki').css('background-color', 'gray')
    $('#wiki').css('color', 'white')

    // For usin jQuery AJAX(art of exchanging the data withing server without reloading)
    // method like GET
    // a=$.get("https://code.jquery.com/jquery-3.7.1.js")
    // console.log(a)
    // $.get("https://code.jquery.com/jquery-3.7.1.js", function (data, status) {
    //     alert(status)
    // })
    // post method syntax
    $.post("https://code.jquery.com/jquery-3.7.1.js", { name: "Prabhash", about: 'infosys engineer' },
        function (data, status) {
            alert(status)
        });

});// document.ready end
