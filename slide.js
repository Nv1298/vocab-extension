var $slider = document.getElementById('slider1');
$slider.addEventListener('click', function() {
    var isOut = $slider.classList.contains('slide-out');
    $slider.setAttribute('class', isOut ? 'slide-in' : 'slide-out');
    
});

//second tab
var $slider2 = document.getElementById('slider2');
$slider2.addEventListener('click', function() {
    var isOut = $slider2.classList.contains('slide-out');
    $slider2.setAttribute('class', isOut ? 'slide-in' : 'slide-out');
});

//third tab
var $slider3 = document.getElementById('slider3');
$slider3.addEventListener('click', function() {
	var isOut = $slider3.classList.contains('slide-out');
	$slider3.setAttribute('class', isOut ? 'slide-in' : 'slide-out');
});

// fourth tab
var $slider4 = document.getElementById('slider4');
$slider4.addEventListener('click', function() {
    var isOut = $slider4.classList.contains('slide-out');
	$slider4.setAttribute('class', isOut ? 'slide-in' : 'slide-out');
});

//fifth tab
var $slider5 = document.getElementById('slider5');
$slider5.addEventListener('click', function() {
    var isOut = $slider5.classList.contains('slide-out');
	$slider5.setAttribute('class', isOut ? 'slide-in' : 'slide-out');
});

//sixth tab
var $slider6 = document.getElementById('slider6');
$slider6.addEventListener('click', function() {
    var isOut = $slider6.classList.contains('slide-out');
    $slider6.setAttribute('class', isOut ? 'slide-in' : 'slide-out');
});
