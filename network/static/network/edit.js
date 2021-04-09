document.addEventListener('DOMContentLoaded',function(){
    view1 = document.querySelectorAll('.comments1');
    for(var i = 0; i < view1.length; i++){
        view1[i].style.display = "none"; 
    }
    let edit = document.querySelectorAll('.edit');
    edit.forEach(link => {
        link.onclick = (event) => {
           const Body = event.target.parentElement;
           let id = Body.getAttribute('id')
           const z = document.querySelector(`#comments1-${id}`);
           Body.style.display = 'none';
           z.style.display = "block";
           t = document.querySelector(`#submit-${id}`)
           Ncontent = document.querySelector(`#comment-cont1-${id}`)
           t.onclick = () =>{
                fetch('/edit/' + id, {
                    method: 'PUT',
                    body: JSON.stringify({
                        post: Ncontent.value
                    })
                  });
                  z.style.display = 'none';
                  document.querySelector(`#comment-cont-${id}`).innerHTML = Ncontent.value;
                  s = document.querySelector(`#comment-cont-${id}`).parentElement;
                  s.style.display = 'block';
           }
        }
    })
});
