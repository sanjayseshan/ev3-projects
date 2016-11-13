/*window.addEventListener('load', eventWindowLoaded, false);	
function eventWindowLoaded() {
    canvasApp();
}

function canvasSupport () {
    return Modernizr.canvas;
}

colorChosen =  'black'
function canvasApp(){  
    if (!canvasSupport()) {
	return;
    }else{
	var theCanvas = document.getElementById('sketch');
	var context = theCanvas.getContext('2d');
/*	var redButton = document.getElementById("Red");
	var orangeButton = document.getElementById("Orange");
	var yellowButton = document.getElementById("Yellow");
	var greenButton = document.getElementById("Green");
	var blueButton = document.getElementById("Blue");
	var purpleButton = document.getElementById("Purple");
	var brownButton = document.getElementById("Brown");
	var blackButton = document.getElementById("Black");
	var whiteButton = document.getElementById("White");
	var colorChosen = document.getElementById("color_chosen");
	var resetButton = document.getElementById("reset_image");
        redButton.addEventListener('click', colorPressed, false);
        orangeButton.addEventListener('click', colorPressed, false);
        yellowButton.addEventListener('click', colorPressed, false);
        greenButton.addEventListener('click', colorPressed, false);
        blueButton.addEventListener('click', colorPressed, false);
        purpleButton.addEventListener('click', colorPressed, false);
        brownButton.addEventListener('click', colorPressed, false);
        blackButton.addEventListener('click', colorPressed, false);
        whiteButton.addEventListener('click', colorPressed, false);
        resetButton.addEventListener('click', resetPressed, false);
	drawScreen();
    }

    function drawScreen() {
	theCanvas.addEventListener('mousedown', mouse_pressed_down, false);
	theCanvas.addEventListener('mousemove', mouse_moved, false);
	theCanvas.addEventListener('mouseup', mouse_released, false);
	theCanvas.addEventListener('touchmove', touch_move_gesture, false);
	theCanvas.addEventListener('touchstart', touch_pressed_down, false);

	var imageObj = new Image();
//	imageObj.src = 'mat.jpg';
        imageObj.onload = function() {
            context.drawImage(imageObj, 0, 0, theCanvas.width, theCanvas.height);
        };

	context.fillStyle = 'white';
	context.fillRect(0, 0, theCanvas.width, theCanvas.height);
	context.strokeStyle = '#000000'; 
	context.strokeRect(1,  1, theCanvas.width-2, theCanvas.height-2);
    }

    // For the mouse_moved event handler.
    var begin_drawing = false;

    function mouse_pressed_down (ev) {
	var x, y;	
	// Get the mouse position in the canvas
	x = ev.pageX;
	y = ev.pageY;

// remove
	context.strokeStyle = colorChosen.innerHTML;
	context.lineWidth = 4;
	context.beginPath();
	context.moveTo(x, y);

	begin_drawing = true;
	context.fillStyle = colorChosen.innerHTML;
    }

    function touch_pressed_down (ev) {
	var x, y;	
	// Get the mouse position in the canvas
	var touch = ev.touches[0];
	x = touch.pageX;
	y = touch.pageY;

// remove
	context.strokeStyle = colorChosen.innerHTML;
	context.lineWidth = 4;
	context.beginPath();
	context.moveTo(x-50, y-50);

	begin_drawing = true;
	context.fillStyle = colorChosen.innerHTML;
    }

    function mouse_moved (ev) {
	var x, y;	
	// Get the mouse position in the canvas
	x = ev.pageX;
	y = ev.pageY;

	if (begin_drawing) {
// remove
	    context.lineTo(x, y);
	    context.stroke();

// remove
//	    context.beginPath();
//	    context.arc(x, y, 7, (Math.PI/180)*0, (Math.PI/180)*360, false);
//	    context.fill();
//          context.closePath();
	}
    }

    function mouse_released (ev) {
	begin_drawing = false;
    }

    function touch_move_gesture (ev) {
	// For touchscreen browsers/readers that support touchmove
	var x, y;
	ev.preventDefault(); //override default UI behavior for better results on touchscreen devices

// remove
//	context.beginPath();

	context.fillStyle = colorChosen.innerHTML;
	context.strokeStyle = colorChosen.innerHTML;
//	context.lineWidth = 4;
	if(ev.touches.length == 1){
	    var touch = ev.touches[0];
	    x = touch.pageX-50;
	    y = touch.pageY-50;
// remove
	    context.lineTo(x, y);
	    context.stroke();

// remove
//	    context.arc(x, y, 7, (Math.PI/180)*0, (Math.PI/180)*360, false);
//	    context.fill();
	}
    }

    function colorPressed(e) {
	var color_button_selected = e.target;
	var color_id = color_button_selected.getAttribute('id');
	colorChosen.innerHTML = color_id;
    }

    function resetPressed(e) {
        theCanvas.width = theCanvas.width; // Reset grid
        drawScreen();
    }
}

        

  


*/



    // Variables for referencing the canvas and 2dcanvas context
    var canvas,ctx;

    // Variables to keep track of the mouse position and left-button status 
    var mouseX,mouseY,mouseDown=0;

    // Variables to keep track of the touch position
    var touchX,touchY;
        r=0; g=0; b=0; a=255;

    // Keep track of the old/last position when drawing a line
    // We set it to -1 at the start to indicate that we don't have a good value for it yet
    var lastX,lastY=-1;
    // Draws a line between the specified position on the supplied canvas name
    // Parameters are: A canvas context, the x position, the y position, the size of the dot
    function drawLine(ctx,x,y,size) {

        // If lastX is not set, set lastX and lastY to the current position 
        if (lastX==-1) {
            lastX=x;
	    lastY=y;
        }

        // Let's use black by setting RGB values to 0, and 255 alpha (completely opaque)
        ctx.strokeStyle = "rgba("+r+","+g+","+b+","+(a/255)+")";

        // Select a fill style

        // Set the line "cap" style to round, so lines at different angles can join into each other
        ctx.lineCap = "round";
        //ctx.lineJoin = "round";


        // Draw a filled line
        ctx.beginPath();

	// First, move to the old (previous) position
	ctx.moveTo(lastX,lastY);

	// Now draw a line to the current touch/pointer position
	ctx.lineTo(x,y);

        // Set the line thickness and draw the line
        ctx.lineWidth = penwidth;
        ctx.stroke();

        ctx.closePath();

	// Update the last position to reference the current position
	lastX=x;
	lastY=y;
    } 

    // Clear the canvas context using the canvas width and height
    function clearCanvas(canvas,ctx) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    // Keep track of the mouse button being pressed and draw a dot at current location
    function sketchpad_mouseDown() {
        mouseDown=1;
        drawLine(ctx,mouseX,mouseY,12);
    }

    // Keep track of the mouse button being released
    function sketchpad_mouseUp() {
        mouseDown=0;

        // Reset lastX and lastY to -1 to indicate that they are now invalid, since we have lifted the "pen"
        lastX=-1;
        lastY=-1;
    }

    // Keep track of the mouse position and draw a dot if mouse button is currently pressed
    function sketchpad_mouseMove(e) { 
        // Update the mouse co-ordinates when moved
        getMousePos(e);

        // Draw a dot if the mouse button is currently being pressed
        if (mouseDown==1) {
            drawLine(ctx,mouseX,mouseY,12);
        }
    }

    // Get the current mouse position relative to the top-left of the canvas
    function getMousePos(e) {
        if (!e)
            var e = event;

        if (e.offsetX) {
            mouseX = e.offsetX;
            mouseY = e.offsetY;
        }
        else if (e.layerX) {
            mouseX = e.layerX;
            mouseY = e.layerY;
        }
     }

    // Draw something when a touch start is detected
    function sketchpad_touchStart() {
        // Update the touch co-ordinates
        getTouchPos();

        drawLine(ctx,touchX,touchY,12);

        // Prevents an additional mousedown event being triggered
        event.preventDefault();
    }

    function sketchpad_touchEnd() {
        // Reset lastX and lastY to -1 to indicate that they are now invalid, since we have lifted the "pen"
        lastX=-1;
        lastY=-1;
    }

    // Draw something and prevent the default scrolling when touch movement is detected
    function sketchpad_touchMove(e) { 
        // Update the touch co-ordinates
        getTouchPos(e);

        // During a touchmove event, unlike a mousemove event, we don't need to check if the touch is engaged, since there will always be contact with the screen by definition.
        drawLine(ctx,touchX,touchY,12); 

        // Prevent a scrolling action as a result of this touchmove triggering.
        event.preventDefault();
    }

    // Get the touch position relative to the top-left of the canvas
    // When we get the raw values of pageX and pageY below, they take into account the scrolling on the page
    // but not the position relative to our target div. We'll adjust them using "target.offsetLeft" and
    // "target.offsetTop" to get the correct values in relation to the top left of the canvas.
    function getTouchPos(e) {
        if (!e)
            var e = event;

        if(e.touches) {
            if (e.touches.length == 1) { // Only deal with one finger
                var touch = e.touches[0]; // Get the information for finger #1
                touchX=touch.pageX-touch.target.offsetLeft;
                touchY=touch.pageY-touch.target.offsetTop;
            }
        }
    }


    // Set-up the canvas and add our event handlers after the page has loaded
    function init() {
        // Get the specific canvas element from the HTML document
        canvas = document.getElementById('sketch');

        // If the browser supports the canvas tag, get the 2d drawing context for this canvas
        if (canvas.getContext)
            ctx = canvas.getContext('2d');

        // Check that we have a valid context to draw on/with before adding event handlers
        if (ctx) {
            // React to mouse events on the canvas, and mouseup on the entire document
            canvas.addEventListener('mousedown', sketchpad_mouseDown, false);
            canvas.addEventListener('mousemove', sketchpad_mouseMove, false);
            window.addEventListener('mouseup', sketchpad_mouseUp, false);

            // React to touch events on the canvas
            canvas.addEventListener('touchstart', sketchpad_touchStart, false);
            canvas.addEventListener('touchend', sketchpad_touchEnd, false);
            canvas.addEventListener('touchmove', sketchpad_touchMove, false);
        }
    }


init()
