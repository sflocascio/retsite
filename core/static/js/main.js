// document.querySelectorAll('.modal-button').forEach(function(el) {
// 	el.addEventListener('click', function() {
// 	  var target = document.querySelector(el.getAttribute('data-target'));
	  
// 	  target.classList.add('is-active');
	  
// 	  target.querySelector('.modal-close').addEventListener('click',   function() {
// 		  target.classList.remove('is-active');
// 	   });
// 	});
//   });



var refs = {
	modalEdicion: {
	  open: function() { document.getElementById('modalEdicion').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion').classList.remove('is-active');
						
	  }
	}
  };


  var refs1 = {
	modalEdicion1: {
	  open: function() { document.getElementById('modalEdicion1').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion1').classList.remove('is-active');
						
	  }
	}
  };

  var refs3 = {
	modalEdicion3: {
	  open: function() { document.getElementById('modalEdicion3').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion3').classList.remove('is-active');
						
	  }
	}
  };

  var refs4 = {
	modalEdicion4: {
	  open: function() { document.getElementById('modalEdicion4').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion4').classList.remove('is-active');
						
	  }
	}
  };

  var refs5 = {
	modalEdicion5: {
	  open: function() { document.getElementById('modalEdicion5').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion5').classList.remove('is-active');
						
	  }
	}
  };

  var refs6 = {
	modalEdicion6: {
	  open: function() { document.getElementById('modalEdicion6').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion6').classList.remove('is-active');
						
	  }
	}
  };

  var refs7 = {
	modalEdicion7: {
	  open: function() { document.getElementById('modalEdicion7').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion7').classList.remove('is-active');
						
	  }
	}
  };

  var refs8 = {
	modalEdicion8: {
	  open: function() { document.getElementById('modalEdicion8').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion8').classList.remove('is-active');
						
	  }
	}
  };

  var refs9 = {
	modalEdicion9: {
	  open: function() { document.getElementById('modalEdicion9').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion9').classList.remove('is-active');
						
	  }
	}
  };

  var refs10 = {
	modalEdicion10: {
	  open: function() { document.getElementById('modalEdicion10').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion10').classList.remove('is-active');
						
	  }
	}
  };

  var refs11 = {
	modalEdicion11: {
	  open: function() { document.getElementById('modalEdicion11').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion11').classList.remove('is-active');
						
	  }
	}
  };

  var refs12 = {
	modalEdicion12: {
	  open: function() { document.getElementById('modalEdicion12').classList.add('is-active');
	  },
	  close:function() { document.getElementById('modalEdicion12').classList.remove('is-active');
						
	  }
	}
  };

  


// class BulmaModal {
// 	constructor(selector) {
// 		this.elem = document.querySelector(selector)
// 		this.close_data()
// 	}
	
// 	show() {
// 		this.elem.classList.toggle('is-active')
// 		this.on_show()
// 	}
	
// 	close() {
// 		this.elem.classList.toggle('is-active')
// 		this.on_close()
// 	}
	
// 	close_data() {
// 		var modalClose = this.elem.querySelectorAll("[data-bulma-modal='close'], .modal-background")
// 		var that = this
// 		modalClose.forEach(function(e) {
// 			e.addEventListener("click", function() {
				
// 				that.elem.classList.toggle('is-active')

// 				var event = new Event('modal:close')

// 				that.elem.dispatchEvent(event);
// 			})
// 		})
// 	}
	
// 	on_show() {
// 		var event = new Event('modal:show')
	
// 		this.elem.dispatchEvent(event);
// 	}
	
// 	on_close() {
// 		var event = new Event('modal:close')
	
// 		this.elem.dispatchEvent(event);
// 	}
	
// 	addEventListener(event, callback) {
// 		this.elem.addEventListener(event, callback)
// 	}
// }

// var btn1 = document.querySelector("#btn1")
// var mdl1 = new BulmaModal("#myModal1")

// var btn2 = document.querySelector("#btn2")
// var mdl2 = new BulmaModal("#myModal2")


// // var $modals = getAll('.modal');
// // var $modalButtons = getAll('.modal-button');

// // BTN 1
// btn1.addEventListener("click", function () {
// 	mdl1.show()
// })
// mdl1.addEventListener('modal:show', function() {
// 	console.log("opened")
// })
// mdl1.addEventListener("modal:close", function() {
// 	console.log("mdl1closed")
// })

// // BTN 2
// btn2.addEventListener("click", function () {
// 	mdl2.show()
// })
// mdl2.addEventListener('modal:show', function() {
// 	console.log("mdl2opened")
// })
// mdl2.addEventListener("modal:close", function() {
// 	console.log("mdl2closed")
// })


// document.addEventListener('DOMContentLoaded', () => {
//     (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
//       $notification = $delete.parentNode;
  
//       $delete.addEventListener('click', () => {
//         $notification.parentNode.removeChild($notification);
//       });
//     });
//   });


//var accordions = bulmaAccordion.attach();



