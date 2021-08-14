const deleteBtn = document.querySelector('#delete-button');
deleteBtn.onclick = (e) => {
      fetch('/venues/' + e.target.dataset['id'] , {
        method: 'DELETE',
        redirect: 'follow'
      })
    }