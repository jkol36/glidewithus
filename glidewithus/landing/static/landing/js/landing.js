function getSelectedText() {
        if (window.getSelection) {
            return window.getSelection().toString();
        } else if (document.selection) {
            return document.selection.createRange().text;
        }
        return '';
    }
	$(function() {
				var Translations = {
    translate_button: {
      
      show_original_description : 'Show original description',
      translate_this_description : 'Translate this description to English'
    },
    per_month: "per month",
    long_term: "Long Term Policy",
    clear_dates: "Clear Dates"
  }
       var date = new Date();
var currentMonth = date.getMonth();
var currentDate = date.getDate();
var currentYear = date.getFullYear();

	   jQuery( "#checkoutdate2" ).datepicker({
                minDate: 1,
                maxDate: "+2Y",
                nextText: "",
                prevText: "",
                numberOfMonths: 1,
                // closeText: "Clear Dates",
                currentText: Translations.today,
                showButtonPanel: true,
                onClose: function(dateText, inst) { 
                	
	 		 	jQuery('.advanced_search').show();
                     
     },
      onSelect: function(dateText, inst) { 

    	if(checkin_status != 1) {
       	
        d = jQuery('#checkindate2').datepicker('getDate');
         if(!d)
         {
         	var d = new Date();
         	 d.setDate(d.getDate()); // add int nights to int date
		$("#checkindate2").datepicker("option", "minDate", d);
         }
         else
         {
         	d.setDate(d.getDate()); // add int nights to int date
		$("#checkindate2").datepicker("option", "minDate", d);
         }
   
    	setTimeout(function () 
		{
			$("#checkindate2").datepicker("show")
                                }, 0)   
                                
           k = (d.getMonth()+1)+"/"+d.getDate()+"/"+d.getFullYear();

         jQuery( "#checkindate2" ).val(k) ; 
        }
        }       
	    });
	  var checkin_status = 0;
	    jQuery( "#checkindate2" ).datepicker({
			    minDate: date,
                maxDate: "+2Y",
                nextText: "",
                prevText: "",
                numberOfMonths: 1,
                currentText: Translations.today,
                showButtonPanel: true,
	 onClose: function(dateText, inst) { 
	 	 
	 				
	 	jQuery('.advanced_search').show();
                  
		  
    },
    onSelect: function(dateText, inst) {
    	
    	checkin_status = 1;
          d = jQuery('#checkindate2').datepicker('getDate');
         if(!d)
         {
         	var d = new Date();
         	 d.setDate(d.getDate()+1); // add int nights to int date
		jQuery("#checkoutdate2").datepicker("option", "minDate", d);
         }
         else
         {
         	d.setDate(d.getDate()+1); // add int nights to int date
		jQuery("#checkoutdate2").datepicker("option", "minDate", d);
         }
    	setTimeout(function () 
		{
			jQuery("#checkoutdate2").datepicker("show")
                                }, 0)   
                                
           k = (d.getMonth()+1)+"/"+d.getDate()+"/"+d.getFullYear();

         jQuery( "#checkoutdate2" ).val(k) ;       
    }
	   });
    });
 
$(document).ready(function(){

	jQuery("#close_search1").click(function(){
			 jQuery("#advanced_search").fadeOut();
           
	
});
jQuery("#close_search").click(function(){
			 jQuery("#advanced_search").fadeOut();
           
	
});
});
    
$(document).ready(function () {
	
      var input = document.getElementById('searchTextField');
    autocomplete = new google.maps.places.Autocomplete(input);    
    google.maps.event.addListener(autocomplete, 'place_changed', function() {
        	 	$('.advanced_search').show();
           
            
// now call it automaitically on page load
jQuery('#checkindate2').trigger('click');
    });
    
});

function disableEnterKey(e){
    
//create a variable to hold the number of the key that was pressed     
var key;
 
    //if the users browser is internet explorer
    if(window.event){
      
    //store the key code (Key number) of the pressed key
    key = window.event.keyCode;
      
    //otherwise, it is firefox
    } else {
      
    //store the key code (Key number) of the pressed key
    key = e.which;     
    }
      
    //if key 13 is pressed (the enter key)
    if(key == 13){
      
    //do nothing
    
    return false;
      
    //otherwise
    } else {
      
    //continue as normal (allow the key press for keys other than "enter")
    return true;
    }
      
//and don't forget to close the function    
}

unction addZero(i)
  {
    if (i<10)
    {
      i="0" + i;
    }
    return i;
  }
  setInterval(function() {
    function addZero(i)
    {
      if (i<10)
      {
        i="0" + i;
      }
      return i;
    }
    
    var d1 = new Date (),
        d = new Date ( d1 );
    d.setMinutes ( d1.getMinutes() + 42 );
    d.setSeconds ( d1.getSeconds() - 10 );
    var s =(d.getSeconds());
    var m =(d.getMinutes());
    
    var x = document.getElementById("time_show");
    var d = addZero(59 - m) + ":" + addZero(59 - s);
    
    t = d;
    
    x.innerHTML = 'Demo self refreshes in '+t;
  }
              , 250)

window.NREUM||(NREUM={}),__nr_require=function(t,n,e){function r(e){if(!n[e]){var o=n[e]={exports:{}};t[e][0].call(o.exports,function(n){var o=t[e][1][n];return r(o?o:n)},o,o.exports)}return n[e].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<e.length;o++)r(e[o]);return r}({D5DuLP:[function(t,n){function e(t,n){var e=r[t];return e?e.apply(this,n):(o[t]||(o[t]=[]),void o[t].push(n))}var r={},o={};n.exports=e,e.queues=o,e.handlers=r},{}],handle:[function(t,n){n.exports=t("D5DuLP")},{}],G9z0Bl:[function(t,n){function e(){var t=l.info=NREUM.info;if(t&&t.agent&&t.licenseKey&&t.applicationID&&p&&p.body){l.proto="https"===f.split(":")[0]||t.sslForHttp?"https://":"http://",i("mark",["onload",a()]);var n=p.createElement("script");n.src=l.proto+t.agent,p.body.appendChild(n)}}function r(){"complete"===p.readyState&&o()}function o(){i("mark",["domContent",a()])}function a(){return(new Date).getTime()}var i=t("handle"),u=window,p=u.document,s="addEventListener",c="attachEvent",f=(""+location).split("?")[0],l=n.exports={offset:a(),origin:f,features:[]};p[s]?(p[s]("DOMContentLoaded",o,!1),u[s]("load",e,!1)):(p[c]("onreadystatechange",r),u[c]("onload",e)),i("mark",["firstbyte",a()])},{handle:"D5DuLP"}],loader:[function(t,n){n.exports=t("G9z0Bl")},{}]},{},["G9z0Bl"])
window.NREUM||(NREUM={});NREUM.info={"beacon":"beacon-5.newrelic.com","licenseKey":"cc04cdf8d5","applicationID":"3472979","transactionName":"YgZTYUAHWBdTV0QNWVtMcFZGD1kKHXxfCVMaCl9RVx4=","queueTime":0,"applicationTime":694,"ttGuid":"","agentToken":"","atts":"TkFQFwgdSxk=","errorBeacon":"bam.nr-data.net","agent":"js-agent.newrelic.com\/nr-411.min.js"}
