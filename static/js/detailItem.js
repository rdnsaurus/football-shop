window.initItemDisplay = function(apiUrl) {
  const grid = document.getElementById('grid');
  const loading = document.getElementById('loading');
  const error = document.getElementById('error');
  const empty = document.getElementById('empty');

  window.fetchItems = async function() {
    console.log('Fetched mas');
    loading.classList.remove('hidden');
    
    try {
      const response = await fetch(apiUrl);
      if (!response.ok) throw new Error('Failed to fetch data');
      const data = await response.json();
      loading.classList.add('hidden');

      if (!Array.isArray(data) || data.length === 0) {
        empty.classList.remove('hidden');
        grid.innerHTML = '';
        return;
      }

      grid.innerHTML = ''; 
      data.forEach(itemObj => {
        const item = itemObj.fields || itemObj; 
        const id = item.id;

        const card = document.createElement('div');
        card.className = "bg-white rounded-2xl shadow-md hover:shadow-lg transition-shadow my-6 flex flex-col";

        card.innerHTML = `
          <div class="h-40 overflow-hidden rounded-t-2xl bg-gray-100 flex items-center justify-center">
            <img src="${item.thumbnail}" alt="${item.name || ''}" class="h-60 object-cover rounded-t-2xl">
          </div>
          <div class="p-4 flex flex-col flex-grow">
            <h3 class="text-xl font-semibold text-gray-900">${(item.name || '').substring(0, 12)}</h3>
            <p class="text-gray-600 text-sm mb-2">${(item.description || '').split(' ').slice(0, 15).join(' ')}...</p>
            <div class="mt-auto">
              <p class="text-sm text-gray-500">Stock: <span class="font-medium">${item.stock ?? 0}</span></p>
              <p class="text-lg font-bold text-red-600 truncate">Rp ${Number(item.price ?? 0).toLocaleString('id-ID')}</p>
              <div class="flex justify-between items-center mt-3">
                <button onclick="showModalById('${id}')" class="text-red-600 hover:underline">Details</button>
                <button class="bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-xl">Add to Cart</button>
              </div>
            </div>
          </div>
        `;
        grid.appendChild(card);
      });
    } catch (err) {
      console.error(err);
      loading.classList.add('hidden');
      error.classList.remove('hidden');
    }
  };

  // Initial fetch
  fetchItems();
};