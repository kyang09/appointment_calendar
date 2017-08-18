
/*
 * Front-End Code for Appointment Calendar
 * by Kevin Yang
 * 
 * I planned to use ReactJS, but for now I'll use jQuery due to time constraint.
 */

(function () {
    var winWidth = $(window).width();
    var winHeight = $(window).height();
    var calendar = $('#calendar');

    function displayAppointment(appointment) {
        console.log(appointment);
    }

    $.getJSON('/rest_appointment/',

        function (data) { 
            $(data).each(function (index, apt) { 
                data.parent = calendar;
                displayAppointment(apt);
            });
        }
    );
})();