// static/js/itemForm.js

function showItemForm() {
  const modal = document.getElementById('itemFormModal');
  if (modal) {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
  } else {
    console.error('Modal #itemFormModal not found!');
  }
}

function hideItemFormModal() {
  const modal = document.getElementById('itemFormModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }
}

window.initCreateItemHandler = function(createUrl) {
  window.addItemEntry= async function(event) {
    event.preventDefault();
    const form = document.querySelector('#itemForm');
    if (!form) {
      console.error('Form #itemForm not found!');
      return false;
    }

    try {
      const csrftoken = form.querySelector('[name=csrfmiddlewaretoken]').value;

      const response = await fetch(createUrl, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
        },
        body: new FormData(form),
      });

      if (response.ok) {
        form.reset();
        hideItemFormModal();
        
        document.dispatchEvent(new CustomEvent('itemAdded'));
        
        if (typeof window.fetchItems === 'function') {
          window.fetchItems();
        }
      } else {
        const errorText = await response.text();
        document.dispatchEvent(new CustomEvent('itemAddedFailed'));

        console.error('Failed to save:', response.status, errorText);
        alert('Failed to save item: ' + errorText);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error saving item: ' + error.message);
    }

    return false;
  }
};