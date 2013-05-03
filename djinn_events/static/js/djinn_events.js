/**
 * Djinn events JS lib
 */

// Use pg namespace
if (djinn == undefined) {
    var djinn = {};
}


djinn.events = {};


/** 
 * Calculate end time for given start time in format HH:mm.
 */
djinn.events.calc_end_time = function(hourstr) {

  if (!hourstr || hourstr.len < 5) {
    return "";
  }

  var hour = parseInt(hourstr.substr(0, 3));

  if (hour >= 23) {
    return "00:00";
  }

  var newhour = "" + (hour + 1);

  if (newhour.length == 1) {
    newhour = "0" + "" + newhour;
  }

  return newhour + ":" + hourstr.substr(3);
};


$(document).ready(function() {
   
    $(document).on("click", "input[name='djinn_events_full_day']", function(e) {
        $("#id_start_time").toggle();
        $("#id_start_time").val("");        
        $("#id_end_time").toggle();
        $("#id_end_time").val("");                
      });    

    // Naive implementation that does string wise comparison
    $(document).on("change", ".event #id_start_date", function(e) {
        if (!$("#id_end_date").val()) {
          $("#id_end_date").val($("#id_start_date").val());
        } else if ($("#id_end_date").val() < $("#id_start_date").val()) {
          $("#id_end_date").val($("#id_start_date").val());
        }
      });

    // Naive implementation that does string wise comparison
    $(document).on("change", ".event #id_start_time", function(e) {
        if ($("#id_end_time").val().substr(0, 3) <= $("#id_start_time").val().substr(0, 3)) {
          $("#id_end_time").val(djinn.events.calc_end_time($("#id_start_time").val()));
        }
      });
  });
