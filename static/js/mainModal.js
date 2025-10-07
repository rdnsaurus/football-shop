window.initModalHandlers = function(jsonByIdUrlTemplate, currentUser, noImageUrl) {
  window.showModalById = async function(id) {
    const modal = document.getElementById('detailsModal');
    const modalContent = document.getElementById('detailsModalContent');
    const accButton = document.getElementById('userAccess');
    const deleteButton = document.getElementById('deleteBtn');
    const editButton = document.getElementById('editBtn');

    try {
      const API_URL = jsonByIdUrlTemplate.replace('00000000-0000-0000-0000-000000000000', id);
      const response = await fetch(API_URL);
      const deliver = await response.json(); 
      
      if (!response.ok) throw new Error('Failed to fetch item details');

      const item = deliver[0];
      const access = Boolean(item.user == currentUser);

      document.getElementById('modalUser').textContent = item.user ? `Item by ${item.user}` : 'Item by Unknown';
      document.getElementById('modalImg').src = item.thumbnail || noImageUrl;
      document.getElementById('modalTitle').textContent = item.name || 'No Name';
      document.getElementById('modalDesc').textContent = item.description || 'No description.';
      document.getElementById('modalStock').textContent = item.stock ?? 0;
      document.getElementById('modalPrice').textContent = `Rp ${Number(item.price ?? 0).toLocaleString('id-ID')}`;

      modal.classList.remove('hidden');

      if (access) {
        accButton.classList.remove('hidden');
        
        if (deleteButton) {
          deleteButton.setAttribute('onclick', `deleteItem('${id}', event)`);
        }

        if (editButton) {
          editButton.setAttribute('onclick', `showEditModal('${id}', event)`);
        }
      } else {
        accButton.classList.add('hidden');
      }

      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50);
    } catch (err) {
      console.error(err);
      alert('Failed to load item details');
    }
  };

  window.hideModal = function() { 
    const modal = document.getElementById('detailsModal');
    const modalContent = document.getElementById('detailsModalContent'); 

    modalContent.classList.remove('opacity-100', 'scale-100'); 
    modalContent.classList.add('opacity-0', 'scale-95'); 

    setTimeout(() => { modal.classList.add('hidden'); }, 150); 
  };
};