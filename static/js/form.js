
function Complete()
          {
            var json=JSON.stringify({
								"name" : 	document.form.name.value,
                "email" : document.form.email.value,
                "message" : document.form.message.value
							});
							var xhr = new XMLHttpRequest();
							xhr.open("POST", '/form', true);
							xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

							xhr.send(json);
              //alert('SENT!');
							xhr.onreadystatechange = function()
        			{
								if (xhr.readyState==4 && xhr.status==200)
                {
                  var resp = JSON.parse(xhr.responseText);
                  //alert(resp);

                  alert(resp['res']);
                  if(resp['meta']){
                    //alert('Clear');
                    document.getElementsByName('form')[0].reset();
                  }
                }
              }
            }
