window.initEditHandlers = function(editUrlTemplate, jsonByIdUrlTemplate) {
  window.showEditModal = async function(id, e) {
    hideModal();
    if (e) {
      e.preventDefault();
    }

    const modal = document.getElementById('editItemModal');
    
    try {
      const API_URL = jsonByIdUrlTemplate.replace('00000000-0000-0000-0000-000000000000', id);

      const response = await fetch(API_URL);
      
      if (!response.ok) throw new Error('Failed to fetch item');
      
      const deliver = await response.json();
      const item = deliver[0];
      
      // Populate form
      document.getElementById('edit_item_id').value = id;
      document.getElementById('edit_name').value = item.name || '';
      document.getElementById('edit_price').value = item.price || '';
      document.getElementById('edit_description').value = item.description || '';
      document.getElementById('edit_thumbnail').value = item.thumbnail || '';
      document.getElementById('edit_category').value = item.category || '';
      document.getElementById('edit_stock').value = item.stock || '';
      
      // Show modal
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to load item data');
    }
  };

  window.editItemEntry = async function(event) {
    event.preventDefault();
    const form = document.querySelector('#editItemForm');
    const itemId = document.querySelector('#edit_item_id').value;

    const url = editUrlTemplate.replace('00000000-0000-0000-0000-000000000000', itemId);
    const csrftoken = form.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch(url, {
        method: "POST",
        headers: { "X-CSRFToken": csrftoken },
        body: new FormData(form),
    });

    const data = await response.json();
    if (data.status === 'success') {
        hideEditModal();
        document.dispatchEvent(new CustomEvent('itemEditted'));

        if (typeof window.fetchItems === 'function') window.fetchItems();
    } else {
        document.dispatchEvent(new CustomEvent('itemEdittedFailed'));
        alert('Failed to update item');
    }
  };

  // Hide edit modal
  window.hideEditModal = function() {
    const modal = document.getElementById('editItemModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  };
};