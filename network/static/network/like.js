document.addEventListener('DOMContentLoaded',function(){
    let like = document.querySelectorAll(".like");
    like.forEach(link =>{
        link.onclick = (event) => {
            let Body = event.target.parentElement
            id = Body.id
        if (link.id ===(`like-${id}`)){    
            fetch(`/like/${id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    like: true
                })
            })
            document.getElementById(`like-${id}`).innerHTML='&#9829';
            document.getElementById(`like-${id}`).className=('like1');
            document.getElementById(`like-${id}`).id=(`like1-${id}`);
            var Count = document.getElementById(`count-${id}`);
            var number = Count.innerHTML;
            number++;
            Count.innerHTML = number;
        }
        else if(link.id ===(`like1-${id}`)){
            fetch(`/like/${id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    like: false
                })
            })
            document.getElementById(`like1-${id}`).innerHTML = '&#9825';
            document.getElementById(`like1-${id}`).id=(`like-${id}`);
            var Count = document.getElementById(`count-${id}`);
            var number = Count.innerHTML;
            number--;
            Count.innerHTML = number;
        }
    }
    })            
});