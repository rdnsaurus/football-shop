window.initDeleteHandler = function(deleteUrlTemplate) {
  const modal = document.getElementById('confirmModal');
  const yesBtn = document.getElementById('confirmYes');
  const noBtn = document.getElementById('confirmNo');
  let currentId = null;

  window.deleteItem = async function(id, e) {
    if (e) e.preventDefault();
    currentId = id;
    modal.classList.remove('hidden');
    modal.classList.add('flex');
  };

  noBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    currentId = null;
  });

  yesBtn.addEventListener('click', async () => {
    if (!currentId) return;

    const DELETE_URL = deleteUrlTemplate.replace(
      '00000000-0000-0000-0000-000000000000',
      currentId
    );

    try {
      const response = await fetch(DELETE_URL, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken')
        }
      });

      modal.classList.add('hidden');
      modal.classList.remove('flex');

      if (response.ok) {
        if (typeof window.fetchItems === 'function') window.fetchItems();
        if (typeof window.hideModal === 'function') window.hideModal();

        document.dispatchEvent(new CustomEvent('itemDeleted'));
      } else {
        document.dispatchEvent(new CustomEvent('itemDeletedFailed'));
        showToast('Gagal menghapus item', 'error');
      }
    } catch (error) {
      console.error('Error:', error);
      showToast('Terjadi kesalahan saat menghapus!', 'error');
    } finally {
      currentId = null;
    }
  });
};
