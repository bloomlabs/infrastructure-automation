// Implement Leap Motion slide swipe
var timeout = null;
var swipedAt = new Date().getTime();

var controllerOptions = {
  enableGestures: true
};

Leap.loop(controllerOptions, function(frame) {

  // Display Gesture object data
  if (frame.gestures.length > 0) {
    for (var i = 0; i < frame.gestures.length; i++) {
      var gesture = frame.gestures[i];
      if (gesture.type == "swipe") {
        //Classify swipe as either horizontal or vertical
        var isHorizontal = Math.abs(gesture.direction[0]) > Math.abs(gesture.direction[1]);
        //Classify as right-left or up-down
        if (isHorizontal) {
          console.log('phase 1');

          swipedAtNew = new Date().getTime();
          if (swipedAtNew > (swipedAt - 500)) {



            swipedAt = swipedAtNew;

            console.log('detected');
            data.stop();
            clearTimeout(timeout);
            timeout = setTimeout(function() {
              data.start();
              console.log('restarting');
            }, 30000);
            if (gesture.direction[0] > 0) {
              if (gesture.state == 'start') {
                //data.next();
                data.prev();
                console.log('eee');
              }
            } else {
              if (gesture.state == 'start') {
                console.log('eee');
                //data.prev();
                data.next();
              }
            }
          }
        }

      }
    }
  }

});